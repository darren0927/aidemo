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
        name="__hello_world__",
        func=__hello_world__,
        description='''
            这个一个测试工具，当用户输入的问题中有个测试的意图时，你可以使用此工具。
            '''
    )