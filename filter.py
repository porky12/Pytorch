def is_palindrome(n):
 	L=str(n)
 	for i in range(len(L)):
 		if (L[i]==L[-i-1])==False:
 			return False
 		else :
 			pass
 	return True
output = filter(is_palindrome, range(1, 20000))
print(list(output))