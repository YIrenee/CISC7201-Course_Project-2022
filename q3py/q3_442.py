import pandas as pd
import random
import os

def q3_442(set):
    goal_h = ['id','name','position','overall','nation','list_positon']
    glmax = 0 # 初始化
    dfs = pd.read_csv(set)
    c_l = []
    for c in [0,3,4,5,23]:
        c_l.append(list(dfs)[c])
    # print(c_l)
    # 阵型 4-4-2['GK', 'RB', 'CB', 'CB', 'LB', 'RM', 'CM', 'CM', 'LM', 'ST', 'ST']
    g = ['GK', 'RB', 'CB', 'CB', 'LB', 'RM', 'CM', 'CM', 'LM', 'ST', 'ST']
    for r in range(605000):
        # 随机重排g442
        random.shuffle(g)
        # print(g)
        # 筛选某位置人选
        gl = pd.DataFrame(columns=c_l) # 新建df新表
        for value in g:
            j = 0
            s_v = dfs[dfs['player_positions'].str.contains(value)] # 筛选该位置所有球员
            if s_v.empty: # 若该位置空缺无人选
                gl = gl.append([0,0,0,dfs['overall'].mean(),0]) #overall取全表均值
                continue
            else:
                # candidate
                # overall降序排列
                s_v = s_v.sort_values(by='overall',ascending=False)  # by指定列,ascending表示是否升
                for i in range(0,2): # 允许的j范围（即可能选择排第j的候选）
                    if gl.empty == False and s_v.iloc[j][0] in gl['sofifa_id'].values: 
                    # 若非空且重复
                        j += 1
                    elif gl.empty == True: # 排除空值情况避免报错
                        continue
                    else:
                        break
                # 储存
                gl = gl.append(s_v.iloc[[j],[0,3,4,5,23]]) # 'id','name','position','overall','nation'
        colsum = gl['overall'].sum() # 求overall列total
        # colaver = gl['overall'].mean() # 求overall列average
        gl['list_positon'] = g # 本队列中担任位置
        if glmax < colsum: # 取大
        # if glmax < colaver: # 取大
            glmax = colsum
            # glmax = colaver
            gl.columns = goal_h # 重置列名 str(round(colaver,2))
            gl.to_csv('goal442.csv',encoding='UTF-8',index=False) # 覆盖存储
    os.rename('goal442.csv', 'goal442_'+str(round(colsum,2))+'.csv') # 将分数加到文件名里
    # os.rename('goal442.csv', 'goal442_'+str(round(colaver,2))+'.csv') # 将分数加到文件名里
    # return colaver
    return colsum
set = "slist.csv"
total = q3_442(set)



# 阵型 4-2-3-1['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CDM', 'CAM', 'CAM', 'CAM', 'ST']
