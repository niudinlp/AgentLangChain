# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/26
Description   : Llama2 interface
"""
import warnings
from langchain.llms.base import BaseLLM
from langchain.schema import LLMResult


class Llama2(BaseLLM):
	"""
	Llama2 interface
	Llama2-Chinese-13b-chat
	Meta-Llama2-7b-chat
	Meta-Llama2-13b-chat
	Meta-Llama2-70b-chat
	"""
	def __new__(cls, **data):  # type: ignore
		"""Initialize the OpenAI object."""
		model_name = data.get("model_name", "")
		if model_name.startswith("gpt-3.5-turbo") or model_name.startswith("gpt-4"):
			warnings.warn(
				"You are trying to use a chat model. This way of initializing it is "
				"no longer supported. Instead, please use: "
				"`from langchain.chat_models import ChatOpenAI`"
			)
			return ChatLlama2(**data)
		return super().__new__(cls)

	def _generate(self, prompts, stop=None) -> LLMResult:
		return super()._generate(prompts, stop)



class ChatLlama2:
	pass
