# 01_list.py
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicyles)
print(bicyles[0])
bicyles.append('gaint')
print(bicyles)
del bicyles[0]
print(bicyles)
print(bicyles[0]) ## will output second item/ cannodale
bicyles.remove('redline')
print(bicyles) ## redline not appear
# bicyles.sort()
print(sorted(bicyles)) ## order by alpha
print(bicyles)
print(len(bicyles))
# print(bicyles[10]) ## IndexError: list index out of range

for bike in bicyles:
	print(bike)


print("-------")

for value in range(1,5): ## 只打印到 4
	print(value)


numbers = range(1,10) ## 1,2,3,4,5,6,7,8,9
print(numbers[2:5]) ## range(3, 6)

numbers2 = [1,2,3,4,5,6,7,8,9]
print(numbers2[2:5]) ## [3, 4, 5]