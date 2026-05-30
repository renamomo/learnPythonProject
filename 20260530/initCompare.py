import pandas as pd
import json
# readName = pd.read_excel(
#     '【排名】.xlsx', 
#     sheet_name='Sheet1',
#     header=[0],
# )                                    # 生成pandas的readName
# newList=readName.values.tolist()     # 生成Python格式的newList

# with open('newList.json', 'w', encoding='utf-8') as f:      # utf-8表示支持中文，w=写，f=文件
#     json.dump(newList, f, ensure_ascii=False, indent=4)     # ensure_ascii=False固定写法，indent=4代表前缩进距离
#     #把newList导入或写入json生成新的文件

# readNameCompare = pd.read_excel(
#     '上海高校排名待确认.xlsx', 
#     sheet_name='Sheet1',
#     header=[0],
# )                                    
# newListCompare=readNameCompare.values.tolist()     

# with open('newListCompare.json', 'w', encoding='utf-8') as f:      
#     json.dump(newListCompare, f, ensure_ascii=False, indent=4)     

newList=[
    [
        1,
        "麻省理工学院",
        "QS 1",
        "美国",
        NaN
    ],
    [
        2,
        "帝国理工学院",
        "QS 2",
        "英国",
        NaN
    ],
    [
        3,
        "斯坦福大学",
        "QS 3",
        "美国",
        NaN
    ],
    [
        4,
        "牛津大学",
        "QS 4",
        "英国",
        NaN
    ],
]

newListCompare=[
    [
        2,
        "帝国理工学院",
        "",
        "",
    ],
    [
        3,
        "斯坦福大学",
        "",
        "",
    ],
]

