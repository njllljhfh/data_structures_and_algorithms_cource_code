# -*- coding:utf-8 -*-
from collections import deque

if __name__ == '__main__':
    dq = deque()

    dq.appendleft(1)
    print(dq)

    dq.append(2)
    print(dq)

    dq.append(3)
    print(dq)

    print(f'最左端数据: {dq[0]}')
    print(f'最右端数据: {dq[-1]}')

    dq.pop()
    print(dq)

    dq.popleft()
    print(dq)

    print(f'当前队列中数据个数：{len(dq)}')
