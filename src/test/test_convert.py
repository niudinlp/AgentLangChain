# -*- coding: utf-8 -*-
"""
Author        : Di Niu
CreatedDate   : 2023/07/26
Description   :
"""
import os, sys
sys.path.append(os.getcwd())

from src.utils.file import load_dataset_from_excel
from src.data.conversion import Converter

datafile = "/Users/diniu/Documents/python/agentlangchain/datafiles/private/2023-07-19--楼盘数据-长沙.xlsx"

df = load_dataset_from_excel(datafile)

converter = Converter()
doc = converter(df, "楼盘名称")

# save_file = "/Users/diniu/Documents/python/agentlangchain/datafiles/private/loupan_data.txt"
save_file = "/Users/diniu/Documents/python/agentlangchain/datafiles/private/loupan_data_v2.txt"
with open(save_file, "w", encoding="utf-8") as fid:
    fid.write(doc)

