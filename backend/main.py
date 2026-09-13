# File: backend/main.py
from fastapi import FastAPI

app = FastAPI(title="Family Connect API")

# Route mặc định để kiểm tra API sống hay không
@app.get("/")
def read_root():
    return {"message": "Welcome to Family Connect API"}
