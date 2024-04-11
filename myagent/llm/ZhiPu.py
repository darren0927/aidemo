from langchain.llms.base import LLM
from typing import Dict, List, Optional, Tuple, Union, Any, Iterator, Type

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LanguageModelInput
from langchain_core.outputs import GenerationChunk
from langchain_core.runnables import Runnable
from pydantic import BaseModel
from zhipuai import ZhipuAI

from config import ZhipuConfig


class CustomLLM(LLM):

    max_token: int = 10000
    temperature: float = 0.1
    top_p = 0.9
    history = []

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "ChatGLM"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:

        print("#################### 使用如下提示词模板 ####################\n")
        print(prompt)

        # 获取LLM相关配置
        config = ZhipuConfig.from_json()

        # 调用ZhiPuAI的SDK
        client = ZhipuAI(api_key=config.api_key)

        response = client.chat.completions.create(
            model="glm-4v",  # 填写需要调用的模型名称
            messages=[{"role": "user", "content": prompt}],
        )
        result_content = response.choices[0].message.content
        self.history = self.history + [[None, response.choices[0].message]]
        return result_content

    def _stream(self, prompt: str, stop: Optional[List[str]] = None,
                run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> Iterator[GenerationChunk]:
        pass

    def with_structured_output(self, schema: Union[Dict, Type[BaseModel]], **kwargs: Any) -> Runnable[
        LanguageModelInput, Union[Dict, BaseModel]]:
        pass
