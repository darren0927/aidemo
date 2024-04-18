from langchain.agents import Tool
from chain import TDMindChain
from llm import LLMLoader
from datetime import datetime


def __get_current_time__(query: str):
    print("############## 调用工具获取当前时间 __get_current_time__")
    print(f"############## 输入参数 query = {query}")
    td_mind_chain = TDMindChain.TDMindChain(llm=LLMLoader.load_llm())
    # 获取当前的日期和时间
    now = datetime.now()
    # 使用strftime方法格式化日期和时间
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    # 打印格式化后的日期和时间
    print("格式化后的当前日期和时间：", formatted_now)
    response = td_mind_chain.run({'question': query +"，当前时间为" + formatted_now})
    return response


def load_tool() -> Tool:
    return Tool(
        name="__get_current_time__",
        func=__get_current_time__,
        description='''
            这是一个获取当前时间的工具，为了保障相对实时和准确的数据返回给用户，你可以调用此工具获取当前的最新时间作为参考，避免回去严重过时的信息给用户，尤其是在获取一些经济指标时通常你需要给用户回答最近的数据，这个时间工具就可以帮助到你了。
            '''
    )