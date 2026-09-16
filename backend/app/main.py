from fastapi import FastAPI
from app.api.routes import api_router  # Đường dẫn import router tổng của dự án

app = FastAPI(
    title="FamilyConnect API",
    description="Backend API cho ứng dụng quản lý gia đình FamilyConnect",
    version="1.0.0"
)

# Nhúng toàn bộ routes (bao gồm /auth, /events,...) vào ứng dụng
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "FamilyConnect Backend API đang chạy thành công!"}