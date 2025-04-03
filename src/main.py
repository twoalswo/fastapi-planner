from fastapi import FastAPI 
from .routes.events import event_router
from .routes.user import user_router  

app = FastAPI()

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