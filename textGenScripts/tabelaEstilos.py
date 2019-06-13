file1 = open('TabelaEstilos','w')
for i in ['textrm','textsf','texttt','textmd','textbf','textup','textit','textsl','textsc','emph','textnormal']:
    a = "\\"+ i + "{"+i+"}"
    b = "\\textbackslash " + i + "\\{" + i + "\\}"
    file1.write(b + "&" + a + "\\\\ \\hline\n")
file1.close()
