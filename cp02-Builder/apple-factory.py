# coding: utf-8
"""
建造者模式和工厂模式的区别在于: 建造者模式需要一步一步构造对象, 而工厂模式只需要单个步骤.
攒电脑就是建造者模式, 买一台macbook pro型号出厂时就固定好的就是工厂模式
"""
MINI14 = '1.4GHz Mac mini'


class AppleFactory:

    # 这里使用了嵌套类, 这是禁止实例化一个类的简洁方式
    class MacMini14:

        def __init__(self):
            self.memory = 4  # 单位为GB
            self.hdd = 500  # 单位为GB
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I dont't know how to build {}".format(model))

if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI14)
    print(mac_mini)
