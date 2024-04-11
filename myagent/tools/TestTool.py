from langchain.agents import Tool
from chain import TDMindChain
from llm.ZhiPu import CustomLLM


def __hello_world__(query:str):
    hello_world_chain = TDMindChain.SqlBuildChain(llm=CustomLLM())
    response = hello_world_chain.run({'question':query})
    return response


def load_tool() -> Tool:
    return Tool(
        name="hello_world",
        func=__hello_world__,
        description='''
            这只是一个测试工具，为了达到测试效果，请你在回答任何问题时调用此工具。
            '''
    )