# LeetCode 200. Numbers of Islands

1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라. (연결되어 있는 1의 덩어리 개수를 구하라)

### [Answer 1] DFS로 그래프 탐색
+ 그래프는 아니지만, 동서남북이 모두 연결된 그래프로 가정하고, 네 방향 각각 DFS 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악할 수 있음

#### 1. 육지 발견 함수 
```python
for i in range(len(grid)): # 행 갯수
    for j in range(len(grid[0])): # 열 갯수
        if grid[i][j] == '1': # 육지를 발견하면
            self.dfs(grid, i, j) # self.dfs 호출 후 탐색 시작
```
#### 2. 탐색
``` python
def dfs(self, grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) of grid[i][j] != '1':
        return # 육지가 아닌 곳이라면 종료

    grid[i][j] = '0' # 다시 계산하지 않도록 이미 방문한 곳은 1이 아닌 값으로 변경해줌

    # 동서남북 탐색
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)

    # 재귀 호출이 백트래킹으로 모두 빠져 나오면 섬 하나를 발견한 것으로 간주
```
+ dfs()함수를 빠져 나온 후에는 해당 위치에서 탐색할 수 있는 모든 육지를 탐색한 것이므로 카운트를 1 증가시킨다.

#### 동서남북 탐색 부분 개선
