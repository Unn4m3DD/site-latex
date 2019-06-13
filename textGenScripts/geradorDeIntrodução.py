file0 = open('introdução','w')
for i  in ['Estrutura de Comandos','Criação Macros','Pacotes \LaTeX','Caracteres Especiais', 'Listas e Tabelas','Disposição e Organização de Texto','Modo Matemática','Criação Gráficos', 'Projetos com \LaTeX: Comando input','Referências a Documentos Externos', 'Inclusão de Imagens','Fontes e Linguagens']:
    a = i.replace(' ','').lower().replace('ç','c').replace('ã','a').replace('á','a').replace('\\','').replace('ê','e')
    file0.write("\nNa \\autoref{chap."+a+"}\n")
file0.close()
