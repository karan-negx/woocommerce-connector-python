from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from woocommerce.import_orders import ImportOrders


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-invoice/{order_id}")
async def get_invoice_by_order_id(order_id:str):
# https://bootsnipp.com/snippets/9gjD
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


