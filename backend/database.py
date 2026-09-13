# File: backend/database.py
from sqlalchemy.ext.declarative import declarative_base

# Tạo Base model giả
Base = declarative_base()

# Tạo hàm get_db giả
def get_db():
    yield None