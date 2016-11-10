from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


@acts_as_state_machine # 装饰器指定一个状态机类
class Process: # 进程模型
    # 指定状态，一个状态就是一个 State，可用带时态的单词命名
    created = State(initial=True) # 创建状态, initial=True 指定为初始状态
    waiting = State() # 等待状态
    running = State() # 运行状态
    terminated = State() # 停止状态
    blocked = State() # 阻塞状态
    swapped_out_waiting = State() # 换出并等待状态
    swapped_out_blocked = State() # 换出并阻塞状态

    # 指定状态转换，一个状态转换就是一个 Event，
    # 装换也是一个动作，可用作为动词的单词命名
    # 等待事件，从创建状态，运行状态，阻塞状态和唤醒并等待状态变为等待状态
    wait = Event(from_states=(created, running, blocked,
                              swapped_out_waiting), to_state=waiting)
    # 运行事件，从等待状态变为运行状态
    run = Event(from_states=waiting, to_state=running)
    # 停止事件，从运行状态变为终止状态
    terminate = Event(from_states=running, to_state=terminated)
    # 阻塞事件，从运行状态，唤醒并阻塞状态变为阻塞状态
    block = Event(from_states=(running, swapped_out_blocked),
                  to_state=blocked)
    # 换出并等待事件，从等待状态变为换出并等待状态
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    # 换出并阻塞事件，从阻塞状态变为换出并等待状态
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    @after('wait') # 在 wait 转换之后运行
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run') # 在 run 转换之后运行
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate') # 在 terminate 转换之前运行
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block') # 在 block 转换之后运行
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait') # 在 swap_wait 转换之后运行
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block') # 在 swap_block 转换之后运行
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err: # 状态转换失败
        print('Error: transition of {} from {} to {} failed'.format(process.name,
                                                                    process.current_state, event_name))


def state_info(process):
    print('state of {}: {}'.format(process.name, process.current_state)) # current_state 当前的状态


def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'

    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

if __name__ == '__main__':
    main()
