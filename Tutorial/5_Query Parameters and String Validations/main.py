from typing import List, Union
from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(
    # default=Required, # 값이 입력되어야 함을 명시(Required 대신 ... 사용 가능)
    default= ["foo", "bar"],
    title="Query string",
    description="Query string for the items to search in the database that have a good match",
    min_length=3, max_length=50, # q의 최소길이 3, 최대 길이를 50자로 지정
    alias="item_query", # 벌칭 설정 가능
    deprecated=True, # 파라미터를 사용할수는 있지만 추천하지 않을때
   # include_in_schema=False, # 파라미터를 사용하지 않을때, 사용 불가
    #regex="^a" # 정규표현식(a로 시작)
)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results