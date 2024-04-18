from langchain.agents import Tool
from langchain import LLMChain, PromptTemplate
from chain import TDMindChain
from llm import LLMLoader
from datetime import datetime

prompt_template = """
#角色
你是一个时间处理大师
#前提
当用户的问题涉及到时间问题，你可以使用此工具获取当前时间
#职责
你的职责是保障回答的内容不会过时，根据工具获取到的今天日期时间进行参考，以此可以返回相对实时的最新数据给用户
#限制
只输出具体的时间值就好，不需要附加信息
问题
{question}
 """


def __get_current_time__(query: str):
    print("############## 调用工具获取当前时间 __get_current_time__")
    print(f"############## 输入参数 query = {query}")
    td_mind_chain = TDMindChain.TDMindChain(
        llm=LLMLoader.load_llm(),
        prompt=PromptTemplate(template=prompt_template, input_variables=['question'])
    )
    # 获取当前的日期和时间
    now = datetime.now()
    # 使用strftime方法格式化日期和时间
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    # 打印格式化后的日期和时间
    print("格式化后的当前日期和时间：", formatted_now)
    response = td_mind_chain.run({'question': query, 'cur_time': formatted_now})
    return response


def load_tool() -> Tool:
    return Tool(
        name="__get_current_time__",
        func=__get_current_time__,
        description='''
            这是一个获取当前时间的工具，为了保障相对实时和准确的数据返回给用户，你可以调用此工具获取当前的最新时间作为参考，避免回去严重过时的信息给用户，尤其是在获取一些经济指标时通常你需要给用户回答最近的数据，这个时间工具就可以帮助到你了。
            '''
    )