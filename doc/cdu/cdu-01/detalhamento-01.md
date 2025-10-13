# CDU 01. Adicionar produto ao carrinho 

- **Ator principal**: Comprador.
- **Atores secundários**: não possui. 
- **Resumo**: Em uma tela onde um produto é visualizado, o comprador clica em um botão, associado a um produto específico, "adicionar ao carrinho". Adicionando o referido produto ao conjunto daqueles que deseja comprar.
- **Pré-condição**: produto devidamente cadastrado. Obs.: usuário não precisa estar logado para ter um carrinho de compras.
- **Pós-Condição**: produto adicionado ao carrinho de compras.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - visulizando um dado produto o comprador seleciona a opção "adicionar ao carrinho". | |  
| | 1 - o sistema adiciona o referido produto ao carrinho associao à sessão ativa |
| | 2 - o sistema exibe o carrinho de compras, com os itens já adicionados (o comprador poderá atualizar as quantidades) |

## Fluxo Alternativo I - Identificador de produto inválido
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 1.1 - o sistema exibe uma mensagem de "produto inválido" e ofere um link para o retor a listagem dos produtos | |  
| (fluxo finalizado) | |

## Fluxo Alternativo II - Sem estoque de produto
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 1.2 - o sistema exibe as informações do produto, informa a imporssibilidade de adicionar por falta de etoque |
| | 2.2 - o sistema exibe a opção de "reservar produto" |
| (fluxo finalizado) | |  

## Fluxo Alternativo III - Produto já no carrinho
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 1.2 - o sistema identifica que o produto já está no carrinho e incrementa a quantidade de 1 (um) |
| | (retorna ao passo 2 do fluxo principal) |
 
> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...