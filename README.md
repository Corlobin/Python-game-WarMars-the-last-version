## War Mars ##

**War Mars** é um jogo que está sendo desenvolvido para Windows/Linux/MacOS na linguagem Python.

Autor: Antonio (anribrasil@gmail.com)

### Seções
1. Padrão de projetos
2. Padrões comportamentais
3. Cadeia de Responsabilidade
4. Iterador
5. Mediador
6. Observador
7. Estado
8. Estratégia
9. Visitador

### 1. Padrões de projeto ###

Padrões de projeto é uma solução geral reutilizável para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software. [Wikipedia, 2015]. 

### 2. Padrões comportamentais


Os padrões comportamentais são relacionados aos comportamentos dos objetos.

### 3. Cadeia de Responsabilidade

A cadeia de responsabilidade serve para evitar o acoplamento de uma requisição com os receivers que irão tratar a requisição. Ela então passa
por cada objeto até tratar a requisição. 

Não houve necessidade de implementação deste padrão de projetos no trabalho pois sua implementação não foi necessária.

### 4. Iterador

O Iterador foi representado no trabalho por meio do acesso aos objetos sem saber a representação interna. Abaixo segue um trecho do codigo onde o iterador teve
utilidade no trabalho. 
![Iterator]( https://github.com/Corlobin/WarMars-4.0/blob/master/Padrao%20Iterator.png?raw=true)

### 5. Mediador
O mediador define um objeto que encapsula as interações de um conjunto de objetos. No trabalho, o nosso mediador foi nada mais do que o Controlador do Menu, ele foi o responsavel por realizar as iterações dos objetos restantes, mostrando a tela respectiva de cada Estado do jogo. Abaixo segue o diagrama do padrão Mediador implementado no Projeto.

![Mediador](https://raw.githubusercontent.com/Corlobin/WarMars-4.0/master/Diagrama_Mediador.jpg)

### 6. Observador

O observador define a dependência de um objeto perante outros objetos, e assim, quando o estado de um objeto é mudado, os objetos dependentes são notificados e atualizados automaticamente. No trabalho, não houve a necessidade de implementação do padrão observador porque eu não precisei observar o comportamento de outro objeto;

### 7. Estado

O padrão permite que o objeto mude seu comportamento conforme o seu estado. Não houve implementação do padrão Estado no projeto. No jogo foi implementado para modificar o estado do helicoptero, lhe dando mais balas e munições para ele metralhar os inimigos! :)

![State](https://raw.githubusercontent.com/Corlobin/WarMars-4.0/master/PadraoState.png)

### 8. Estratégia, Visitador

Não houve implementação do padrão Estratégia e Visitador. Sem necessidade de utilização no codigo.

### 10. Memento

Foi implementado caso acontecesse algum problema com relação ao jogador. 

![Memento](https://github.com/Corlobin/WarMars-4.0/blob/master/Memento.png?raw=true)




