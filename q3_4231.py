import pandas as pd
import numpy as np
import random
import os

def q3_4231(set):
    goal_h = ['id','name','position','overall','nation','list_positon']
    glmax = 0 # 初始化
    dfs = pd.read_csv(set)
    if dfs.empty: # 跳过空表
        return -1
    else:
        c_l = []
        for c in [0,3,4,5,23]:
            c_l.append(list(dfs)[c])
        # print(c_l) 
        pl_h = pd.DataFrame(columns=c_l, data=[[000000, 'placeholders', 'nan', dfs['overall'].mean(), dfs.iloc[0][23]]])
        # 不存在的占位选手，取全表overall均值作为分数
        # 阵型 4-2-3-1['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CDM', 'CAM', 'CAM', 'CAM', 'ST']
        g = ['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CDM', 'CAM', 'CAM', 'CAM', 'ST']
        for r in range(6050):
            # 随机重排g442
            random.shuffle(g)
            # 筛选某位置人选
            gl = pd.DataFrame(columns=c_l) # 新建df新表
            for value in g:
                j = 0
                s_v = dfs[dfs['player_positions'].str.contains(value)] # 筛选该位置所有球员
                # print(value)
                if s_v.empty: # 若该位置空缺无人选
                    # print(1)
                    gl = gl.append(pl_h, ignore_index=True)
                    #overall取全表均值
                else:
                    # candidate
                    # print(11)
                    # overall降序排列
                    s_v = s_v.sort_values(by='overall',ascending=False)  # by指定列,ascending表示是否升
                    l1,l2 = s_v.shape
                    for i in range(0,2): # 允许的j范围（即可能选择排第j的候选）
                        if gl.empty == False and s_v.iloc[j][0] in gl['sofifa_id'].values: 
                        # 若非空且重复
                            # print(111)
                            j += 1
                            if j >= l1 or i == 1:
                            # 假如该位置候选不够了 # 或允许的j范围到头了
                                # print(1111)
                                gl = gl.append(pl_h, ignore_index=True)
                                #overall取全表均值
                                break
                        else:
                            # 储存
                            # print(value)
                            # print(s_v.iloc[j][23])
                            gl = gl.append(s_v.iloc[[j],[0,3,4,5,23]]) # 'id','name','position','overall','nation'
                            break
            # colsum = gl['overall'].sum() # 求overall列total
            colaver = gl['overall'].mean() # 求overall列average
            # if glmax < colsum: # 取大-q3v
            if glmax < colaver: # 取大
                # glmax = colsum
                glmax = colaver
                gl['list_positon'] = g # 本队列中担任位置
                gl.columns = goal_h # 重置列名 str(round(colaver,2))
                gl.to_csv('goal4231.csv',encoding='UTF-8',index=False) # 覆盖存储
        # os.rename('goal4231.csv', 'goal4231_'+str(round(colsum,2))+'.csv') # 将分数加到文件名里
        return str(round(colaver,2))
        # return colsum

# set = "slist.csv"
# total = q3_4231(set)

