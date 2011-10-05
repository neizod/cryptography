def multiple(matrix_1, matrix_2):
	if len(matrix_1[0]) != len(matrix_2):
		return("can not multiple matrix")
	else:
		result_matrix = matrix(len(matrix_1), len(matrix_2[0]))
		for m in range(len(matrix_1)):
			for n in range(len(matrix_2[0])):
				for i in range(len(matrix_1[0])):
					result_matrix[m][n] += matrix_1[m][i] * matrix_2[i][n]
		return(result_matrix)

def show(matrix):
	for col in matrix:
		print(col)

def matrix(m, n):
	matrix = [[0 for row in range(n)] for col in range(m)]
	return(matrix)
