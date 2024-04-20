import os
from sqlmodel import create_engine

# DB URL
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Set up the SQLModel engine
engine = create_engine(DATABASE_URL)
