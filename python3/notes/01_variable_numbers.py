# 01_variable_numbers.py
print(3 ** 2) ## should be 3 power 2 9
print( 3 * 2) ## should 6
print(0.1 + 0.1) ## 0.2
print(0.1 + 0.2) ## should be 0.3 , got 0.30000000000000004
print(4/2) ## 2.0, 任何两个数相除，得到 浮点数
print(123_456_3) ## 数字中的下划线会被忽略, 和golang一样

x, y , z = 10,9, 7 ## 多赋值
print(f"x is: {x}, y is:{y}, z: {z}")

MAX_SPEED = 1.9 ## python 没有常数(constant)，一般程序员会认为全大写变量为常数
MAX_SPEED = 2.0 ## 程序不会报错，但不推荐

