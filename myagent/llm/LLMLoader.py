import os
import dashscope
from langchain.llms import Tongyi
from llm.ZhiPuLLM import ZhiPuApiLLM
from conf.conf import AppConfig
from conf.conf import QWenConfig


def load_llm():
    try:

        config = AppConfig.from_json()
        qwen_config = QWenConfig.from_json()

        if config.model_name == 'qwen':
            dashscope.api_key = qwen_config.api_key
            os.environ["DASHSCOPE_API_KEY"] = qwen_config.api_key
            return Tongyi(model=config.model_name, temperature=0.8)
        if config.model_name =='zhipu':
            return ZhiPuApiLLM()
        else:
            raise Exception(status_code=500, detail="model is not support!!!")
    except Exception as e:
        print("模型加载失败", e)
        raise Exception(status_code=500, detail=str(e))