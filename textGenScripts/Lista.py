file1 = open('listas.tex','w') 
for i in ['itemize','enumerate']: 
	file1.write("\\begin{"+i+"}\n")
	for j in range(5):
		file1.write("\\item item" + str(j) +"\n")
	file1.write("\\end{"+i+"}\n")
file1.close()
