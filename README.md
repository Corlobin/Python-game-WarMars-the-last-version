## War Mars ##

**War Mars** é um jogo que está sendo desenvolvido para Windows/Linux/MacOS na linguagem Python.


Autor: Antonio (anribrasil@gmail.com)

Para melhor visualização, o conteudo do trabalho 3 foi omitido, assim, você podera verificar apenas os padrões comportamentais. Você pode visualizar o conteud odo trabalho três clicando [aqui](corlobin.github.io/WarMars3.0)

### Seções
1. Padrões comportamentais
2. Cadeia de Responsabilidade
3. Mediador
4. Observador
5. Estado
6. Estratégia
7. Visitador
8. Sonar


### 1. Padrões de projeto ###

Os padrões comportamentais são relacionados aos comportamentos dos objetos.

### 3. Mediador
O mediador define um objeto que encapsula as interações de um conjunto de objetos. No trabalho, o nosso mediador foi nada mais do que o Controlador do Menu, ele foi o responsavel por realizar as iterações dos objetos restantes, mostrando o controlador respectiva de cada Estado do jogo. Por exemplo, caso eu necessitasse de mostrar o cenário do jogo, eu deveria então haver uma interação para o Controlador respectivo do Cenário, que por sua vez, caso houvesse alguma modificação e/ou volta ao menu, ele retornaria ao menu. Foi implementado então esse padrão em Python, =abaixo segue o diagrama do padrão Mediador implementado no Projeto.

![Mediador](https://raw.githubusercontent.com/Corlobin/WarMars-4.0/master/Diagrama_Mediador.jpg)

### 4. Observador

O observador define a dependência de um objeto perante outros objetos, e assim, quando o estado de um objeto é mudado, os objetos dependentes são notificados e atualizados automaticamente. Esse padrão foi util para capturar eventos do teclado, ele já veio implementado na interface do pygame, toda vez que há uma modificação do teclado ele então sabe, e, possivelmente, adiciona a lista de keys pressionadas, o meu cadastro e login e o cenário, que utiliza dos teclados então, sabe quando as teclas são pressionadas. 

![Observer](https://raw.githubusercontent.com/Corlobin/WarMars-4.0/master/Observer%20example.png)

### 5. Estado

O padrão permite que o objeto mude seu comportamento conforme o seu estado. Não houve implementação do padrão Estado no projeto. No jogo foi implementado para modificar o estado do helicoptero, lhe dando mais balas e munições para ele metralhar os inimigos! :)

![State](https://raw.githubusercontent.com/Corlobin/WarMars-4.0/master/PadraoState.png)

### 6. Estratégia, Visitador, Cadeia

Não houve implementação do padrão Estratégia, Visitador ou cadeia. Sem necessidade de utilização no codigo.

### 7. Memento

Como não há seções criticas o memento deixou de ser implementado no trabalho, mas, posteriormente, caso haja alguma necessidade de implementação de algum local que faça alguma alteração com os dados do usuario, ele será atualizado. De qualquer forma o codigo foi gerado para possiveis utilizações. 

![Memento](https://github.com/Corlobin/WarMars-4.0/blob/master/Memento.png?raw=true)

### 8. Sonar

A avaliação do soonar anteriormente deu uma pontuação de 394. 
![Sonar](https://github.com/Corlobin/WarMars-4.0/blob/master/sonar3.png?raw=true)

Com as modificações a avaliação não subiu muito, passou para 395.
![Sonar](https://github.com/Corlobin/WarMars-4.0/blob/master/Sonar4.png?raw=true)



