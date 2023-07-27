# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2022/03/18
Description   : http response
"""
import traceback
from sanic import response
from src.commons.symbols import ResponseCode
from src.commons.logger import logger


def response_json(code=ResponseCode.OK, message="", status=200, **data):
    return response.json({
        "success": code.value,
        "err_msg": message,
        **data
    }, status, headers={"Access-Control-Allow-Origin": "*"})


def handle_exception(request, e):
	traceback.print_exc()

	code = ResponseCode.FAIL
	message = repr(e)
	status = 500
	trace_id = request.headers.get("trace_id", None)

	logger.error(f"[{trace_id}] service error: {traceback.format_exc()}")
	data = {}
	if request.app.config.get("DEBUG"):
		data["exception"] = traceback.format_exc()

	return response_json(code, message, status, **data)
