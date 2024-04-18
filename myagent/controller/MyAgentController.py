# controller/MyAgentController.py
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from agent import MyAgent

router = APIRouter()


# 定义请求体模型
class RequestModel(BaseModel):
    input: str


# 定义响应体模型
class ResponseModel(BaseModel):
    result: str


class MyAgentController:

    @router.post("/agent/daily_quote", response_model=ResponseModel)
    async def get_daily_quote(self: RequestModel):
        try:
            ret = MyAgent.run(self.input)
            print(f"返回值 = {ret}")
            return ResponseModel(result=ret)
        except Exception as e:
            print("发生异常", e)
            raise HTTPException(status_code=500, detail=str(e))