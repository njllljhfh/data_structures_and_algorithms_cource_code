# -*- coding:utf-8 -*-

def factorial(n):
    print(dir(), vars())
    if n == 0:
        return 1
    return n * factorial(n - 1)


def xxx():
    try:
        a = 1 / 0
        print(9999999999)
    except Exception as e:
        print(e)


def yyy():
    xxx()


if __name__ == '__main__':
    # print(factorial(0))
    # print(factorial(5))

    # # a = [i for i in range(200, 601, 5)]
    # a = [25,38,12,90]
    # # print(a)
    # b = []
    # for i in a:
    #     res = i % 13
    #     print(res)
    #     b.append(res)
    #
    # print("len(a)",len(a))
    # print("len(b)",len(b))
    #
    # print(len(set(b)))

    # yyy()

    from collections import OrderedDict

    # order_dict = OrderedDict()
    # print(f"order_dict={order_dict}")
    # order_dict["b"] = 2
    # order_dict["a"] = 1
    # order_dict["c"] = 3
    # print(f"order_dict={order_dict}")
    # - - -

    from collections.abc import MutableSet

    s = {1, 2, 3}
    t = {3, 4, 5}
    print(f"s={s}")
    print(f"t={t}")
    # ---
    print(s.isdisjoint(t))
    # ---
    print(s | t)
    # ---
    # s |= t
    # print(s)
    # ---
    print(s & t)
    # ---
    # s &= t
    # print(s)
    # ---
    print(s ^ t)
    # ---
    # s-=t
    # print(s)
    # ---
    print(s - t)
    # ---

    print(s.union(t))


    class A(object):

        def __init__(self, a):
            self.a = a

        def __repr__(self):
            return f"{self.a}"


    x = A(1)
    print(x)
    y = type(x)(2)
    print(y)
    # ---

    from collections import Counter

    counter = Counter()
    counter["a"] = 3
    counter["b"] = 2
    counter["c"] = 1
    print(counter)
    print(list(counter.elements()))
    print(counter.most_common(2))

    del counter["u"]

    # xxx={"a":1,"b":2}
    # del xxx["a"]
    # del xxx["w"]
