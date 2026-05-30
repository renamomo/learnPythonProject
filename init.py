# age='18'
# age1='16'
# name1='rena'

# a=18
# b=16
# d=0
# e=-1


# age='19'
# a=19
# print(age)
# print(a)

# age=15
# a=5
# print(age)
# print(a)

# print(a>b)
# print(b>a)

# my_str='应收账款的期末余额为2000元'
# print(my_str[:4])
# print(my_str[::-1])
# print(my_str)

# print(my_str[5:9:])
# print(my_str[5:9:1])
# print(my_str[5:9:2])
# print(my_str[5:9:3])
# print(my_str[5:9:4])

# print(my_str[6:10])
# print(my_str[-5:-2])

# myList=[1,2,3,4,2,3,5,6,7,1,2,2,2]
# myListLength=len(myList)
# print(myListLength)

# print(myList.count(2))


# myList=[1,2,3,4]
# myList[-1]=123
# print(myList)

# mylist=[100,200,300,400,200,500,100,300]
# mylistlen1=len(mylist)
# print(mylistlen1)

# mylist[3]=222
# print(mylist)

# print(mylist.count(200))


# mylist=[100,200,300,400,200,500,100,300]
# mylist.append(800)
# print(mylist)
# mylist.append(801)
# mylist.append(801)
# mylist.append(801)
# mylist.append(803)
# print(mylist)

# mylist=[100,200,300,400,500]
# mylist.insert(3,60)
# mylist.insert(2,50)

# print(mylist)
# mylist.append(1)
# mylist.append(2)
# print(mylist)

# mylist=[100,200,300,400,500]
# mylist.append(222)
# mylist.append(100)
# mylist.append(222)
# mylist.insert(4,200)
# mylist.insert(1,222)
# print(mylist)

# print(mylist.count(222))

# mylist=[100,200,300,400,500]
# del mylist[2]
# print(mylist)


# mylistRow=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],  
#     [16,17,18,19,20],
#     [21,22,23,24,25],
# ]

# 在13和14中间插一个13.5

# print(mylistRow[2])
# mylistRow[2].insert(3,13.5)
# print(mylistRow)

# mylistRow[3][2]=88
# print(mylistRow)
# print(len(mylistRow[2]))

# print(mylistRow)

# mylistRow.append([26,27,28,28,30])

# print(mylistRow)

# del mylistRow[2]

# print(mylistRow)


# mylist=[
#     [1,6,11,16,21],
#     [2,7,12,17,22],
#     [3,8,13,18,23],
#     [4,9,14,19,24],
#     [5,10,15,20,25],
# ]
# print(mylist)


# myDictionary={
#     'abandon':{
#         '笔画':7,
#         '词组':'abandon me',
#         '词头':'a'
#     },
#     'personName':'名字',
#     '数字':12,
#     'bool':False,
#     'array':[{
#         'aa':'aa1',
#         'bb':'bb1'
#     },2,3,4,5,6]
# }

# family=[{
#     'personName':'grandpa',
#     'age':90,
#     'gender':'male',
#     'children':[{
#         'personName':'大儿子',
#         'age':50,
#         'gender':'male',
#         'children':[{
#             'personName':'大孙子',
#             'age':20,
#             'gender':'male',
#             'childern':[]
#         }]
#     },{
#         'personName':'小女儿',
#         'age':45,
#         'gender':'female',
#         'children':[]
#     }]
# }]

# familyRena=[{
#     'personName':'rena',
#     'age':43,
#     'gender':'female',
#     'marry':True,
#     'children':[{
#         'personName':'mason',
#         'age':17,
#         'gender':'male',
#         'marry':False,
#     },{
#         'cat':'baby',
#         'age':3,
#         'gender':'female',
#         'marry':False,
#     }]
# }]

# familyZZ=[{
#     'personName':'ZZ',
#     'age':44,
#     'gender':'male',
#     'pet':[{
#         'catName':'小宝',
#         'age':2.5,
#         'gender':'male',        
#     },{
#         'catName':'xuan',
#         'age':2.5,
#         'gender':'male',        
#     },{
#         'catName':'baby',
#         'age':3,
#         'gender':'famale',        
#     }],
# }]

# familyZZ[0]['pet'][0]['married']={}
# familyZZ[0]['pet'][0]['married']['marri']={}
# familyZZ[0]['pet'][0]['married']['marri']['abc']=111

# del familyZZ[0]['pet'][1]['gender']
# print(familyZZ)

# print(familyZZ)

# simpleDictionary={
#     'catName':'小宝',
#     'age':2.5,
#     'gender':'male',        
# }
# print(simpleDictionary.keys())
# print(simpleDictionary.values())
# print(simpleDictionary['catName'])
# print(familyZZ[0]['pet'][1]['catName'])

# print(familyZZ[0]['pet'][2]['age'])



# company=[{
#     'companyName':'DHR',
#     'companyAge':16,
#     'department':[{
#         'departName':'Admin',
#         'person':5,
#         'manager':{
#             'name':'shao',
#             'age':50,
#             'gender':'male',
#             'school':'上海交通大学',
#         },
#     },{
#         'departName':'outsourcing',
#         'person':100,
#         'leader':5,
#         'manager':{
#             'name':'zhang',
#             'age':48,
#             'gender':'famale',
#             'school':'上海大学',
#         },
#     },{
#         'depatName':'recruit',
#         'person':30,
#         'leader':3,
#         'manager':{
#             'name':'feng',
#             'age':42,
#             'gender':'male',
#             'school':'上海师范大学',
#         },
#     },{
#         'depatName':'operation',
#         'person':20,
#         'leader':1,
#         'manager':{
#             'name':'hu',
#             'age':46,
#             'gender':'famale',
#             'school':'复旦大学',
#         },
#     }]
# }]
# print(company)

# adminAll=company[0]['department'][0]['person']+company[0]['department'][0]['manager']
# print(adminAll)

# outsourcingAll=company[0]['department'][1]['person']+company[0]['department'][1]['manager']+company[0]['department'][1]['leader']
# print(outsourcingAll)

# difference1=outsourcingAll-adminAll
# print(difference1)

# recruitment=company[0]['department'][2]['leader']*3
# print(recruitment)

# bonus=280000
# operationAll=company[0]['department'][3]['person']+company[0]['department'][3]['manager']+company[0]['department'][3]['leader']
# operationBonus=bonus/operationAll
# print(operationBonus)

# operationBonus=bonus//operationAll
# print(operationBonus)

# operationBonus=bonus%operationAll
# print(operationBonus)

# outsourcingRecruitment=company[0]['department'][1]['leader']**company[0]['department'][2]['leader']
# print(outsourcingRecruitment)

# print(company[0]['department'][1]['leader']==company[0]['department'][2]['leader'])
# print(company[0]['department'][1]['leader']!=company[0]['department'][2]['leader'])

# recruitAll=company[0]['department'][2]['person']+company[0]['department'][2]['manager']+company[0]['department'][2]['leader']
# operationAll=company[0]['department'][3]['person']+company[0]['department'][3]['manager']+company[0]['department'][3]['leader']
# print(recruitAll>operationAll)
# print(recruitAll<operationAll)

# print(company[0]['department'][0]['person']>=company[0]['department'][1]['leader'])
# print(company[0]['department'][0]['person']<=company[0]['department'][1]['leader'])

# print(company[0]['department'][1]['manager']['age']>50 and company[0]['department'][1]['manager']['gender']=='famale')
# zhang=company[0]['department'][1]['manager']
# print(zhang['age']>50 and zhang['gender']=='famale')

# school=['上海交通大学','湖南师范大学','复旦大学','清华大学']
# print('清华大学' in school)

# print((company[0]['department'][0]['manager']['age']>45 or company[0]['department'][0]['person']>=40) and (not company[0]['department'][0]['manager']['school'] in school))
# print((company[0]['department'][1]['manager']['age']>45 or company[0]['department'][1]['person']>=40) and (not company[0]['department'][1]['manager']['school'] in school))
# print((company[0]['department'][2]['manager']['age']>45 or company[0]['department'][2]['person']>=40) and (not company[0]['department'][2]['manager']['school'] in school))
# print((company[0]['department'][3]['manager']['age']>45 or company[0]['department'][3]['person']>=40) and (not company[0]['department'][3]['manager']['school'] in school))


# a=3
# b=4
# print(a)
# a **=b
# print(a)
# a=a**b
# print(a)

# a=a+b
# a+=b
# print(a)

# a=10
# b='我是结果'

# if a<=9:
#     print('小于等于9')
#     b=b+'小于等于9'
# else:
#     print('大于9')
#     b=b+'大于9'
# print(b)

# if ((company[0]['department'][0]['manager']['age']>45 or company[0]['department'][0]['person']>=40) and company[0]['department'][0]['manager']['school'] in school):
#     print('升职备选')
# else:
#     print('不列入升职备选')

# a=20
# if 90<=a:
#     print('老年')
# elif 45<=a and a<90:
#     print('中年')
# elif 20<=a and a<45:
#     print('青年')
# else:
#     print('少年')

# if 90<=a:
#     print('老年')
# elif 45<=a and a<90:
#     print('中年')
# elif 20<=a and a<45:
#     print('青年')
# elif a<20:
#     print('少年')


# 50 高
# 20 经理
# 10 组长
# 5  小

# person=company[0]['department'][2]['person']
# if person>50:
#     print('高级经理')
# elif 20<=person and person<50:
#     print('经理')
# elif 10<=person and person<20:
#     print('组长')
# elif 5<=person and person<10:
#     print('小组长')
# else:
#     print('员工')


# onePerson={
#     'name':'张三',
#     'college':'上海交通大学',
#     'middleSchool':'圆南中学',
# }

# college985=['上海交通大学','复旦大学','清华大学']
# college211=['上海大学','湖南师范大学','上海海事大学']
# collegeNotGood=['上海大学','湖南师范大学','上海海事大学']
# middleSchoolTop=['上海中学','华育中学']
# middleSchool=['园南中学','上海第四中学','徐汇中学']



# if onePerson['college'] in college:
#     print('大学优秀')

# if onePerson['middleSchool'] in middleSchool:
#     print('中学优秀')

# if onePerson['college'] in college and onePerson['middleSchool'] in middleSchool:
#     print('C9+市重')
# elif onePerson['college'] in college and onePerson['middleSchool'] not in middleSchool:
#     print('C9+普通高中')
# elif onePerson['college'] not in college and onePerson['middleSchool'] in middleSchool:
#     print('普通大学+市重')
# else:
#     print('非清单')

# if onePerson['college'] in college:
#     print('985')
# elif onePerson['college'] in college2:
#     print('211')
# else:
#     print('普通高校')

# if onePerson['college'] in college985:
#     if onePerson['middleSchool'] in middleSchoolTop:
#         print('sale1')
#     elif onePerson['middleSchool'] in middleSchool:
#         print('sale2')
#     else:
#         print(f'{onePerson["name"]}的中学填写的是"{onePerson["middleSchool"]}"，未找到，人工核验')
# elif onePerson['college'] in college211:
#     if onePerson['middleSchool'] in middleSchoolTop:
#         print('sale3')
#     elif onePerson['middleSchool'] in middleSchool:
#         print('sale4')
#     else:
#         print('未找到，人工核验')
# else:
#     print('不录用')

# print(f'{familyRena[0]["personName"]}的年龄是{familyRena[0]["age"]}，性别是{familyRena[0]["gender"]}')
# print(f'{familyRena[0]["children"][0]["personName"]}的年龄是{familyRena[0]["children"][0]["age"]}，性别是{familyRena[0]["children"][0]["gender"]}')
# print(f'{familyRena[0]["children"][1]["cat"]}的年龄是{familyRena[0]["children"][1]["age"]}，性别是{familyRena[0]["children"][1]["gender"]}')


# a=121
# b=23123
# c=78
# 最后输出结果 23123>78>45

# if a>b>c:
#     print(f'{a}>{b}>{c}')
# elif a>c>b:
#     print(f'{a}>{c}>{b}')
# elif b>a>c:
#     print(f'{b}>{a}>{c}')
# elif b>c>a:
#     print(f'{b}>{c}>{a}')
# elif c>a>b:
#     print(f'{c}>{a}>{b}')
# elif c>b>a:
#     print(f'{c}>{b}>{a}')     
# else:
#     print('不成立')

# sort=[a,b,c]
# sort.sort()
# print(sort)
# sort.reverse()
# print(sort)


# a=12
# b=23123
# c=7112678

# max=a
# if b>max:
#     max=b
# if c>max:
#     max=c
# print(f'{max}')


# college985=['上海交通大学','复旦大学','清华大学','同济大学','东南大学','华中科学院大学','电子科技大学','北京大学','上海科技大学','浙江大学']

# print(college985[0])
# print(college985[1])
# print(college985[2])
# print(college985[3])
# print(college985[4])

# for item in college985:
#     print(item)
#     print(f'{item}是985')

# for item in college211:
#     print(f'{item}是211')



# total=[1.5,2,0.8,3,4,3.5,1.2,1.3]
# totalSalary=0
# for tal in total:
#     print(tal)
#     print(totalSalary)
#     totalSalary=totalSalary+tal
#     print(totalSalary)
#     print('#############################################')
# print(totalSalary)

# totalBonus=100
# total=[1.5,2,0.8,3,4,3.5,1.2,1.3]
# for tal in total:
#     print(tal)
#     print(totalBonus)
#     totalBonus=totalBonus-(tal*2)
#     print(totalBonus)
#     print('###')

total=[{
    'name':'张三',
    'salary':2.5,
    'age':26,
    'gender':'male',
    'children':[{
        'name':'小张',
        'salary':1.7,
        'age':22,
        'gender':'famale',
    },{
        'name':'小王',
        'salary':2.1,
        'age':26,
        'gender':'male'
    }]
},{
    'name':'李四',
    'salary':1.5,
    'age':23,
    'gender':'male',
    'children':[{
        'name':'小李',
        'salary':2,
        'age':26,
        'gender':'male'
    },{
        'name':'小吴',
        'salary':0.9,
        'age':20,
        'gender':'famale'
    },{'name':'小图',
        'salary':1.62,
        'age':24,
        'gender':'famale'
    }]
},{
    'name':'张丽',
    'salary':1.7,
    'age':24,
    'gender':'famale',
    'children':[{
        'name':'小潘',
        'salary':1,
        'age':21,
        'gender':'male'
    }]
}]

# totalSalary=0
# for item in total:
#     print(item)
#     print()item['salary']
#     totalSalary=totalSalary+item['salary']
# print(totalSalary)

# totalSalary=0
# for item in total:
#     print(item)
#     print(item['gender'])
#     if item['gender']=='male':
#         totalSalary=totalSalary+item['salary']
# print(totalSalary)

# totalSalary=0
# for item in total:
#     print(item)
#     print(item['salary'])
#     totalSalary=totalSalary+item['salary']
#     for itemChildren in item['children']:
#         print(itemChildren)
#         totalSalary=totalSalary+itemChildren['salary']
# print(totalSalary)

# for index,item in enumerate(total):  #先写员工名再写部门总额
#     print(f"第{index+1}部门经理的姓名是{item['name']},有{len(item['children'])}名员工，分别是：")
#     totalSalary=0
#     for indexChildren,itemChildren in enumerate(item['children']):
#         print(f"{itemChildren['name']}") #每个部门内员工姓名，简化版
#         # print(f"第{index}部门经理的第{indexChildren}名员工的姓名是{itemChildren['name']}") #每个部门内员工姓名
#         totalSalary=totalSalary+itemChildren['salary']
#     print(f"第{index+1}部门员工薪资总额为{totalSalary}")
        
        
# for index,item in enumerate(total):   #先写部门总额在写员工名
#     print(f"第{index+1}部门经理的姓名是{item['name']},有{len(item['children'])}名员工，分别是：")
#     totalSalary=0
#     totalAge=0
#     for indexChildren,itemChildren in enumerate(item['children']):
#         totalSalary=totalSalary+itemChildren['salary']
#         totalAge=totalAge+itemChildren['age']
#     print(f"第{index+1}部门员工薪资总额为{totalSalary}")   #部门员工薪资
#     print(f"第{index+1}部门员工平均年龄为{totalAge//len(item['children'])}")    #部门员工平均年龄
#     for indexChildren,itemChildren in enumerate(item['children']):
#         print(f"{itemChildren['name']}")    #每个部门内员工姓名，简化版



        
