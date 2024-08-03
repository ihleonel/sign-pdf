from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    # Do something ...
    return {"message": "success !!!", 'status': 200}
