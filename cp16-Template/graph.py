# coding: utf-8

# 算法中的path不是最优的路径，
# 而是搜索过程中的遍历路径
def bfs(graph, start, end): # 广度优先图搜索
    path = [] #　访问路径链
    visited = [start] # 访问起始城市加入要访问的列表
    while visited: # 访问城市不为空
        current = visited.pop(0) # 弹出当前的城市
        if current not in path: # 如果当前的城市没有在访问路径中
            path.append(current) # 将当前的城市添加到访问路径中
            if current == end: # 如果当前的城市是目标城市
                print(path) # 输出访问路径
                return (True, path)
            if current not in graph: # 如果当前城市不在图的起点城市中，
                continue # 则不能作为访问的起点，跳过去
        # 将当前城市的可访问城市添加到要访问的目标城市列表中
        visited = visited + graph[current] # 并作为优先访问（在后面优先 pop）的目标城市
    return (False, path)


def dfs(graph, start, end): # 深度优先图搜索
    path = [] #　访问路径链
    visited = [start] # 访问起始城市加入要访问的列表
    while visited: # 访问城市不为空
        current = visited.pop(0) # 弹出当前的城市
        if current not in path: # 如果当前的城市没有在访问路径中
            path.append(current) # 将当前的城市添加到访问路径中
            if current == end: # 如果当前的城市是目标城市
                print(path) # 输出访问路径
                return (True, path)
            if current not in graph: # 如果当前城市不在图的起点城市中，
                continue # 则不能作为访问的起点，跳过去
        # 将当前城市的可访问城市添加到要访问的目标城市列表中
        visited = graph[current] + visited # 并将当前的访问列表作为优先的目标城市（在后面的先 pop）
    return (False, path)


def main():
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart', 'Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
    }

    bfs_path = bfs(graph, 'Frankfurt', 'Nurnberg')
    dfs_path = dfs(graph, 'Frankfurt', 'Nurnberg')
    print('bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
    print('dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))

    bfs_nopath = bfs(graph, 'Wurzburg', 'Kassel')
    print('bfs Wurzburg-Kassel: {}'.format(bfs_nopath[1] if bfs_nopath[0] else 'Not found'))
    dfs_nopath = dfs(graph, 'Wurzburg', 'Kassel')
    print('dfs Wurzburg-Kassel: {}'.format(dfs_nopath[1] if dfs_nopath[0] else 'Not found'))

if __name__ == '__main__':
    main()
