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

	def __call__(self, data, primary_key):
		"""
		convert structured data into sequential data
		"""
		if isinstance(data, dict):	# ignore nested dict case
			doc = self.convert_dict(data, primary_key) + self.line_sep
		elif isinstance(data, pd.DataFrame):
			doc = self.convert_dataframe(data, primary_key) + self.doc_sep
		else:
			raise RuntimeError(f"specify supported type: dict, DataFrame")

		return doc

	def convert_dict(self, data, primary_key):
		"""
		convert dictionary into sequence
		"""
		ss = []
		primary_value = data[primary_key]
		for key, val in data.items():
			# ss.append(f"{key}是{val}")
			ss.append(f"{key}: {val}")
		# return f"以下是{primary_value}的信息：" + ", ".join(ss)
		return ", ".join(ss)

	def convert_dataframe(self, data, primary_key):
		doc = ""
		for row in data.iterrows():
			ss = []
			primary_value = row[1][primary_key]
			for label, val in zip(row[1].index, row[1].values):
				if pd.isna(val):
					print(">>>> Ignore NaN value:", label, val)
					continue
				# ss.append(f"{label}是{val}")
				ss.append(f"{label}: {val}")
			# doc += f"以下是{primary_value}的信息：" + ", ".join(ss) + self.line_sep
			doc += ", ".join(ss) + self.line_sep
		return doc
