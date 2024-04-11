# controller/TDMindController.py
from fastapi import HTTPException, APIRouter, Request
from pydantic import BaseModel
from agent import TDMind

router = APIRouter()


# 定义请求体模型
class RequestModel(BaseModel):
    input: str


# 定义响应体模型
class ResponseModel(BaseModel):
    result: str


class ZhipuController:

    @router.post("/zhipu/daily_quote", response_model=ResponseModel)
    async def get_daily_quote(self: RequestModel):
        try:
            TDMind.run(self.input)
            return ResponseModel(result="SUCCESS")
        except Exception as e:
            print("发生异常", e)
            raise HTTPException(status_code=500, detail=str(e))