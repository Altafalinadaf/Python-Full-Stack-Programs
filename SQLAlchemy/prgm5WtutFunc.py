from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

# --------------------------
# Database Setup
# --------------------------
engine = create_engine("sqlite:///students.db")   # connect to SQLite DB
metadata = MetaData()

# Define "students" table
students = Table(
    "students", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),  # auto-increment ID
    Column("name", String),
    Column("age", Integer)
)

# --------------------------
# 1. Create Table
# --------------------------
metadata.create_all(engine)
print("Table created successfully!")

# --------------------------
# 2. Insert Single Record
# --------------------------
# with means “use this resource, and when I’m done, clean it up automatically.”
with engine.connect() as conn:
    conn.execute(students.insert().values(name="Khaleel", age=22))
    conn.commit()
print("Inserted: Khaleel, 22")

# --------------------------
# 3. Insert Multiple Records
# --------------------------
data_list = [
    {"name": "Sanju", "age": 21},
    {"name": "Nikil", "age": 23},
    {"name": "Raju", "age": 20}
]

with engine.connect() as conn:
    conn.execute(students.insert(), data_list)
    conn.commit()
print("Multiple records inserted!")

# --------------------------
# 4. Print All Records
# --------------------------
with engine.connect() as conn:
    result = conn.execute(select(students))
    rows = result.fetchall()
    print("\nAll Students:")
    for row in rows:
        print(row)

# --------------------------
# 5. Print Filtered Records
# --------------------------
with engine.connect() as conn:
    stmt = select(students).where(students.c.age > 21)
    result = conn.execute(stmt)
    rows = result.fetchall()
    print("\nStudents older than 21:")
    for row in rows:
        print(row)
