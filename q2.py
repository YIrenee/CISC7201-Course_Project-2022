# 分别对每个文件求overall列均值
# Average the overall column for each file separately
import pandas as pd
import os
import csv

path = "snb" # 文件夹目录
files= os.listdir(path) # 得到文件夹下的所有文件名称
squad_r = dict()
na = 0
for file in files: # 遍历文件夹
    position = path+'\\'+ file # 构造文件路径
    dfa = pd.read_csv(position) # 读取数据
    col_aver = dfa['overall'].mean() # 求overall列均值
    # print(position)
    if dfa.empty:
        # 排除空文件
        na += 1
        continue
    else:
        ad = {dfa.iloc[1][23]: col_aver}
        # print(dfa.iloc[1][24])
        squad_r.update(ad) # 存入字典
# 按overall score对字典进行排序
s_rank = sorted(squad_r.items(),key=lambda x:x[1],reverse=True) # 从大到小降序排列
# print(type(s_rank))
# print(s_rank)
# print(na)
# print(squad_r)
# list存入csv
header = ['nation_name', 'average_overall_score']
record_s=pd.DataFrame(columns=header,data=s_rank)
record_s.to_csv('q2.csv',encoding='UTF-8',index=False)