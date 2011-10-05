from cryptologic import *

def shift(plian_text, key):
	cipher_text = ""
	for i in range(len(plian_text)):
		char_num = lower_to_number(plian_text[i])
		char_num += key
		char_num %= 26
		cipher_text += number_to_upper(char_num)
	return cipher_text

def affine(plian_text, a, b):
	if gcd(26, a) != 1:
		return "gcd(26, %(a)i) must be 1" % locals()
	else:
		cipher_text = ""
		for i in range(len(plian_text)):
			char_num = lower_to_number(plian_text[i])
			char_num = a*char_num + b
			char_num %= 26
			cipher_text += number_to_upper(char_num)
		return cipher_text
	
def substitution(plian_text, key_file):
	cipher_text = ""
	mapping = list(26)
	f = open(key_file)
	for i in range(26):
		mapping[i] = upper_to_number(f.read(1))
	f.close()
	for i in range(len(plian_text)):
		char_num = lower_to_number(plian_text[i])
		char_num = mapping[char_num]
		cipher_text += number_to_upper(char_num)
	return cipher_text
	
def vigenere(plian_text, key_list):
	cipher_text = ""
	for i in range(len(plian_text)):
		char_num = lower_to_number(plian_text[i])
		char_num += key_list[i%len(key_list)]
		char_num %= 26
		cipher_text += number_to_upper(char_num)
	return cipher_text
	
def hill(plian_text, matrix):
	if len(plian_text)%2 != 0:
		return "text lenght must be even number"
	if matrix_inv(matrix) == None:
		return "matrix must have inverse in order to prevent decryption problem"
	else:
		cipher_text = ""
		char_num = [[0, 0]]
		for i in range(int(len(plian_text)/2)):
			char_num[0][0] = lower_to_number(plian_text[2*i])
			char_num[0][1] = lower_to_number(plian_text[2*i + 1])
			char_num = matrix_multiple(char_num, matrix)
			cipher_text += number_to_upper(char_num[0][0])
			cipher_text += number_to_upper(char_num[0][1])
		return cipher_text