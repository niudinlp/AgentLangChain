# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/27
Description   : LLM server
"""
from transformers import pipeline

class GPT2:
	"""
	GPT2 Server
	"""
	def __init__(self, model_path) -> None:
		self.generator = pipeline('text-generation', model=model_path)


	def generate(self, prompt):
		"""
		use contrastive search strategy
		"""
		out = self.generator(
				prompt,
				max_new_tokens=50,
				penalty_alpha=0.6,
				top_k=4,
				num_return_sequences=1)
		return out

