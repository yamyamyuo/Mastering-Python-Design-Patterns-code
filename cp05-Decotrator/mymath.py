# coding: utf-8
"""
想对一个对象添加额外的功能, 可以修改类的逻辑, 使用组合, 使用继承. 但是继承是静态的,
修饰器模式提供了动态扩展一个对象的能力.

横切关注点 cross-cutting concerns

一个函数接收另一个函数作为参数，这种函数就称之为高阶函数。
编写高阶函数，就是让函数的参数能够接收别的函数。


使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，
比如函数的docstring、__name__、参数列表, 这时候可以使用@functools.wraps
"""
import functools


def memoize(fn):
    known = dict()

    # wraps 推荐使用, 为创建装饰器模式提供便利, 它能够保留被修饰函数的文档和签名.
    @functools.wraps(fn)
    def memoizer(*args):

        # print (fn.__name__)      # 输出 'memoizer'
        # print (fn.__doc__)       # 输出 None
        # 函数 fn 被 memoizer 取代了，当然它的docstring，__name__就是变成了 memoizer 函数的信息了
        #  @functools.wraps(fn) 可以避免这个问题
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer

def logger(fn):

    @functools.wraps(fn)
    def logit(*args):
        print("log something %s" % fn.__name__)

    return logit


@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

@logger
def wtf(a):
    assert(a >= 8), 'a must be >= 8'
    return a

if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(3)', 'import': 'fibonacci',
                'func': fibonacci},
                {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}
                                     ]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import \
            {}'.format(m['import']))

        # 这里打印的__name__ 和 __doc__, 如果把 @functools.wraps(fn) 注释掉, 就会没有文档信息
        print('name: {}, doc: {}, executing: {}, time: \
            {}'.format(m['func'].__name__, m['func'].__doc__,
                       m['exec'], t.timeit()))

    # 如何直接调用装饰器
    z = memoize(fibonacci)
    a = z(5)
    print(a)

    f = logger(wtf)
    print("--------")
    f(9)
