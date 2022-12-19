import pandas as pd
import os
import csv
from q3_442 import q3_442
from q3_433 import q3_433
from q3_4231 import q3_4231

def get_keys(d, value): # 根据value取key
    for k,v in d.items():
        if v == value:
            return k 
     

# 读入数据
path = "snb" # 文件夹目录
files= os.listdir(path) # 得到文件夹下的所有文件名称
# print(files)
goal_h = ['id','name','position','overall','nation','list_positon']
goal = pd.DataFrame(columns=goal_h) # 新建df新表
for file in files: # 遍历文件夹
    position = path+'\\'+ file # 构造文件路径
    a_433 = q3_433(position)
    a_442 = q3_442(position)
    a_4231 = q3_4231(position)
    if a_433 == -1: # 目标是空表
        continue
    else:
        # 文件名变量
        q4_a433 = 'goal433.csv' 
        q4_a442 = 'goal442.csv'
        q4_a4231 = 'goal4231.csv'
        # 排序
        q4_set = {'a433':a_433,'a442':a_442,'a4231':a_4231}
        q4_sort = sorted([a_433,a_442,a_4231])
        set_list = set(q4_sort)
        if len(set_list) == 1: # 同分全保存
            nation = pd.read_csv(q4_a433).iloc[0][4]
            score = str(a_433)
            os.rename(q4_a433, 'q4'+'\\'+nation+'_'+score+'_433.csv')
            # 重命名
            os.rename(q4_a442, 'q4'+'\\'+nation+'_'+score+'_442.csv')
            # 重命名
            os.rename(q4_a4231, 'q4'+'\\'+nation+'_'+score+'_4231.csv')
            # 重命名
        elif len(set_list) < len(q4_sort): # 并列第一
            k1 = get_keys(q4_set,q4_sort[0])
            k2 = get_keys(q4_set,q4_sort[1])
            gl1 = pd.read_csv(eval('q4_' + k1))
            nation = gl1.iloc[0][4]
            score = str(q4_sort[0])
            gl1.to_csv('q4'+'\\'+nation+'_'+score+'_'+k1+'.csv',encoding='UTF-8',index=False)
            gl2 = pd.read_csv(eval('q4_' + k2))
            gl2.to_csv('q4'+'\\'+nation+'_'+score+'_'+k2+'.csv',encoding='UTF-8',index=False)
        else:
            k = get_keys(q4_set,q4_sort[0])
            goal = pd.read_csv(eval('q4_' + k))
            nation = goal.iloc[0][4]
            score = str(q4_sort[0])
            goal.to_csv('q4'+'\\'+nation+'_'+score+'_'+k+'.csv',encoding='UTF-8',index=False)