from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-categories")
async def root():
    return {"message": "Hello World"}

@app.get("/get-customers")
async def root():
    return {"message": "Hello World"}

@app.get("/get-products")
async def root():
    return {"message": "Hello World"}

@app.get("/get-orders")
async def root():
    return {"message": "Hello World"}


