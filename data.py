# 重读q1文件
# 获取selected_nation-name_birthdate_height_list(snblist)

# Re-read the q1 file
# to obtain selected_nation-name_birthdate_height_list(snblist)
import pandas as pd
import os

df = pd.read_csv('players_22.csv')
# print(df.iloc[0]) 

snblist = []
# 读入数据
path = "squad list(new)" # 文件夹目录
files= os.listdir(path) # 得到文件夹下的所有文件名称
# print(files)
for file in files: # 遍历文件夹
    position = path+'\/'+ file # 构造文件路径
    b = []; i = 0; h = []
    with open(position, encoding='UTF-8') as fr:
        for line in fr.read().splitlines():
            i += 1
            if i == 2: # or i == 5: # 读取国家
                b.append(line)
                h.append(line)
            elif i >= 9 and i % 9 == 4: # in [0,2,3]: # 读取出生日期
                b.append(line)
            elif i >= 9 and i % 9 == 5: # in [0,2,3]: # 读取身高
            # 准确度不够，加筛身高
                h.append(line)
            else:
                continue
    snblist.append(b)
    snblist.append(h)
# print(slist)

# name=['country','two','three']
record_s=pd.DataFrame(columns=None,data=snblist)#数据有27列，列名省略，其中第0列为国家
record_s.to_csv('snblist.csv',encoding='UTF-8')
