class Publisher:

    def __init__(self):
        self.observers = [] # 观察者列表

    def add(self, observer): # 添加观察者
        if observer not in self.observers: # 如果观察者不在列表中
            self.observers.append(observer) # 向列表中添加观察者
        else: # 否则，观察者已经在列表中，已经在观察，为避免多次 notify
            print('Failed to add: {}'.format(observer)) # 添加失败提示

    def remove(self, observer): # 移除观察者
        try: #　尝试
            self.observers.remove(observer) # 从列表移除观察者
        except ValueError: # 如果观察者不在列表中，引发值异常
            print('Failed to remove: {}'.format(observer)) # 移除失败提示

    def notify(self): # 通知所有观察者，状态已经改变
        # 通知列表中的每一个观察值，状态已经改变
        [o.notify(self) for o in self.observers] 
        

class DefaultFormatter(Publisher): # 默认的被观察者，发布者，主持者

    def __init__(self, name):
        Publisher.__init__(self) # 调用发布者的初始化函数
        self.name = name
        self._data = 0 # _ 表示该属性不得被访问，私有

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property # 将方法装饰成属性
    def data(self):
        return self._data

    @data.setter # 向被 property 装饰成的属性赋值时调用函数
    def data(self, new_value): # self.data = x 等价于 self.data(x)?
        try: # 尝试
            self._data = int(new_value) # 将值转化为int并传递给 self._data
        except ValueError as e: # 转化失败产生异常
            print('Error: {}'.format(e)) # 输出
        else:
            self.notify() # 通知所有注册的观察者


class HexFormatter: # 十六进制的观察者

    def notify(self, publisher): # 被通知时的行为
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name, hex(publisher.data)))


class BinaryFormatter: # 二进制的观察者

    def notify(self, publisher): # 被通知时的行为
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,
                                                      publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf) # 添加观察者
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf) # 添加观察者
    df.data = 21
    print(df)

    print()
    df.remove(hf) # 移除观察者
    df.data = 40
    print(df)

    print()
    df.remove(hf) # 移除观察者
    df.add(bf) # 添加观察者
    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()
