def split(string, delim):
	i = 0
	start = i
	l = len(string)
	while i < l:
		if string[i] == delim:
			yield string[start:i]
			start = i+1	
		i = i+1

	yield string[start:]	


a = "It is a far, far better thing that I do, that I have ever done"        
for s in split(a,' '):
	print(s)


