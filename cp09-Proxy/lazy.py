# coding: utf-8


class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print('function overriden: {}'.format(self.method))
        print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        if not obj:
            return None
        """
        这一步会调用 Test 的 resource 方法
        """
        value = self.method(obj)
        #print('value {}'.format(value))
        """
        这个是为了python2, python3不需要, 将resource的值赋予为新的value,
        即tuple(range(5))

        print(t.resource)
        >>> (0, 1, 2, 3, 4)

        不执行这一步的话:
        print(t.resource)
        >>> <__main__.LazyProperty instance at 0x102843c20>
        """
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
        # python 2.7.x
        t = Test()
        print(t.x)
        #>>> foo
        print(t.y)
        #>>> bar
        print(t.resource)
        #>>> <__main__.LazyProperty instance at 0x02C2E058>
        print(t.resource.__get__(t,Test))
        #>>> initializing self._resource which is: None
        #>>> (0, 1, 2, 3, 4)
        print(t.resource)
        #>>> (0, 1, 2, 3, 4)

    def main_Py3():
        # python 3.x
        t = Test()
        print(t.x)
        #>>> foo
        print(t.y)
        #>>> bar
        print(t.resource)
        #>>> initializing self._resource which is: None
        #>>> (0, 1, 2, 3, 4)
        print(t.resource)
        #>>> (0, 1, 2, 3, 4)

        def main():
            import sys
            if sys.version_info < (3,0):
                main_Py27()
            else:
                main_Py3()

        if __name__ == '__main__':
            main()

t = Test()
print(t.x)
#>>> foo
print(t.y)
#>>> bar
print(t.resource)
print(t.resource.__get__(t,Test))
print(t.resource)
