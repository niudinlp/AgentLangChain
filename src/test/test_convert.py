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

datafile = "/Users/diniu/Documents/python/langchainagent/datafiles/2023-07-19--楼盘数据-长沙.xlsx"

df = load_dataset_from_excel(datafile)

converter = Converter()
doc = converter(df)

save_file = "/Users/diniu/Documents/python/langchainagent/datafiles/loupan_data.txt"
with open(save_file, "w", encoding="utf-8") as fid:
    fid.write(doc)

