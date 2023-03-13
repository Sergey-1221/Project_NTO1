t = int(input())

import itertools
import copy
import sys
sys.stdout = open("out.txt", 'w')
def check_martix(martix, arr):
	arr_ = arr.copy()
	for i in martix:
		try:
			arr_.remove(i)
		except:
			pass
	for x in range(len(martix)):
		y = ""
		for i in martix:
			y += i[x]
		try:
			arr_.remove(y)
		except:
			pass

	if len(arr_) == 0:
		return True
	else:
		return False


for t_ in range(t):
	n = int(input())
	arr = []
	for i in range(n*2):
		arr.append(input())

	arr_0 = {}
	for i in arr:
		if i[0] in arr_0.keys():
			arr_0[i[0]].append(i)
		else:
			arr_0[i[0]] = [i]
	state = False

	for key in arr_0.keys():
		if state:
			break

		if len(arr_0[key]) > 1:
			x = 0
			comb = []
			for z in range(len(arr_0[key])):
				comb.append(z)


			for i in itertools.combinations(comb, r=2):
				if state:
					break
				arr_ = copy.deepcopy(arr_0)
				matrix = []
				i1, i2 = i
				i1 = arr_0[key][i1]
				i2 = arr_0[key][i2]
				arr_[key].remove(i1)
				arr_[key].remove(i2)
				matrix.append([i1])
				
				#
				for z_ in range(1, n):
					i_ = i2[z_]
					if i_ in arr_.keys():
						matrix_ = []
						for z in arr_[i_]:
							matrix_.append(z)
						matrix.append(matrix_)

				
				for m in itertools.product(*matrix):
					if check_martix(m, arr):
						for m_ in m:
							print(m_)

						print()
						state = True
						break
