# 以国家+出生日期作为匹配条件进行筛选
# 有概率出现同一国家同一出生日期的球员
# 因此将身高添加为筛选条件进行清洗。

# The country-date of birth was selected as the matching condition.
# However, in the database,there is a probability that
# there are players with the same date of birth in the same country,
# so we added the height data together as a screening condition for cleaning.
import pandas as pd
import re
from data import df,snblist

# print(type(''.join(re.findall(r'[0-9]', df.iloc[255][10]))))

# main
m,n = df.shape
g=0;na=0;p=0
for group in range(0,len(snblist)):
    df1 = pd.DataFrame(columns = list(df))
    g += 1
    if group >= 2 and group % 2 == 1: # 跳过身高行
        continue
    elif group == 1: # 跳过第一个身高行（预防报错）
        continue
    else:
        pin = 0
        for ply in snblist[group][1:]:
            pin += 1
            if pd.isna(ply) or len(ply) == 0:
            # 排除空值
                na += 1
                continue
            else:
                p += 1
                for i in range(0,m): 
                    if  df.iloc[i][23] in snblist[group][0]: # 筛国家 # 其中美国、加拿大、韩国数据未对齐有问题
                        df_date = ''.join(re.findall(r'[1-9]', df.iloc[i][10]))
                        snblist_date = ''.join(re.findall(r'[1-9]', ply[6:]+ply[3:5]+ply[0:2]))
                        # print(df_date,snblist_date)
                        if int(df_date) == int(snblist_date): # or df.iloc[i][23] in ['UnitedStates','Canada','KoreaRepublicDPR']:
                            # 筛出生日期
                            if df.iloc[i][11] == int(snblist[group+1][pin]) or df.iloc[i][11] == 0:
                            # 筛身高 # 数据问题，个别选手的身高是零值,零值skip
                                # 储存该选手信息
                                df1 = df1.append(df.iloc[i:i+1])         
                df1.to_csv('snb'+'\\''selected'+''.join(re.findall(r'[A-Za-z]', snblist[group][0]))+'.csv',encoding='UTF-8',index=False)
print(g,p,na,pin)