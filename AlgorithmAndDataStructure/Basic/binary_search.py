def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid  = (low+high) // 2
		guess = list[mid]
		if guess == item:
			return print('Yeah,found it:%d'%mid)
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1

	return print('Oops,there is no one.')
'''for example'''
my_list = [1,4,8,9,22,55,65,89,321,2345]

binary_search(my_list, 2345)