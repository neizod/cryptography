start_lower = ord('a')
start_upper = ord('A')

def lower_to_number(text):
	return ord(text) - start_lower

def upper_to_number(text):
	return ord(text) - start_upper

def number_to_lower(num):
	return chr(num + start_lower)
	
def number_to_upper(num):
	return chr(num + start_upper)

def gcd(a, b):
	if a%b == 0:
		return b
	else:
		return gcd(b, a%b)

def multiple_inv(a, b, s = 0, t = 1):
	if a%b == 0:
		if b == 1:
			return t
	else:
		return multiple_inv(b, a%b, t, (s-t*int(a/b))%26)

def matrix_multiple(matrix_1, matrix_2):
	result_matrix = matrix()
	for i in range(len(matrix_1)):
		for j in range(len(matrix_2[0])):
			for k in range(len(matrix_1[0])):
				result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
				result_matrix[i][j] %= 26
	return result_matrix

def matrix_inv(m):
	det_inv = determinant_inv(m)
	if det_inv != None:
		inverse = matrix(m[1][1], -m[0][1], -m[1][0], m[0][0])
		for i in range(2):
			for j in range(2):
				inverse[i][j] *= det_inv
				inverse[i][j] %= 26
		return inverse

def determinant_inv(m):
	determinant = m[0][0]*m[1][1] - m[0][1]*m[1][0]
	if determinant != 0:
		return multiple_inv(26, determinant%26)

def matrix(a00 = 0, a01 = 0, a10 = 0, a11 = 0):
	return [[a00%26, a01%26], [a10%26, a11%26]]

def list(n):
	return [None for i in range(n)]