from external import Synthesizer, Human


class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'

"""
创建通用的Adapter类, 将一些带不同接口的对象(如Computer是execute方法,
Synthesizer 是play, Human 是 speak)适配到一个统一的接口中.
"""
class Adapter:

    def __init__(self, obj, adapted_methods):
        """
        obj: 想要适配的对象
        adapted_methods: 一个字典, 键值对. key是想要被调用的方法, value是应该被调用的方法
        """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

    @property
    def name(self):
        return self.obj.name


def main():
    # objects 容纳着所有对象, 兼容Computer的对象可以直接append
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    # 不兼容Computer的对象需要使用Adapter来适配一下再添加到objects中
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    # 最终所有对象都可以调用execute方法, 而无需关心类之间的接口差异
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

    for i in objects:
        print(i.name)

if __name__ == "__main__":
    main()
