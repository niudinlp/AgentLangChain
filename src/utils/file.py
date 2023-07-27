# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/26
Description   :
"""
import yaml
import pandas as pd
import time
import requests
from pathlib import Path
from src.commons.logger import logger


def read_yaml_file(fname):
	fname = ensure_path(fname)
	if fname.suffix not in ('.yml', '.ymal'):
		raise TypeError(f"specify file suffix ({fname.suffix}) error: .yaml, .yml")
	with fname.open('r', encoding='utf-8') as fid:
		contents = yaml.load(fid.read(), Loader=yaml.FullLoader)
	return contents

def write_yaml_file(fname, data):
	fname = ensure_path(fname)
	with fname.open("w", encoding="utf-8") as fid:
		yaml.dump(data, fid)

def ensure_path(path):
	"""Ensure string is converted to a Path.

	path (Any): Anything. If string, it's converted to Path.
	RETURNS: Path or original argument.
	"""
	if isinstance(path, str):
		return Path(path)
	else:
		return path

def load_dataset_from_excel(data_file):
	data_file = ensure_path(data_file)
	if data_file.suffix not in (".xls", ".xlsx"):
		raise TypeError("data file type error. Specify type: .xls, .xlsx")
	if not data_file.exists():
		return None
	#
	DISPLAY_ALL_TEXT = False
	pd.set_option("display.max_colwidth", 0 if DISPLAY_ALL_TEXT else 50)

	try:
		return pd.read_excel(data_file, index_col=None)
	except pd.errors.EmptyDataError as exc:
		return None


def load_dataset_from_csv(data_file):
	data_file = ensure_path(data_file)
	if data_file.suffix != ".csv":
		raise TypeError("data file type error. Specify type: .csv")
	if not data_file.exists():
		return None
	#
	DISPLAY_ALL_TEXT = False
	pd.set_option("display.max_colwidth", 0 if DISPLAY_ALL_TEXT else 50)

	try:
		return pd.read_csv(data_file, index_col=None)
	except pd.errors.EmptyDataError as exc:
		return None


def diff_time(start, end, point=2, unit="ms", sep="") -> str:
	diff = end - start
	diff = diff * 1000 if unit == "ms" else diff
	return f"{ round(diff, point) }{ sep }{ unit }"


def request_url(url: str, body: dict, method: str = "post", headers: dict = None, timeout: int = 1,
                trace_id: str = None) -> dict:
	"""
	request method for inner API
	"""
	# 请求方法只有 post 和 get
	method = method.lower()
	if method not in ("post", "get", "delete"):
		return {}
	# body 字段名称
	body_name = "json" if method == "post" else "params"

	func = getattr(requests, method)
	params = {body_name: body, "timeout": timeout}
	if not headers:
		headers = dict()
	trace_id = headers.get('trace_id', None) if trace_id is None else trace_id
	params.update(headers=headers)

	st = time.time()
	try:
		response = func(url, **params)
		# logger.info(f"[{trace_id}] request [{method} {url}] response text: {response.text}")
	except Exception as e:
		response = None
		logger.info(f"[{trace_id}] request [{method} {url}] error: {e}")
	et = time.time()
	logger.info(f"[{trace_id}] request [{method} {url}] cost: {diff_time(st, et)}, params: {params}")

	return response.json() if response else {}


def gen_trace_id() -> str:
	return str(int(time.time() * 1000000))

