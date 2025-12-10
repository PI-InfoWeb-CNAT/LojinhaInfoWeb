# Modelo de Domínio

## 1. Diagrama de Classes Conceituais

![Modelo de Domónio do Sistema](./imgs/dominio.png)

## 2. Glossário

Termo | Explicação
----- | ----------
Produto | Armazena das informações dos produtos disponíveis para venda
Categoria | Possibilita classificar os produtos pelos tipos específicos, tais como: camisas, bonés, botons, adesivos, etc.
Reserva | Representa a reserva de um produto específico por um usuário
FilaReserva | Responsável por gerenciar o conjunto das reservas de um dado produto
Compra | Inicialmente representa um carrinho de compras que pode ser transformado no registro de uma compra
ItemDeCompra | Representa um item específico de uma compra, definindo uma quantidade

## 3. Diagrama de Estados - Classe Compra

![](./imgs/estados/classe_Compra.png)