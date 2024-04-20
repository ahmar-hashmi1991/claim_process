from sqlmodel import Session
from sqlmodel.sql.expression import Select, SelectOfScalar
from . import engine

# Dependency to provide a database session
def get_session():
    with Session(engine) as session:
        yield session