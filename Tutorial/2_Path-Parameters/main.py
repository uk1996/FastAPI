from enum import Enum

from fastapi import FastAPI

# 유효하고 미리 정의할 수 있는 미리 정의할 수 있는 경로 매개변수 값을 원할떄
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item:id": item_id}

# 순차적으로 평가되기 떄문에 /user/me 를 /users/{user_id}보다 먼저 배치해야 /users/me가 제대로 동작함
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    print(model_name.value)
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# 경로 매개변수로 path를 받아야 할떄(Ex> /home/cswook96/file.txt)
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}