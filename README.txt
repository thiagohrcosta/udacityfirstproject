#Projeto: Site de trailer de filmes 
#Institui��o: Udacity
#Curso: NanoDegree - Desenvolvimento Web Full Stack

#Autor: Thiago H.R. Costa - 2018

==================================>>>RESUMO<<<===============================================
Primeiro projeto apresentado no Curso NanoDegree - Desenvolvimento Web da Udacity, o presente
site, foi desenvolvido incrementando os requisitos originalmente fixados pela Udacity para a
elabora��o do projeto, tendo como base a permiss�o para que o aluno pudesse desenvolver suas
pr�prias ideias.

=============================>>> TECNOLOGIAS UTILIZADAS <<< =================================
No desenvolvimento do presente projeto foram utilizadas as tecnologias: HTML, CSS e Python. Igualmente utilizou-se o Photoshop para o tratamento breve da imagem de logo. 

=============================>>> O QUE FOI ADICIONADO <<< ===================================
O conte�do original n�o continha menu, slide ou rodap�, desta forma, fora acrescentado no 
c�digo HTML inserido dentro do arquivo 'fresh_tomatoes.py' o c�digo HTML respons�vel para a
cria��o destas tr�s novas adi��es. De igual forma, houve manipula��o via CSS do c�digo, de 
forma a ajustar as mudan�as com o conte�do HTML.  Para tanto, usou-se a edi��o via CSS por 
classe(".") e ID("#" - Carousel, neste caso dispensou-se conte�do interno uma vez que o c�digo
por si s� se adaptou perfeitamente ao conte�do HTML). Foi criada tamb�m a classe Movie no 
arquivo media.py de forma a suportar os dados apresentados na p�gina principal.

==========================>>> MUDAN�A - VERS�O 1.0 <<< ======================================
1. Body{
	A cor do backround foi alterada para preto no html;

2. .movie-title{
	Foi inserido o comando ''color:white'' para criar contraste com o novo background 
	definido no body;

3. Logo
	Foi adicionada uma imagem ''logo.png'' como logo do site, alterando o conte�do de 
	texto original por uma imagem .png hospedada na pasta interna /img. 

4. Menu
	O projeto original n�o exigia menu. Neset projeto contudo, foi adicionado um menu
	simples, usando listas n�o ordenadas para criar os menus #TV Show Trailer, #Netflix
	Original Trailer, #Amazon Prime Trailer, #Login.
	Estes quatro menus s�o apenas para prop�sitos visuais, n�o possuem c�digo atrelado.
	O ''search'' tamb�m foi inserido, mas assim como os quatro menus acima, n�o possui
	qualquer c�digo atrelado, sendo apenas para efeitos de ''front-end'' e visuais.

5. Pasta /img
	Para suportar a inser��o do logo e do slide carousel, foi criada uma pasta /img
	vinculada ao arquivo HTML de forma que o arquivo possa buscar as imagens na pasta
	("img src="") e exib�-las em sua p�gina. 	

6. O slide Carousel
	Foi inserido o slide para criar um efeito visual mais amig�vel no site. Sendo tamb�m
	ajustado o "body{padding-top:}". Houve ma redu��o de 80px para 52px;

7. Footer
	Foi criado um footer com o nome do autor deste projeto, informa��o sobre o curso e 
	institui��o vinculada. 

8. Autor
	Thiago H.R. Costa - Criado em 19/11/2018 como primeiro projeto para o curso da Udacity
	NanoDegree de Desenvolvimento Web Full Stack
 
========================>>> COMO UTILIZAR OU ABRIR O ARQUIVO <<<==============================

DOWNLOAD: Para ambos os modos de acesso abaixo, o usu�rio dever� efeutar o download do arquivo
disponibilizado, e em seguida, extrair seu conte�do para uma pasta qualquer desejada.

ACESSO VIA PYTHON: 

O acesso via Python deve ser realizado da seguinte forma ap�s extrair o conte�do do arquivo: 

a) Iniciar o IDLE (Python GUI) em seu computador;
b) Clicar em "File" e posteriormente em "Open";
c) Abrir o arquivo "entertainment_center.py";
d) Uma vez aberto o arquivo, clicar em "Run" e "Run Module", ou simplesmente apertar F5;
e) O Python automaticamente abrir� o seu navegador com a p�gina do Fresh Tomatoes Movie Trailer.

ACESSO DIRETO VIA COMPUTADOR - SEM PYTHON

Caso o usu�rio n�o tenha o Python instalado em seu computador, dever� seguir as seguintes 
instru��es ap�s efetuar o download do arquivo e extra�-lo para uma pasta desejada dentro de seu
computador. 

a) Acessar a pasta de destino;
b) Procurar pelo arquivo "fresh_tomatoes.html"
c) Clicar neste arquivo duas vezes, ou clicar uma vez com o bot�o direito e abr�-lo no navegador
   desejado.
d) O arquivo ser� automaticamente aberto no navegador padr�o ou escolhido pelo usu�rio, exibindo
   o site Fresh Tomatoes Movie Trailer