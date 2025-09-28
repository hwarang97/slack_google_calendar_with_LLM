import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/slack/command/gcl")
async def handle_google_calendar_command():  # naming
    return "It works"


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
