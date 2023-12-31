# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/26
Description   : Llama2 interface
"""
import warnings
import requests
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from src.commons.logger import logger


class Llama2(LLM):
	"""LLama2 service.

	Example:
		.. code-block:: python

			import llama2
			endpoint_url = (
				"http://127.0.0.1:8000"
			)
			llm = Llama2(
				endpoint_url=endpoint_url
			)
	"""

	endpoint_url: str = "http://127.0.0.1:8000/"
	"""Endpoint URL to use."""
	model_kwargs = None
	"""Key word arguments to pass to the model."""
	max_token: int = 20000
	"""Max token allowed to pass to the model."""
	temperature: float = 0.1
	"""LLM model temperature from 0 to 10."""
	history = []
	"""History of the conversation"""
	top_p: float = 0.7
	"""Top P for nucleus sampling from 0 to 1"""
	with_history: bool = False
	"""Whether to use history or not"""

	@property
	def _llm_type(self):
		return "llama2"

	@property
	def _identifying_params(self):
		"""Get the identifying parameters."""
		_model_kwargs = self.model_kwargs or {}
		return {
			**{"endpoint_url": self.endpoint_url},
			**{"model_kwargs": _model_kwargs},
		}

	def _call(self, prompt, stop=None, run_manager=None, **kwargs):
		"""Call out to a ChatGLM LLM inference endpoint.

		Args:
			prompt: The prompt to pass into the model.
			stop: Optional list of stop words to use when generating.

		Returns:
			The string generated by the model.

		Example:
			.. code-block:: python

				response = chatglm_llm("Who are you?")
		"""
		_model_kwargs = self.model_kwargs or {}

		# HTTP headers for authorization
		headers = {"Content-Type": "application/json"}

		payload = {
			"prompt": prompt,
			"temperature": self.temperature,
			"history": self.history,
			"max_length": self.max_token,
			"top_p": self.top_p,
		}
		payload.update(_model_kwargs)
		payload.update(kwargs)

		logger.debug(f"payload: {payload}")

		# call api
		try:
			response = requests.post(self.endpoint_url, headers=headers, json=payload)
		except requests.exceptions.RequestException as e:
			raise ValueError(f"Error raised by inference endpoint: {e}")

		logger.debug(f"response: {response}")

		if response.status_code != 200:
			raise ValueError(f"Failed with response: {response}")

		try:
			parsed_response = response.json()

			# Check if response content does exists
			if isinstance(parsed_response, dict):
				content_keys = "response"
				if content_keys in parsed_response:
					text = parsed_response[content_keys]
				else:
					raise ValueError(f"No content in response : {parsed_response}")
			else:
				raise ValueError(f"Unexpected response type: {parsed_response}")

		except requests.exceptions.JSONDecodeError as e:
			raise ValueError(
				f"Error raised during decoding response from inference endpoint: {e}."
				f"\nResponse: {response.text}"
			)

		if stop is not None:
			text = enforce_stop_tokens(text, stop)
		if self.with_history:
			self.history = self.history + [[None, parsed_response["response"]]]
		return text
