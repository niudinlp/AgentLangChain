# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2022/11/08
Description   :
"""
from sanic import Blueprint
from src.commons.logger import logger
from src.commons.symbols import ResponseCode
from src.utils.response import response_json

sl_model = Blueprint('sl_model', url_prefix="/model")		# portrait SL


@sl_model.route("/gpt2", methods=['POST'])
async def gpt2(request):
	"""
	GPT2 model request
	"""
	req_data = request.json
	trace_id = request.headers.get('TraceId', None)
	logger.info(f"===================================================>>>")
	logger.info(f"[{trace_id}] [\"/gpt2\"] request data: {req_data}")
	#
	server = request.app.ctx.server
	data, err_msg = server.run_portrait_analysis(trace_id, req_data)
	if err_msg is not None:
		logger.info(f"[{trace_id}] [\"/gpt2\"] service error: {err_msg}")
		return response_json(code=ResponseCode.FAIL, message=err_msg)
	#
	logger.info(f"[{trace_id}] [\"/gpt2\"] service ok! result: {data}")
	logger.info(f"<<<===================================================")
	return response_json(results=data)

