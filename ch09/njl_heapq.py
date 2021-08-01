# -*- coding:utf-8 -*-
import heapq

if __name__ == '__main__':
    # heapq模块, 把列表作为堆，进行管理
    print(f"堆初始状态")
    lsA = [5, 4, 6, 1, 3, 7, 9, 8, 2, 11]
    print(lsA)
    print("- " * 20)

    """以下函数 不要求 列表中的元素顺序满足heap-oder属性"""
    print(f"nlargest(k,iterable): 从一个给定的迭代中生成含有前k个最大值的列表")
    # 时间复杂度：O(n + k·log n)
    res = heapq.nlargest(3, lsA)
    print(f"res={res}")
    print(lsA)
    print("- " * 20)

    print(f"nlargest(k,iterable): 从一个给定的迭代中生成含有前k个最小值的列表")
    # 时间复杂度：O(n + k·log n)
    res = heapq.nsmallest(3, lsA)
    print(f"res={res}")
    print(lsA)
    print("- " * 20)

    print(f"heapify(L,e): 改变未排序的列表，使其满足heap-order属性")
    # 时间复杂度：O(n)，该函数使用自底向上的方法构建堆
    heapq.heapify(lsA)
    print(lsA)
    print("- " * 20)

    """以下函数需要列表中的元素顺序满足heap-oder属性"""
    print(f"heappush(L,e): 将元素插入列表，并重新调整列表，使其满足heap-order属性")
    # 时间复杂度：O(log n)
    heapq.heappush(lsA, 0)
    print(lsA)
    print("- " * 20)

    print(f"heappop(L): 取出最小值元素")
    # 时间复杂度：O(log n)
    smallValue = heapq.heappop(lsA)
    print(f"最小值：{smallValue}")
    print(lsA)
    print("- " * 20)

    print(f"heappushpop(L,e): 放入元素e，并取出最小值")
    # 时间复杂度：O(log n)
    smallValue = heapq.heappushpop(lsA, 12)
    print(f"最小值：{smallValue}")
    print(lsA)
    print("- " * 20)

    print(f"heapreplace(L,e): 相当于先pop出当前堆中最小值，在push新元素到堆中")
    # 时间复杂度：O(log n)
    smallValue = heapq.heapreplace(lsA, -5)
    print(f"最小值：{smallValue}")
    print(lsA)
    print("- " * 20)
