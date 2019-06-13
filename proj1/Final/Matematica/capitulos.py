l1 = ['Pacotes $\LaTeX$','Caracteres Especiais', 'Listas e Tabelas','Modo Matemática','Criação Gráficos', 'Projetos com $\LaTeX$: Comando input','Referências a Documentos Externos', 'Inclusão de Imagens','Fontes e Linguagens']
l2 = ['Como Utilizar o Modo de Matemática','Comandos mais Comuns do Modo de Matemática','Caracteres Especiais do Modo de Matemática','Frações',
'SuperScripts e SubScripts','Radicais','Integrais, Somatórios, Produtórios e Limites','Indexação de Equações','Matrizes','Chavetas','Listas','Tabelas','Prós',
'Contras','WYSIWYM','WYSIWYG']
for i  in l2:
    a = i.replace(' ','').lower().replace('ç','c').replace('ã','a').replace('á','a').replace(':','').replace('\\','').replace('ê','e').replace('$','').replace('õ','o').replace('ó','o')
    file1 = open(a + '.html','w+')
    file1.write("""
	<!DOCTYPE html>
	<html lang="pt">
	<meta charset="utf-8">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<div id="importsInit"></div>
	<script>$(document).ready(function(){$("#importsInit").load("../Includables/importsInit.html");});</script>

	<body>
		<div id="wrapper">
			<header id="navBar">
				<script>$(document).ready(function(){$("#navBar").load("../Includables/navBar.html");});</script>
			</header>
		</div>
		<a href="#" class="scrollup"><i class="icon-chevron-up icon-square icon-48 active"></i></a>
		""" +"Escrever aqui o conteudo do capitulo" + i + """
		<div id="importsEnd"></div>
		<script>$(document).ready(function(){$("#importsEnd").load("../Includables/importsEnd.html");});</script>
	</body>
	</html>
	""")
    file1.close()



