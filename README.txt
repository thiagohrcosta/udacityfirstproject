#Projeto: Site de trailer de filmes 
#Instituição: Udacity
#Curso: NanoDegree - Desenvolvimento Web Full Stack

#Autor: Thiago H.R. Costa - 2018

==================================>>>RESUMO<<<===============================================
Primeiro projeto apresentado no Curso NanoDegree - Desenvolvimento Web da Udacity, o presente
site, foi desenvolvido incrementando os requisitos originalmente fixados pela Udacity para a
elaboração do projeto, tendo como base a permissão para que o aluno pudesse desenvolver suas
próprias ideias.

=============================>>> TECNOLOGIAS UTILIZADAS <<< =================================
No desenvolvimento do presente projeto foram utilizadas as tecnologias: HTML, CSS e Python. Igualmente utilizou-se o Photoshop para o tratamento breve da imagem de logo. 

=============================>>> O QUE FOI ADICIONADO <<< ===================================
O conteúdo original não continha menu, slide ou rodapé, desta forma, fora acrescentado no 
código HTML inserido dentro do arquivo 'fresh_tomatoes.py' o código HTML responsável para a
criação destas três novas adições. De igual forma, houve manipulação via CSS do código, de 
forma a ajustar as mudanças com o conteúdo HTML.  Para tanto, usou-se a edição via CSS por 
classe(".") e ID("#" - Carousel, neste caso dispensou-se conteúdo interno uma vez que o código
por si só se adaptou perfeitamente ao conteúdo HTML). Foi criada também a classe Movie no 
arquivo media.py de forma a suportar os dados apresentados na página principal.

==========================>>> MUDANÇA - VERSÃO 1.0 <<< ======================================
1. Body{
	A cor do backround foi alterada para preto no html;

2. .movie-title{
	Foi inserido o comando ''color:white'' para criar contraste com o novo background 
	definido no body;

3. Logo
	Foi adicionada uma imagem ''logo.png'' como logo do site, alterando o conteúdo de 
	texto original por uma imagem .png hospedada na pasta interna /img. 

4. Menu
	O projeto original não exigia menu. Neset projeto contudo, foi adicionado um menu
	simples, usando listas não ordenadas para criar os menus #TV Show Trailer, #Netflix
	Original Trailer, #Amazon Prime Trailer, #Login.
	Estes quatro menus são apenas para propósitos visuais, não possuem código atrelado.
	O ''search'' também foi inserido, mas assim como os quatro menus acima, não possui
	qualquer código atrelado, sendo apenas para efeitos de ''front-end'' e visuais.

5. Pasta /img
	Para suportar a inserção do logo e do slide carousel, foi criada uma pasta /img
	vinculada ao arquivo HTML de forma que o arquivo possa buscar as imagens na pasta
	("img src="") e exibí-las em sua página. 	

6. O slide Carousel
	Foi inserido o slide para criar um efeito visual mais amigável no site. Sendo também
	ajustado o "body{padding-top:}". Houve ma redução de 80px para 52px;

7. Footer
	Foi criado um footer com o nome do autor deste projeto, informação sobre o curso e 
	instituição vinculada. 

8. Autor
	Thiago H.R. Costa - Criado em 19/11/2018 como primeiro projeto para o curso da Udacity
	NanoDegree de Desenvolvimento Web Full Stack
 
========================>>> COMO UTILIZAR OU ABRIR O ARQUIVO <<<==============================

DOWNLOAD: Para ambos os modos de acesso abaixo, o usuário deverá efeutar o download do arquivo
disponibilizado, e em seguida, extrair seu conteúdo para uma pasta qualquer desejada.

ACESSO VIA PYTHON: 

O acesso via Python deve ser realizado da seguinte forma após extrair o conteúdo do arquivo: 

a) Iniciar o IDLE (Python GUI) em seu computador;
b) Clicar em "File" e posteriormente em "Open";
c) Abrir o arquivo "entertainment_center.py";
d) Uma vez aberto o arquivo, clicar em "Run" e "Run Module", ou simplesmente apertar F5;
e) O Python automaticamente abrirá o seu navegador com a página do Fresh Tomatoes Movie Trailer.

ACESSO DIRETO VIA COMPUTADOR - SEM PYTHON

Caso o usuário não tenha o Python instalado em seu computador, deverá seguir as seguintes 
instruções após efetuar o download do arquivo e extraí-lo para uma pasta desejada dentro de seu
computador. 

a) Acessar a pasta de destino;
b) Procurar pelo arquivo "fresh_tomatoes.html"
c) Clicar neste arquivo duas vezes, ou clicar uma vez com o botão direito e abrí-lo no navegador
   desejado.
d) O arquivo será automaticamente aberto no navegador padrão ou escolhido pelo usuário, exibindo
   o site Fresh Tomatoes Movie Trailer