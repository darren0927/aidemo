
from llm import LLMLoader
from langchain.agents import load_tools, AgentType
from langchain.agents import AgentExecutor, create_structured_chat_agent, initialize_agent
from langchain import hub

from tools import TestTool


def run_new(query):

    try:
        # 1、定义大模型为自定义大模型（调用智谱LLM的API）
        llm = LLMLoader.load_llm()

        # 2、定义agent需要调用的工具
        tools = load_tools(["requests_all", "llm-math"], llm=llm, allow_dangerous_tools=True)
        tools.append(TestTool.load_tool())

        # 3、定义提示词模板
        prompt = hub.pull("hwchase17/structured-chat-agent")

        #4、打印提示词模板
        print("#################### 使用如下提示词模板 ####################\n")
        prompt.pretty_print()

        agent = create_structured_chat_agent(llm, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools)

        # 5、执行agent
        print("#################### 开始调用agent ####################")
        return agent_executor.invoke(query)
    except Exception as e:
        print("agent执行发生异常", e)
        raise Exception(status_code=500, detail=str(e))


def run(query):

    try:
        # 1、定义大模型为自定义大模型（调用智谱LLM的API）
        llm = LLMLoader.load_llm()

        # 2、定义agent需要调用的工具
        tools = load_tools(["requests_all", "llm-math"], llm=llm, allow_dangerous_tools=True)
        tools.append(TestTool.load_tool())

        # 3、初始化agent
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

        # 4、执行agent
        print("#################### 开始调用agent ####################")
        return agent.run(query)
    except Exception as e:
        print("agent执行发生异常", e)
        raise Exception(status_code=500, detail=str(e))


