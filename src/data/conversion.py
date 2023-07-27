# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/26
Description   : format conversion
"""
import pandas as pd


class Converter:
	"""
	convert structured data (SQL, dict, excel...) into sequence data
	"""
	line_sep = "\n"
	doc_sep = "<|endoftext|>"

	def __init__(self) -> None:
		"""
		:param sep: separator, line separator "\n", doc separator "<|endoftext|>"
		"""
		pass

	def __call__(self, data):
		"""
		convert structured data into sequential data
		"""
		if isinstance(data, dict):	# ignore nested dict case
			doc = self.convert_dict(data) + self.line_sep
		elif isinstance(data, pd.DataFrame):
			doc = self.convert_dataframe(data) + self.doc_sep
		else:
			raise RuntimeError(f"specify supported type: dict, DataFrame")

		return doc

	def convert_dict(self, data):
		"""
		convert dictionary into sequence
		"""
		ss = []
		for key, val in data.items():
			ss.append(f"{key}: {val}")
		return ", ".join(ss)

	def convert_dataframe(self, data):
		doc = ""
		for row in data.iterrows():
			ss = []
			for label, val in zip(row[1].index, row[1].values):
				if pd.isna(val):
					print(">>>> Ignore NaN value:", label, val)
					continue
				ss.append(f"{label}: {val}")
			doc += ", ".join(ss) + self.line_sep
		return doc
