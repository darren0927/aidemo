from langchain.agents import Tool
from chain import TDMindChain
from llm import LLMLoader


def __hello_world__(query: str):
    hello_world_chain = TDMindChain.TDMindChain(llm=LLMLoader.load_llm())
    response = hello_world_chain.run({'question': query})
    print("############## 调用测试工具 __hello_world__")
    return response


def load_tool() -> Tool:
    return Tool(
        name="hello_world",
        func=__hello_world__,
        description='''
            这是一个礼貌工具，当你在回答问题时可以先调用此工具。
            '''
    )