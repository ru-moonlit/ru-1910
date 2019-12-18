"""
    2048 游戏核心算法

    1. 降维思想:因为行与行/列与列相对独立,
              所以可以将二维列表的操作转换为对一维列表操作
              对矩阵进行转置,然后可以将列操作转化为行操作.
    2. 高内聚:
        每个函数内部小而精

     核心流程:列 --> 行 --> 去零 --> 合并(i == i+1)
"""
# 全局变量
list_merge = [2, 0, 2, 2]  # 2 2 0 0


# 1. 定义函数,将零元素移动到末尾.
# 输入:[2, 0, 2, 0]
# 输出:[2, 2, 0, 0] (不用返回值)
def zero_to_end():
    # 核心思想:倒序删除0元素,后面追加0元素.
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试代码
# zero_to_end()
# print(list_merge)


# 2. 定义函数,合并相同元素(非零)
# 输入:[2, 2, 0, 0]
# 输出:[4, 0, 0, 0]
# 输入:[2, 0, 0, 2] -- > [2, 2, 0, 0]
# 输出:[4, 0, 0, 0]
# 输入:[2, 0, 2, 2] -- > [2, 2, 2, 0]
# 输出:[4, 2, 0, 0]
# 输入:[8, 8, 8, 8]
# 输出:[16, 16, 0, 0]
def merge():
    # 核心思想:先将0元素移动到末尾,再判断相邻相同
    zero_to_end()
    for i in range(len(list_merge) - 1):  # 3
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# 测试代码
# merge()
# print(list_merge)
map = [
    [2, 0, 2, 0],
    [2, 4, 0, 2],
    [0, 0, 2, 0],
    [2, 4, 4, 2],
]


# 3. 定义函数,向左移动.
# 提示:每行交给list_merge,再调用练习2
def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()


# move_left()
# print(map)

# 4. 定义函数,向右移动.
# 提示:将每行反向切片交给list_merge,再调用练习2
def move_right():
    global list_merge
    for line in map:
        # 因为切片拷贝了新列表,所以merge操作的是新列表,与map无关.
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


# move_right()
# print(map)

# 5. 定义函数,向上移动.
# 提示:方阵转置,在调用练习3
def square_matrix_transposition(list_matrix):
    for c in range(1, len(list_matrix)):
        for r in range(c, len(list_matrix)):
            list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]


def move_up():
    square_matrix_transposition(map)
    move_left()
    square_matrix_transposition(map)


# move_up()
# print(map)

# 6. 定义函数,向下移动.
# 提示:方阵转置,在调用练习4
def move_down():
    square_matrix_transposition(map)
    move_right()
    square_matrix_transposition(map)


move_down()
print(map)
