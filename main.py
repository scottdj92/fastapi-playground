from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
  name: str
  description: str | None = None

app = FastAPI()

@app.get('/')
async def root():
  return {"message": "hello world"}

@app.post('/product')
async def create_product(product: Product):
  return product
