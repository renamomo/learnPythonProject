# my_str='应收账款的期末余额为2000元'
# print(my_str[:4]+my_str[-6:])

# A='哈'
# B='我'
# front=my_str[:5]
# aMany=A*4
# middle=my_str[5:9]
# bMany=B*4
# end=my_str[-6:]
# print(front+aMany+middle+bMany+end)


# init=[1,2,3,3,4]
# 删除多余的一个3
# 在队尾增加5,6
# 在1和2中间插入1.5，在5和6中间插入5.5
# 修改5.5为6.6
# 算出数组中有多少个值
# 每一步请打印当前的init
# print(init)
# del init[2]
# print(init)
# init.append(5)
# init.append(6)
# print(init)
# init.insert(-1,5.5)
# print(init)
# init.insert(1,1.5)
# print(init)
# init[-2]=6.6
# print(init)
# print(len(init))


# test=[
#     [1,2,3,4,5],
#     ['我','你','他','他们','她','她'],
#     [True,True,True,False,False,False],
# ]

# （1）请打印出一维列表的长度
# （2）请打印出一维列表中子列表的长度
# （3）请把他们替换成我们
# （3）请在5后面加6
# （4）请删除最后的布尔型列表
# （5）请在2后面插入20
# （6）打印出最后的结果


# print(len(test))
# print(len(test[0]))
# test[1][3]='我们'
# print(test[1])
# test[0].append(6)
# print(test[0])
# del test[2]
# print(test)
# test[0].insert(1,20)
# print(test[0])

# 一个班主任的基本信息，student是列表，列表里面随机写您家孩子和另外两个同学的信息

deTeacher=[{
    'identity':'5',
    'personName':'青青',
    'age':35,
    'gender':'female',
    'studentNumber':3,
    'student':[{
        'identity':'1',
        'personName':'DE',
        'age':17,
        'gender':'male',
    },{
        'identity':'2',
        'personName':'Mason',
        'age':17,
        'gender':'male',
    },{
        'identity':'3',
        'personName':'May',
        'age':18,
        'gender':'female',
    }],
},{
    'identity':'6',
    'personName':'青青',
    'age':35,
    'gender':'female',
    'studentNumber':1,
    'student':[{
        'identity':'4',
        'personName':'DE1',
        'age':17,
        'gender':'male',
    }],
}]
deTeacher[1]['student'][0]['age']=deTeacher[1]['student'][0]['age']+1
print(deTeacher[1])

# 请把所有的id用本页替换的方式替换成 identity
# 请把所有的name用全局替换的方式替换成 personName
# 请帮我打印出'DE1'，'female'

# print(deTeacher[1]['student'][0]['personName'])
# print(deTeacher[0]['student'][2]['gender'])
# print(deTeacher[0]['student'][1])
# print(deTeacher[1].keys())
# print(deTeacher[0]['student'][1].values())