from typing import Union
from fastapi import FastAPI
# 모든 데이터 검증은 Pydantic에서 검증
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None, q2: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "q2": q2}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}