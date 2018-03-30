"""按特定顺序对一串数据进行排序。
排序算法的稳定性，让相等键值的记录维持次序，例如：
(3,1)(3,7)(4,1)(5,6)维持次序
(3,7)(3,1)(4,1)(5,6)次序被改变"""

"""Bubble Sort冒泡排序,第一次冒泡把最大的推到最上面，
第二次把第二大的推到最大的后面，最多需要冒泡的次数为
元素总数减1"""
def bubble_sort(list):
	"""j为每次遍历需要比较的次数，逐次减小1"""
	for j in range(len(alist)-1,0,-1):
		for i in range(j):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]

"""Selection sort选择排序：包括如何选出列表中的
最小值"""
def selection_sort(alist):
	n = len(alist)
	"""需要进行次n-1选择操作，逐次找出
	最大，次最大，，，，"""
	for i in range(n-1):
		"""记录最小的位置"""
		min_index = i
		"""从i+1位置开始选出最小数据"""
		for j in range(i+1, n):
			if alist[j] < alist[min_index]:
				min_index = j
		"""如果选出的数据不在正确位置，进行交换"""
		if min_index != i:
			alist[i], alist[min_index] = alist[min_index], alist[i]

"""Insertion Sort插入排序"""
def insert_sort(alist):
	"""从第二个位置，即下标为1的元素开始向前插入"""
	for i in range(1, len(alist)):
		for j in range(i, 0, -1):
			"""从第i个元素向前比较，如果小于前一个元素，交换位置"""
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]

"""Quick sort快速排序"""
def quick_sort(alist, start, end):
	if start >= end:
		return

	mid = alist[start]
	low = start
	high = end

	while low < high:
		while low < high and alist[high] >= mid:
			high -= 1
			alist[low] = alist[high]

		while low < high and alist[low] < mid:
			low += 1
		alist[high] = alist[low]
	alist[low] = mid
	quick_sort(alist, start, low-1)
	quick_sort(alist, low+1, end)
			
"""Shell sort希尔排序，是改进版直接插入排序算法"""
def shell_sort(alist):
	n = len(alist)
	gap = n / 2
	while gap > 0:
		for i in range(gap, n):
			j = i
			while j>= gap and alist[j-gap] > alist[j]:
				alist[j-gap], alist[j] = alist[j], alist[j-gap]
				j -= gap
		gap = gap / 2

"""merge_sort归并排序"""
def merge_sort(alist):
	if len(alist) <= 1:
		return alist
	num = len(alist)/2
	left = merge_sort(alist[:num])
	right = merge_sort(alist[num:])
	return merge_sort(left, right)

def merge(left, right):
	l, r = 0, 0
	result = []
	while l<len(left) and r<len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result += left[l:]
	result += right[r:]
	return result

		
				

			
		

