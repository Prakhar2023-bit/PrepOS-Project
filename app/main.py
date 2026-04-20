from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. Import CORS
from app.db.session import engine, Base
from app.models import user, roadmap 
from app.api.routes import users, roadmaps 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PrepOS API", version="1.0.0")

# 2. Add the CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Allow your Next.js frontend
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(roadmaps.router, prefix="/roadmaps", tags=["Roadmaps"])

@app.get("/")
async def health_check():
    return {"status": "online"}