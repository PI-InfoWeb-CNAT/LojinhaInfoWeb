# CDU 01. Adicionar produto ao carrinho 

- **Ator principal**: Comprador.
- **Atores secundários**: não possui.	 
- **Resumo**: Visualizando um dado produto, o comprador seleciona a opção "inserir ao carrinho", que adcionará o produto na lista daqueles que deseja comprar.
- **Pré-condição**: O produto está devidamente cadastrado e quantidade em estoque é maior que zero. Obs.: o usuário não necessita estar logado para ter carrinho de compra.
- **Pós-Condição**: Um item de compra relativo ao produto deve ter sido associado no carrinho de compras (entidade Compra).

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - Estando visualizando um dado produto o comprador seleciona a opção "inserir ao carrinho" | |  
| | 1 - o sistema adiciona o referido produto ao carrinho de compras associado à sessão |
| | 2 - o sistema apresenta os detalhes do carrinho de compras e seus itens, permitindo que o comprador altere as quantidades dos mesmos | 

## Fluxo Alternativo I - Identificador de produto inválido
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 1.1 - o sistema exibe uma mensagem de "produto inválido" e oferece uma possibilidade retornar à lista dos produtos |  
| (fluxo finalizado) | |

## Fluxo Alternativo II - Estoque de produto zerado
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 1.2 - o sistema exibe mensagem da impossibilidade de adição, dado não haver estoque do produto |   
| | 2.2 - o sistema dá a opção do comprador realizar a "reserva" do produto |
| (fluxo finalizado) | |  

## Fluxo Alternativo III - Produto já se encontra no carrinho
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 1.2 - O sistema incrementa (de um) a quantidade do referido produto no carrinho |   
| | (retorna ao passo 2 do fluxo principal) | 

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...