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
'''
#3rd version：结合肖哥的思路和上一个stack的思路的综合版本。
'''
def balanced_parentheses(str):
    valid = True
    detect_stack = []
    left_parentheses = "([{"
    right_parentheses = ")]}"
    parentheses_dict = {'(':')', '[':']', '{':'}'}

    for each in str:
        if (each in left_parentheses):
            detect_stack.append(each)
        elif each in right_parentheses:
            if not detect_stack or (each != parentheses_dict[detect_stack.pop()]):
                valid = False

    if not detect_stack and (valid):
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
arr8 = '))))'
print(balanced_parentheses(arr8))

