# -*- coding: utf-8 -*

#ターゲット(t)の座標を返す
def find_coordinate(m, t):
    for i, l in enumerate(m):
        for j, e in enumerate(l):
            if e == t:
                return [i, j]


def to_map(m):
    for line in m:
        line = list(map(str,line))
        print(''.join(line))


def find_root(m, g, n):

    x = g[0]
    y = g[1]
    
    current = []
    tmp = _update(m, x, y+1, n)
    if tmp:
        current.append(tmp)
    tmp = _update(m, x, y-1, n)
    if tmp:
        current.append(tmp)
    tmp = _update(m, x+1, y, n)
    if tmp:
        current.append(tmp)
    tmp = _update(m, x-1, y, n)
    if tmp:
        current.append(tmp)
    for p in current:
        find_root(m, p, n+1)
    

def _update(m, x, y, n):
    if m[x][y] == '*':
        return False
    if m[x][y] == ' ':
        m[x][y] = n
        return [x, y]


def _output(m, x, y):
    up, down, left, right = m[x-1][y],m[x+1][y],m[x][y-1],m[x][y+1]
    _l = [up, down, left, right]
    if 'G' in _l:
        return 1
    elif all(list(map(lambda x: type(x) is not int,  _l))):
        return 'Fail'
    else:
        return min(filter(lambda x: type(x) is int, _l)) + 1


f = open('test2.txt')
maze = f.read().splitlines()
m = []
for line in maze:
    m.append(list(line))
f.close()
goal = find_coordinate(m, 'G')
start = find_coordinate(m, 'S')
find_root(m, goal, 1)
print(_output(m, start[0], start[1]))




