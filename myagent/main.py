# main.py
from fastapi import FastAPI
from pydantic import ValidationError

from controller.MyAgentController import router as zhipu_router

import uvicorn

app = FastAPI()

# 注册 ZhihuController 的路由器
app.include_router(zhipu_router)

# 启动服务
if __name__ == "__main__":
    try:
        # 启动服务
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except ValidationError as e:
        print(f"Validation error: {e.json()}")  # 打印验证错误
    except Exception as e:
        print(f"Error Run: {e}")