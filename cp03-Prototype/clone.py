import copy
"""
https://docs.python.org/3/library/copy.html

copy.copy(x)
Return a shallow copy of x.

copy.deepcopy(x[, memo])
Return a deep copy of x.

The difference between shallow and deep copying is only relevant for
compound objects (objects that contain other objects, like lists or class instances)

浅副本依赖了引用, 引入数据共享和写时复制一类的技术可以优化内存性能, 减少克隆的时间以及内存使用. 
"""

class A:

    def __init__(self):
        # 不可变对象（变量指向的内存的中的值不能够被改变）
        # 当更改该对象时，由于所指向的内存中的值不可改变，所以会把原来的值复制到新的空间，
        # 然后变量指向这个新的地址。
        # python中数值类型（int和float），布尔型bool，字符串str，元组tuple都是不可变对象。
        self.x = 18
        self.msg = 'Hello'
        # 可变对象（变量指向的内存的中的值能够被改变）
        # 当更改该对象时，所指向的内存中的值直接改变，没有发生复制行为。
        # python中列表list，字典dict，集合set都是可变对象。包括自定义的类对象也是可变对象。
        self.compount_obj = [1,2,3]


class B(A):

    def __init__(self):
        A.__init__(self)
        self.y = 34

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.x, self.msg, self.y, repr(self.compount_obj))

if __name__ == '__main__':
    b = B()
    print("b 的地址: 0x%x" % id(b))
    print("b.compount_obj 的地址: 0x%x" % id(b.compount_obj))
    print("b.y 的地址: 0x%x" % id(b.y))

    e = copy.copy(b)
    print("shallow copy >>>>>>>>>>>")
    # e的地址跟b不一样了
    print("e 的地址: 0x%x" % id(e))
    # 如果是shallow copy, mutable types 直接复制了引用
    print("e.compount_obj 的地址: 0x%x" % id(e.compount_obj))
    print("e.y 的地址: 0x%x" % id(e.y))


    c = copy.deepcopy(b)
    print("deep copy >>>>>>>>>>>>>>")
    print("c 的地址: 0x%x" % id(c))
    # 如果是deepcopy, 这里的引用都不一样了
    print("c.compount_obj 的地址: 0x%x" % id(c.compount_obj))
    c.y += 2
    print("c.y 的地址: 0x%x" % id(c.y))


    d = b
    print("简单的赋值 >>>>>>>>>>>>>>>")
    # d只是b的引用, 地址都跟b一样
    print("d 的地址: 0x%x" % id(d))
    # 如果通过d去改变属性, 最后b的属性y也会改变
    d.y = 35


    print([str(i) for i in (b, c)])
    print([i for i in (b, c)])
