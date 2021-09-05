# -*- coding:utf-8 -*-
# 用栈来计算+-*/四则运算

def calculate(tokens: str):
    stack = []
    for t in tokens:
        if t in '+-x*/':  # t is an operator symbol
            stack.append(t)  # push the operator symbol
        elif t not in '()':  # consider t to be a literal
            stack.append(float(t))  # push trivial tree storing value
        elif t == ')':  # compose a new tree from three constituent parts
            right = stack.pop()  # right subtree as per LIFO
            op = stack.pop()  # operator symbol
            left = stack.pop()  # left subtree

            if op == '+':
                res = left + right
            elif op == '-':
                res = left - right
            elif op == '/':
                res = left / right
            else:  # treat 'x' or '*' as multiplication
                res = left * right
            stack.append(res)  # repush tree
    if stack:
        return stack.pop()


if __name__ == '__main__':
    exp = '((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'

    print(calculate(exp))
