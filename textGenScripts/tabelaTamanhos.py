file1 = open('TabelaTamanhos','w') 
for i in ['tiny','scriptsize','footnotesize','small','normalsize','large','Large','LARGE','huge','Huge']: 
    a = "\\"+ i + "{"+i+"}" 
    b = "\\textbackslash " + i + "\\{" + i + "\\}"     
    file1.write(b + "&" + a + "\\\\ \\hline\n") 
file1.close()
