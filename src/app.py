# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2022/11/08
Description   :
"""
import time
from sanic import Sanic, response
from sanic.config import Config

from src.blueprints.bp_model import sl_model
from src.commons.logger import logger
from src.commons.configer import base_config as config
from src.utils.response import handle_exception
from src.utils.file import diff_time
from src.main.llm_main import GPT2

# app
app = Sanic(name='Portrait', config=Config(defaults=config, env_prefix='MY_SL_'))

# 注册exception
app.error_handler.add(Exception, handle_exception)

# 注册蓝图
app.blueprint(sl_model)

# @app.route("/", methods=["GET", "HEAD"])
# async def health(request):
# 	return response.text('ok')


@app.listener("before_server_start")
async def server_init(app, loop):
	"""
	服务启动之前 初始化资源
	"""
	app.ctx.server = Portrait(config)


@app.middleware("request")
async def request_begin(request):
	"""
	请求开始，执行路由函数之前的操作
	"""
	request.headers["start_time"] = str(time.time())


@app.middleware("response")
async def request_end(request, response):
	"""
	请求结束，执行路由函数之后的操作
	"""
	trace_id = request.headers.get('trace_id', None)
	start_time = request.headers.pop("start_time", None)
	spend_time = -1 if start_time is None else diff_time(float(start_time), time.time())
	logger.info(f"[{ trace_id }] time cost: { spend_time }")


if __name__ == '__main__':
	app.run(
		host=config['host'],
		port=config['port'],
		debug=config['debug'],
		workers=config['workers']
	)
