# CDU008 - Visualizar produto 

- **Ator principal**: Visitante e Comprador
- **Atores secundários**: Nenhum
- **Resumo**: Habilita ao usuário a possibilidade de visualizar os produtos e seus detalhes comercializados pela loja.
- **Pré-condição**: Haver produtos devidamente cadastrados e em status de ativo no sistema.
- **Pós-Condição**: O sistema permite que o usuário visualize os detalhes do produto desejado com suas especificações, em sua respectiva página.

## Fluxo Principal
|  Ator  | Sistema |
|:-------|:------- |
|1. O visitante acessa a página inicial da aplicação. | --- |
| 2. O visitante clica na seção de "Produtos”. | --- |
| --- |3. O sistema exibe a página com a lista de produtos.|
| 4.  O visitante clica em um card contendo o produto para detalhamento deste.| --- |
| --- | 5. O sistema recupera os dados registrados daquele produto. |
| --- | 6. O sistema mostra ao usuário o produto e suas especificações. |
| --- | 7. O sistema verifica o status de estoque do produto e exibe a informação. |
| 8. O visitante consegue visualizar e realizar outras funções desejadas. | --- | 

#### Fluxos Alternativos
### Fluxo 1 - Busca na barra de pesquisa
|  Ator  | Sistema |
|:-------|:------- |
|1. O visitante acessa a página inicial da aplicação. | --- |
|2. O visitante digita o nome do produto na barra de busca e dá enter. | --- |
| --- | 3. O sistema exibe a página com os resultados da busca. |
| (Continua a partir do passo 3 do fluxo principal) | --- |

### Fluxo 2 - Usuário acessa diretamente a URL da página do produto
|  Ator  | Sistema |
|:-------|:------- |
| --- | (Continua a partir do passo 5 do fluxo principal) |

#### 2.2. Fluxo de exceção 
|  Ator  | Sistema |
|:-------|:------- |
| 1. O visitante acessa o link de um produto excluído. | --- |
| --- | 2. O sistema procura retornar os dados do produto e vê que foi excluído do banco de dados. |
| --- | 3. O sistema exibe uma página de erro e um botão para retornar à seção de produtos. |
| 4. O usuário clica no botão e retorna a outra página, sem sucesso. | --- |

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...
