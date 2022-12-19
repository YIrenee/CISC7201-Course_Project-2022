# q3 所使用的数据是snb文件夹中的所有数据，因此创建一个总表会更加方便对数据进行处理
import re
import pandas as pd
import os
from data import df

slist = []
# 读入数据
path = "snb" # 文件夹目录
files= os.listdir(path) # 得到文件夹下的所有文件名称
dfs = pd.DataFrame(columns = list(df)) # 新建df新表
for file in files: # 遍历文件夹
    position = path+'\\'+ file # 构造文件路径
    f = pd.read_csv(position)
    dfs = dfs.append(f) # 读取并保存该csv文件内的全部内容到dataframe中
dfs.to_csv('slist''.csv',encoding='UTF-8',index=False) # 存储
