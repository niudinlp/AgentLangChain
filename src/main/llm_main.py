# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/27
Description   : LLM server
"""
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class GPT2:
	"""
	GPT2 Server
	"""
	def __init__(self, model_path) -> None:
		self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
		self.model = GPT2LMHeadModel.from_pretrained(model_path)

	def generate(self, prompt):
		pass
	
