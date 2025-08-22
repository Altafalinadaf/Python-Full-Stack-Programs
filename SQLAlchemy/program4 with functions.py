from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

# --------------------------
# Database Setup
# --------------------------
engine = create_engine("sqlite:///students.db")   # creates SQLite DB file
metadata = MetaData()

# Define "students" table
students = Table(
    "students", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),  # auto-increment ID
    Column("name", String),
    Column("age", Integer)
)

# --------------------------
# Functions
# --------------------------

def create_table():
    """Create the students table."""
    metadata.create_all(engine)
    print("Table created successfully!")

def insert_single(name, age):
    """Insert a single student record."""
    with engine.connect() as conn:
        conn.execute(students.insert().values(name=name, age=age))
        conn.commit()
    print(f"Inserted: {name}, {age}")

def insert_multiple(data_list):
    """Insert multiple student records at once.
       data_list should be a list of dictionaries.
    """
    with engine.connect() as conn:
        conn.execute(students.insert(), data_list)
        conn.commit()
    print("Multiple records inserted!")

def print_all():
    """Fetch and print all student records."""
    with engine.connect() as conn:
        result = conn.execute(select(students))
        rows = result.fetchall()
        for row in rows:
            print(row)

def print_filtered(min_age):
    """Fetch and print students older than min_age."""
    with engine.connect() as conn:
        stmt = select(students).where(students.c.age > min_age)
        result = conn.execute(stmt)
        rows = result.fetchall()
        for row in rows:
            print(row)

# --------------------------
# Example Usage
# --------------------------

if __name__ == "__main__":
    create_table()  # create the table

    # Insert one record
    insert_single("Altaf", 22)

    # Insert multiple records
    insert_multiple([
        {"name": "Saniya", "age": 21},
        {"name": "Rahul", "age": 23},
        {"name": "Aisha", "age": 20}
    ])

    print("\n All Students:")
    print_all()

    print("\n Students older than 21:")
    print_filtered(21)
