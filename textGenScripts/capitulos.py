comentar o erro se tiver a certeza, correr o programa substituirá todos os ficheiros de texto previmente criados
file1 = open('chapter.tex','w')
for i  in ['Pacotes \LaTeX','Caracteres Especiais', 'Listas e Tabelas','Modo Matemática','Criação Gráficos', 'Projetos com \LaTeX: Comando input','Referências a Documentos Externos', 'Inclusão de Imagens','Fontes e Linguagens']:
    a = i.replace(' ','').lower().replace('ç','c').replace('ã','a').replace('á','a').replace(':','').replace('\\','').replace('ê','e')
    b = """
\section{"""+i+"""}
\label{chap."""+a+"""}
\input{textos/"""+a+""".tex}\n"""
    file1.write(b)
    file2 = open('../textos/' + a + '.tex','w')
    file2.write("Escrever aqui Capitulo " + i)
    file2.close()
file1.close()


