from cryptologic import *

def shift(cipher_text, key):
	plian_text = ""
	for i in range(len(cipher_text)):
		char_num = upper_to_number(cipher_text[i])
		char_num -= key
		char_num %= 26
		plian_text += number_to_lower(char_num)
	return plian_text

def affine(cipher_text, a, b):
	a_inv = multiple_inv(26, a)
	if a_inv == None:
		return "%(a)i has no inverse, can not decrypt cipher text." % locals()
	else:
		plian_text = ""
		for i in range(len(cipher_text)):
			char_num = upper_to_number(cipher_text[i])
			char_num = a_inv*(char_num - b)
			char_num %= 26
			plian_text += number_to_lower(char_num)
		return plian_text
	
def substitution(cipher_text, key_file):
	plian_text = ""
	mapping = list(26)
	f = open(key_file)
	for i in range(26):
		mapping[upper_to_number(f.read(1))] = i
	f.close()
	for i in range(len(cipher_text)):
		char_num = upper_to_number(cipher_text[i])
		char_num = mapping[char_num]
		plian_text += number_to_lower(char_num)
	return plian_text
	
def vigenere(cipher_text, key_list):
	plian_text = ""
	for i in range(len(cipher_text)):
		char_num = upper_to_number(cipher_text[i])
		char_num -= key_list[i%len(key_list)]
		char_num %= 26
		plian_text += number_to_lower(char_num)
	return plian_text
	
def hill(cipher_text, matrix):
	inverse = matrix_inv(matrix)
	if len(cipher_text)%2 != 0:
		return "text lenght must be even number"
	if inverse == None:
		return "matrix must have inverse in order to decrypt"
	else:
		plian_text = ""
		char_num = [[0, 0]]
		for i in range(int(len(cipher_text)/2)):
			char_num[0][0] = upper_to_number(cipher_text[2*i])
			char_num[0][1] = upper_to_number(cipher_text[2*i + 1])
			char_num = matrix_multiple(char_num, inverse)
			plian_text += number_to_lower(char_num[0][0])
			plian_text += number_to_lower(char_num[0][1])
		return plian_text