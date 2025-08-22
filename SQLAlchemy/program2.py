from sqlalchemy import create_engine

# this is line is for connecting python to db 
engine = create_engine("sqlite:///movies.db")  # SQLite DB file
