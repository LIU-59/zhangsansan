"""
print("hello world!")  #字符串
print(2333) #整数
print(2.33) #小数
print(True) #布尔值 Ture False
print(())  #元组
print([]) #数组
print({}) #字典
锄禾日当午
汗滴禾下土

print("hah",233,66)
print("哈哈"+"嘻嘻") #字符串的拼接
print("哈哈哈"*100)
print(((1+2)*100-9.9)/2)
print(2>3)

#变量
#赋值
a = "张三"  # 把张三的值赋值给了名字叫a这个变量
print(a)
"""
print(2333) #整数
print(2.33) #小数
print(True) #布尔值 Ture False
print(())  #元组
print([]) #数组
print({}) #字典

# #数据格式的装换
# c = type(2333)
# print(c)
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
 
# a = str ("2333")
# print(type(a))

a = 'adbjhagwcdevajhdbhjvaghvwdc  hjacve'
print(len(a))
"""
练习:通过代码获取两端不同的内容，并且计算他们长度的和。
"""
# a = input("请输入：")
# b = input("请输入：")
# print("input获取内容：",len(a+b))
a = input("请输入：")
b = input("请输入：")
print("两端字符串的长度：",len(a)+len(b))