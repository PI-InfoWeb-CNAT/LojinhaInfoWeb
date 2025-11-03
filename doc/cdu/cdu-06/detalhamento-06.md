# CDU006. Realizar pré-venda de produto

- **Ator principal**: Comprador
- **Atores secundários**: Não possui	 
- **Resumo**: O comprador realiza a pré-reserva de um produto que ainda não está disponível para retirada ou envio imediato. O sistema registra a intenção de reserva e garante que o item será disponibilizado para o comprador assim que houver estoque.
- **Pré-condição**: O comprador deve estar autenticado no sistema e o produto deve estar liberado para pré-reserva.
- **Pós-Condição**: A pré-reserva é registrada no sistema, o comprador recebe confirmação da pré-reserva e o sistema posiciona o comprador na fila de reservas.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |
| 0 -  O comprador acessa a página de um produto disponível para pré-venda.| | 
| 1 - O comprador confirma a intenção de pré-reserva. | |  
| | 1.1 - O sistema recupera os dados do produto. | 
| | 1.2 - O sistema cria o registro de reserva vinculado ao comprador e ao produto. | 
| | 1.3 - O sistema insere o comprador na fila de reserva. | 
| | 2 - O sistema exibe mensagem informando que a pré-reserva foi registrada com sucesso. | 
| 3 - O comprador é redirecionado ao carrinho ou página de reservas. | | 

## Fluxo Alternativo I - Produto Indisponível para Pré-Reserva
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O comprador tenta pré-reservar um produto que não possui mais vagas de reserva. | |  
| | 1.2 - O sistema informa que não é mais possível reservar este produto. |

(retorna ao passo 2 do fluxo principal)

## Fluxo Alternativo II - Cancelamento da Pré-Reserva pelo Comprador
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - O comprador solicita o cancelamento da pré-reserva antes da disponibilidade do produto. | |  
| | 2.2 - O sistema remove o comprador da fila e atualiza o status da reserva. |   

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> <img width="482" height="320" alt="cdu 006" src="https://github.com/user-attachments/assets/8ae4d66f-2e0b-4eb9-ab9d-47f576601a1a" />

