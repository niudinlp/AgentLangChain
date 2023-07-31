# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/27
Description   :
"""
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner


# set enviroment key: OPENAI_API_KEY SERPAPI_API_KEY
# e.g: os.environ["OPENAI_API_KEY"] = "xxxxx", or export OPENAI_API_KEY=xxxx in shell

search = SerpAPIWrapper()
tools = [
	Tool(
		name = "Current Search",
		func=search.run,
		description="useful for when you need to answer questions about current events or the current state of the world"
	),
]


model = ChatOpenAI(temperature=0)

planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)


query = "tell me who won the world cup in 1978?"

