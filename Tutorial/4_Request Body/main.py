from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str = "choi"
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int, q: Union[str, None] = None):
    print(f"data_dict: {item.dict()}")
    print(f"name: {item.name}")
    print(f"description: {item.description}")
    print(f"price: {item.price}")
    print(f"tax: {item.tax}")

    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})

    return result