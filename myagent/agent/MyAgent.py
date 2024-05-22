from langchain.memory import ConversationBufferMemory
from llm import LLMLoader
from langchain.agents import load_tools, AgentType, ZeroShotAgent
from langchain.agents import AgentExecutor, initialize_agent
from langchain import LLMChain
from tools import HelloWorldTool, AlphavantageClientTool
from tools import DateTimeTool

prefix = """Answer the following questions as best you can, You have access to the 
    following tools: """
suffix = """Begin! Remember to speak as a personal assistant to give the final answer."
Question: {input}
{agent_scratchpad}
"""


def run_new(query):

    try:
        # 1、定义大模型为自定义大模型（调用智谱LLM的API）
        llm = LLMLoader.load_llm()

        # 2、定义agent需要调用的工具
        tools = load_tools(["requests_all", "llm-math"], llm=llm, allow_dangerous_tools=True)
        tools.append(HelloWorldTool.load_tool())
        tools.append(DateTimeTool.load_tool())
        tools.append(AlphavantageClientTool.load_tool())

        # 3、定义提示词模板
        # prompt = hub.pull("hwchase17/structured-chat-agent")

        prompt = ZeroShotAgent.create_prompt(
            tools,
            prefix=prefix,
            suffix=suffix,
            input_variables=["input", "agent_scratchpad"]
        )

        #4、打印提示词模板
        print("#################### 使用如下提示词模板 ####################\n")
        prompt.pretty_print()

        # 5、记忆功能
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        tool_names = [tool.name for tool in tools]
        agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, memory=memory,
                                                            verbose=True, handle_parsing_errors=True, )
        # 6、执行agent
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
        tools.append(HelloWorldTool.load_tool())
        tools.append(DateTimeTool.load_tool())
        tools.append(AlphavantageClientTool.load_tool())

        # 3、初始化agent
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

        # 4、执行agent
        print("#################### 开始调用agent ####################")
        return agent.run(query)
    except Exception as e:
        print("agent执行发生异常", e)
        raise Exception(status_code=500, detail=str(e))


