from fastapi import FastAPI

app = FastAPI()

@app.get("/action")
async def root():
    # Do something ...
    return {"message": "success"}
