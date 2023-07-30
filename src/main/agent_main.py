# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/27
Description   :
"""
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import ConversationalAgent
# from langchain.agents import initialize_agent

# set enviroment key: OPENAI_API_KEY SERPAPI_API_KEY
# e.g: os.environ["OPENAI_API_KEY"] = "xxxxx", or export OPENAI_API_KEY=xxxx in shell
llm = ChatOpenAI()

search = SerpAPIWrapper()

tools = [
	Tool(
		name = "Current Search",
		func=search.run,
		description="useful for when you need to answer questions about current events or the current state of the world"
	),
]


agent = ConversationalAgent.from_llm_and_tools(llm, tools)

query = "tell me who won the world cup in 1978?"

