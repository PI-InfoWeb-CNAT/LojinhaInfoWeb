# CDU006. Realizar pré-venda de produto

- **Ator principal**: Comprador
- **Atores secundários**: Não possui	 
- **Resumo**: O comprador realiza a pré-venda de um produto que ainda não está disponível em estoque. O sistema permite o pagamento antecipado e reserva o item para o comprador, garantindo que o produto seja enviado assim que estiver disponível.
- **Pré-condição**: O comprador deve estar autenticado no sistema e o produto deve estar disponível para pré-venda.
- **Pós-Condição**: O pagamento é registrado, o produto é reservado e o comprador recebe a confirmação da pré-venda.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |
| 0 -  O comprador acessa a página de um produto disponível para pré-venda.| | 
| 1 - O comprador seleciona a opção “Realizar pré-venda”. | |  
| | 2 - O sistema solicita as informações de pagamento e confirmação da reserva. | 
| 3 - O comprador confirma o pagamento antecipado. | | 
| | 4 - O sistema processa o pagamento. | 
| 5 - O sistema registra a reserva do produto em nome do comprador. | | 
| | 6 - O sistema exibe a mensagem de confirmação de pré-venda e o prazo estimado de envio. | 

## Fluxo Alternativo I - Pagamento não autorizado 
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O comprador informa os dados de pagamento, mas a transação não é autorizada. | |  
| | 1.2 - O sistema exibe mensagem informando que o pagamento não foi aprovado e solicita nova tentativa ou método alternativo. |

(retorna ao passo 2 do fluxo principal)

## Fluxo Alternativo II - Produto Indisponível para pré-venda
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O comprador tenta realizar a pré-venda de um produto que não está mais disponível para reserva. | |  
| | 2.2 - O sistema exibe mensagem informando que o produto esgotou e não pode mais ser reservado. |  

## Fluxo Alternativo III - Cancelamento pelo comprador
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 3.1 - O comprador decide cancelar a pré-venda antes do envio do produto. | |  
| | 3.2 - O sistema registra o cancelamento, atualiza o status do pedido e agenda o estorno do pagamento conforme as políticas da loja. |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...
