#예제 3-1. 거스름돈

coins = [10, 50, 100, 500]
N = int(input())
count = 0

index = len(coins)-1
while index >= 0:
    if N - coins[index] >= 0:
        N -= coins[index]
        count += 1
    elif N - coins[index] < 0:
        index -= 1
    if N == 0:
        break

print(count)

#답안

coins = [500, 100, 50, 10]
N = int(input())
count = 0

for i in coins:
    count += N // i
    n %= i

#예제 3-2. 큰 수의 법칙

input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr_sorted = sorted(arr, reverse = True)

result = 0
count = 0
index = 0
index_count = 0

while count != M:
    if index_count < K:
        result += arr_sorted[index]
        index_count += 1
        count += 1
    elif index_count == K:
        index += 1
        index_count = 0
        result += arr_sorted[index]
        count += 1
        index = 0

print(result)

#예제 3-3. 숫자 카드 게임

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
mins = []

for i in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    mins.append(min(data))

index = 0
for i in range(N):
    if mins[i] == max(mins):
        index = i

print(min(arr[index]))

#예제 3-4. 1이 될 때까지

input = sys.stdin.readline
N, K = map(int, input().split())

count = 0
while N != 1:
    if N % K == 0:
        N = N / K
        count += 1
    else:
        N = N - 1
        count += 1

print(count)

#예제 4-1. 상하좌우

input = sys.stdin.readline
N = int(input())
moves = list(map(str, input().split()))

x, y = 1, 1

for i in range(len(moves)):
    if moves[i] == 'L' and y > 1:
        y -= 1
    elif moves[i] == 'R' and y < N:
        y += 1
    elif moves[i] == 'U' and x > 1:
        x -= 1
    elif moves[i] == 'D' and x < N:
        x += 1

print(x, y)

#예제 4-2. 시각

N = int(input())

h = 0
m = 0
s = 0

count = 0

while h < N+1:
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if '3' in str(h) + str(m) + str(s):
        count += 1

print(count)

#실전 4-2. 왕실의 나이트

pos = str(input())
x = int(ord(pos[0])) - 96
y = int(pos[1])

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)


#실전 4-3. 게임 개발

input = sys.stdin.readline
N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move_count = 1
turn_count = 0

def turn_left():
    global d
    if d == 0:
        d += 3
    else:
        d -= 1

while turn_count <= 4:
    turn_left()
    turn_count += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if arr[nx][ny] == 0:
        x = x + dx[d]
        y = y + dy[d]
        arr[x][y] = 2
        move_count += 1
        turn_count = 0

    if turn_count == 4:
       bx = x - dx[d]
       by = y - dy[d]

       if arr[bx][by] != 1:
           turn_count = 0
           x = x - dx[d]
           y = y + dy[d]

       elif arr[bx][by] == 1:
           print(move_count)
           break

#실전 5-3. 음료수 얼려 먹기

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


#실전 5-4. 미로 탈출

from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append(x, y)
    while queue:
        x, y = queue.popleft(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))

#실전 6-2. 위에서 아래로

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
for i in range(N):
    print(sorted(arr, reverse = True)[i], end = ' ')

#실전 6-3. 성적이 낮은 순서로 학생 출력하기

N = int(input())
arr = []
for _ in range(N):
    a, b = map(str, input().split())
    arr.append([int(b), a])
for i in sorted(arr):
    print(i[1], end = ' ')

#실전 6-4. 두 배열의 원소 교체

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B, reverse = True)

for i in range(N):
    if i <= K-1:
        if A[i] < B[i]:
            A[i] = B[i]
    else:
        continue

print(sum(A))


