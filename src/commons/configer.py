# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2022/03/18
Description   : 读取系统配置
"""
import os
from src.utils.file import read_yaml_file
from src.commons.constant import CONFIG_PATH

config_file = os.path.join(CONFIG_PATH, 'config.yaml')
base_config_set = read_yaml_file(config_file)
env_name = os.getenv("MY_SL_ENV", "local")
base_config = base_config_set[env_name]
