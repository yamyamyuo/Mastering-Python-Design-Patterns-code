# coding: utf-8


class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        #print('function overriden: {}'.format(self.method))
        #print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        #print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 假设这一行的计算成本比较大
        return self._resource

def main_Py27():
    t = Test()
    print(t.x)
    print(t.y)
    # 在 python 2.7.12 中
    print(t.resource) # 这是一个 LazyProperty 的 instance (实例)
    print(t.resource.__get__(t,Test)) # 调用 get 方法，将 t.resource 变为属性值
    print(t.resource) # 再调用，得到的是 t.resource 属性值，不再计算
    
def main_Py3():
    t = Test()
    print(t.x)
    print(t.y)
    # 做更多的事情。。。
    # 在 Python 3.x 中
    print(t.resource) # 第一次调用，运行 resource() 方法，并将 t.resource 设定为其返回值
    print(t.resource) # 再调用，得到的是 t.resource 属性值，不再计算

def main():
    import sys
    if sys.version_info < (3,0):
        main_Py27()
    else:
        main_Py3()
        
if __name__ == '__main__':
    main()
