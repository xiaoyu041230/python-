#定义一个函数，用于检测一行字符串中括号
def check_brackets(string):
    #定义一个列表stack,存放"("的序号，实现"栈"的功能
    stack = []
    #定义一个列表result,存放检测结果，初始状态，里面存入与检测数据同长度的空格符号
    result = [' '] * len(string)

    #循环，逐字符查看
    for i, char in enumerate(string):
        #如果字符是"(",就把这个字符的序号加入stack列表中
        if char == '(':                 
            stack.append(i)
        #如果字符是")",且stack非空，就删除stack中一个元素（即删除最后一个"("的序号）；
        elif char == ')':               
            if stack:               
                stack.pop()
            #如果字符是")",且stack非，就修改result列表中第i个元素的值为"?"；
            else:                   
                result[i] = '?'

    #此时，stack若非空，则里面存放的都是"("的序号，修改result相应序号的元素值为"x"
    for index in stack:             
        result[index] = 'x'

    #将result中所有元素组合成一个字符串，并返回
    return ''.join(result)      


test_str=input("请输入一行字符串:")
print(test_str)
print(check_brackets(test_str))
