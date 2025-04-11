from contextlib import asynccontextmanager
from fastapi import FastAPI 
from .routes.events import event_router
from .routes.users import user_router
from fastapi.middleware.cors import CORSMiddleware 
from src.database.connection import Settings

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 코드를 구현하면 서버 시작할때
    await settings.initialize_database()
    yield
    # 서버 종료시 정리해야할 작업들

app = FastAPI(
    lifespan=lifespan
)
app.include_router(event_router)
app.include_router(user_router)

@app.get("/")
async def root_path():
    return "hello world!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main.app",
        host = "127.0.0.1",
        port = 8000,
        reload = True
    )