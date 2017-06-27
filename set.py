bak={'bad','bad','good','good','hu','hi'}
print(bak)            #显示结果会去重
if 'bad' in bak:
    print("yes")         #判断元素是否在集合
else:
    print("no")

if 'hui' in bak:        #判断元素是否在集合
    print("yes")
else:
    print("no")

a=set('abcdhuiiu')
b=set('abkgyo')
print(a)    # 打印集合a中包含元素
print(a-b)  #把a里元素在b里存在的元素去掉
print(a|b)  # 集合a或b中包含的所有元素
print(a&b)  # 集合a和b中都包含了的元素
print(a^b)  # 不同时包含于a和b的元素

