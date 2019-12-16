''''''
'''
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced

[{]}-->Unbalanced
'''
'''
#使用stack方法: 
遍历字符串，如果是左括弧，则append到stack；
如果是右括弧，则检查stack是否为空，若为空则为Unbalanced，或者检查pop出stack的字符是否为对应的左括弧，若不是，则为Unbalanced；
最后检查valid标志和stack是否为空
'''
def balanced_parentheses(str):
    valid = True
    stack = []

    for each in str:
        if ((each=='(') or (each=='[' ) or (each=='{')):
            stack.append(each)
        elif each==')':
            if not stack or (stack.pop() != '('):
                valid = False
        elif each==']':
            if not stack or (stack.pop() != '['):
                valid = False
        elif each=='}':
            if not stack or (stack.pop() != '{'):
                valid = False

    if not stack and (valid):
        return "Balanced"
    else:
        return "Unbalanced"


str = "[]({()[{}]})"  #"[(){((()))}()]" #"[{]}"
arr1 = '{[]{()}}'       # balanced
arr2 = '[{}{}(]'        # unbalanced
arr3 = '(}(}'           # unbalanced
arr4 = '({)}'           # unbalanced
arr5 = '[)'             # unbalanced
arr6 = '{{{[]}}}}'      # unbalanced
arr7 = '{{{[]}}}([)][[()){{}]}'      # unbalanced
print(balanced_parentheses(arr7))

