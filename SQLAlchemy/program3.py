from sqlalchemy import Table, Column, Integer, String, MetaData,create_engine,insert,select

engine = create_engine("sqlite:///movies.db")
# Create a container for all tables
metadata = MetaData()

# Define a "students" table
students = Table(
    "students", metadata,
    Column("id", Integer, primary_key=True),  # unique student ID
    Column("name", String),                   # student name
    Column("age", Integer)                    # student age
)

# Actually create the table inside movies.db
metadata.create_all(engine)

# Adding Data to the database #


# Create an insert statement
ins = students.insert().values(id=2, name="Altaf", age=22)

# Open a connection to the database
conn = engine.connect()

# Execute the insert
conn.execute(ins)

# Commit the changes (SQLite auto-commits, but it's good practice)
conn.commit()



# printing the data from the table 

# Create a SELECT statement
stmt = select(id=2)

# Execute the statement
result = conn.execute(stmt)

# Fetch and print all rows
for row in result:
    print(row)

conn.close()