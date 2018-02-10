# hashprojectpython

#HashTabFoldMethodForStr :
Este programa utiliza o comando ord() do Python para transformar a string que será inserida em um codigo numérico
Depois, este codigo é dividido em pedaços iguais para se realizar o método de dobra com ele, somando os pedaços
Depois, o valor resultante da soma é dividido pelo valor do tamanho da tabela Hash (neste caso, sendo representada por uma lista),
e seu resto será a chave para colocar o item no slot correspondente ao número da chave

#HashTabMidSquare :
Este programa funciona de forma semelhante ao programa acima, com a única diferença sendo o método que ele utiliza
Neste caso, ele utiliza o método da multiplicação (ou meio do quadrado), onde se eleva ao quadrado o item e se usa 
uma quantidade r de itens do meio do numero
Depois, esse numero que foi selecionado será dividido pelo tamanho da tabela, eseu resto será a chave para colocar o item no slot correspondente ao número da chave

O.B.S.: Para solucionar problemas de colisão, caso um slot já esteja ocupado por um item, o prgrama busca um slot vazio e posiciona 
o item nele, e sua chave passa a se tornar o índice deste slot
