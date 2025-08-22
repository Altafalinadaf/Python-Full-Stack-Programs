from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, update, delete

# --------------------------
# Database Setup
# --------------------------
# Create SQLite database (students.db file will be created if not exists)
engine = create_engine("sqlite:///students.db")
metadata = MetaData()

# Define "students" table
students = Table(
    "students", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),  # Auto increment ID
    Column("name", String),  # Name of student
    Column("age", Integer)   # Age of student
)

# --------------------------
# Functions for Operations
# --------------------------

def create_table():
    """Create the students table in DB"""
    metadata.create_all(engine)
    print("Table created successfully!")

def insert_single(name, age):
    """Insert a single record"""
    with engine.connect() as conn:
        conn.execute(students.insert().values(name=name, age=age))
        conn.commit()
    print(f"Inserted: {name}, {age}")

def insert_multiple(data_list):
    """Insert multiple records at once"""
    with engine.connect() as conn:
        conn.execute(students.insert(), data_list)
        conn.commit()
    print("Multiple records inserted!")

def print_all():
    """Print all rows in the table"""
    with engine.connect() as conn:
        result = conn.execute(select(students))
        rows = result.fetchall()
        print("\nAll Students:")
        for row in rows:
            print(row)

def print_filtered(min_age):
    """Print rows where age > min_age"""
    with engine.connect() as conn:
        stmt = select(students).where(students.c.age > min_age)
        result = conn.execute(stmt)
        rows = result.fetchall()
        print(f"\nStudents older than {min_age}:")
        for row in rows:
            print(row)

def update_record(student_id, new_age):
    """Update student age by ID"""
    with engine.connect() as conn:
        stmt = update(students).where(students.c.id == student_id).values(age=new_age)
        conn.execute(stmt)
        conn.commit()
    print(f"Updated student {student_id} age to {new_age}")

def delete_record(student_id):
    """Delete a student row by ID"""
    with engine.connect() as conn:
        stmt = delete(students).where(students.c.id == student_id)
        conn.execute(stmt)
        conn.commit()
    print(f"Deleted record with id={student_id}")

def rename_table(old_name, new_name):
    """Rename an existing table"""
    with engine.connect() as conn:
        conn.execute(f"ALTER TABLE {old_name} RENAME TO {new_name}")
        conn.commit()
    print(f"Table renamed: {old_name} → {new_name}")

def rename_column(table_name, old_col, new_col):
    """Rename a column in a table"""
    with engine.connect() as conn:
        conn.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_col} TO {new_col}")
        conn.commit()
    print(f"Column renamed: {old_col} → {new_col}")

def delete_column(table_name, col_name):
    """Delete (drop) a column from a table (SQLite ≥ 3.35.0 required)"""
    with engine.connect() as conn:
        conn.execute(f"ALTER TABLE {table_name} DROP COLUMN {col_name}")
        conn.commit()
    print(f"Column dropped: {col_name}")

def drop_table(table_name):
    """Drop a table completely"""
    with engine.connect() as conn:
        conn.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
    print(f"Table {table_name} dropped!")

# --------------------------
# Example Usage
# --------------------------
if __name__ == "__main__":
    # 1. Create table
    create_table()

    # 2. Insert one student
    insert_single("Altaf", 22)

    # 3. Insert multiple students
    insert_multiple([
        {"name": "Saniya", "age": 21},
        {"name": "Rahul", "age": 23},
        {"name": "Aisha", "age": 20}
    ])

    # 4. Print records
    print_all()
    print_filtered(21)

    # 5. Update record
    update_record(1, 25)

    # 6. Delete one record
    delete_record(3)

    # 7. Rename column (age → student_age)
    rename_column("students", "age", "student_age")

    # 8. Rename table (students → learners)
    rename_table("students", "learners")

    # 9. Delete (drop) a column
    delete_column("learners", "student_age")

    # 10. Drop the whole table
    drop_table("learners")
