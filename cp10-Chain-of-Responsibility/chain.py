# coding: utf-8

class Event:

    def __init__(self, name): # 消息初始化
        self.name = name

    def __str__(self):
        return self.name # str(e) 得到消息


class Widget:

    def __init__(self, parent=None): # 初始化动态分发框架
        self.parent = parent # 责任链的上一级对象

    def handle(self, event): # 事件处理和分发和转移
        handler = 'handle_{}'.format(event) # 事件处理函数的格式， 处理 x 事件的函数名称为 handle_x
        if hasattr(self, handler): # 如果对象自己有该消息的处理函数
            method = getattr(self, handler) # 将自己的消息处理函数提取为 method
            method(event) # 执行处理函数，处理该消息，并消灭该c消息(即处理完毕，不再传播)
        elif self.parent: # 如果该对象在责任链上有上级对象
            print("上级对象: %s" % self.parent)
            self.parent.handle(event) # 将消息交给上级对象处理
        elif hasattr(self, 'handle_default'): # 如果该对象在责任链上无上级，且有默认处理函数
            self.handle_default(event) # 对事件调用默认处理函数
        # 若都没有处理则忽略该消息，也可传出异常？


class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    # parent 像一个指针一样, 一层一层往上传递
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)
    haha = SendDialog(msg)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)
        print('Sending event -{}- to haha'.format(evt))
        haha.handle(evt) # 由对象 haha 处理消息 'paint' 相当于 haha 截了 sd 的胡

if __name__ == '__main__':
    main()
