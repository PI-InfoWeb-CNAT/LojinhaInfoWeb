# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :--: | :----: | :-------: | :-----: |
| 22/09/25 | 1.0 | Versão inicial | Fellipe Aleixo |
| 29/09/25 | 1.1 | Conclusão da primeira versão | Fellipe Aleixo |
| | | | |

## 1. Objetivo do projeto

Implementação da um sistema Web (exemplo) que irá servir para comercialização de produtos relacioados ao curso Técnico Integrado em Informática para Internet do campus Natal Central do IFRN. Através do sistema serão comercializados produtos como camisas, bonés, canecas, botons, adesivos, etc. Serão ofertados descontos especiais para alunos/servidores ligados ao curso e ao IFRN. 


## 2. Descrição do problema

|    |    |
| -- | -- |
| **Problema** | Ausência de um canal próprio para a comercialização de produtos referentes ao curso de InfoWeb |
| **Afeta** | Alunos e professores ligados ao curso |  
| **Impacta** | O não desenvolvimento da identidade dos alunos e professores com o curso |
| **Solução** | Desenvolvimento de uma sistema Web para comercialização de produtos ligados ao curso | 

## 3. Descrição dos usuários 

| Nome | Descrição | Responsabilidade |
| :--: | :-------: | :--------------: |
| Administrador | administrador do sistema | validar o cadastro de usuários e definir permissões |
| Comissão da lojinha | representantes dos alunos matriculados | gerenciar o catálogo dos produtos ofertados |
| Aluno InfoWeb | aluno matriculado no curso | pesquisar produtos e realizar compras |
| Aluno IFRN | aluno matriculado no IFRN | pesquisar produtos e realizar compras |
| Professor InfoWeb | professor ministrando disciplina para o curso | pesquisar produtos e realizar compras |
| Servidor IFRN | servidor do IFRN | pesquisar produtos e realizar compras |

## 4. Descrição do ambiente dos usuários

TODOS os usuários que irão acessar ao sistema o farão através de um computador pessoal (muito provavelmente um notebook), porém o acesso através do celular também deverá acontecer. 

## 5. Principais necessidades dos usuários

1. **Administrador**
   - atribuir as permissões aos demais usuários;
1. **Comissão da lojinha**
   - gerenciar o catálogo dos produtos oferecidos;
   - gerenciar as entregas dos itens comprados;
1. **Alunos/servidores (compradores)**
   - pesquisar os produtos do catálogo;
   - selecionar produtos que deseja comprar;
   - finalizar compra de produtos.

## 6. Alternativas concorrentes

1. Mercado Livre
   - usuários cadastrados na plataforma podem ofertar itens OU comprar itens ofertados por outros usuários;
   - comercializa qualquer tipo de itens, sem nincho específico;
   - Solução de broker de pagamento integrada à plataforma - MercadoPago;
1. OLX
   - oferta itens para venda, aluguel ou até mesmo compra;
   - usuários cadastrados na plataforma podem ofertar os seus próprios itens;
   - também trabalha com todo o tipo de nprodutos e não de um nincho específico.

## 7. Regras de Negócio

| ID  | Regra | Dscrição |
| :-: | :---: | :------: |
| RN01 | Carrinho de compras dura até dois dias | Carrinho de compras terá "tempo de vida" máximo de dois dias |
| RN02 | Reservas valem por duas semanas | As reservas  de produtos serão respeitadas até um limite máximo duas semanas |
| RN03 | Fila de espera de produtos | Itens reservados que não foram comprados no prazo são disponibilizados para o primeiro da fila de espera |
| RN01 | Desconto aluno InfoWeb | Desconto de 40% para alunos InfoWeb |
| RN02 | Desconto DIATINF | Desconto 30% para alunos/servidores DIATINF |
| RN03 | Desconto IFRN | Desconto de 15% para alunos/servidores IFRN |

## 8. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :----: | :--: | :-------: | :--------: |
| RF01 | Gerenciamento de produtos | Funções de inclusão, alteração, listagem e remoção de produtos | alta |
| RF02 | Cadastro e autenticação de usuários | Auto-cadastro de usuário, com validação pelo administrador, além de login/logout no sistema | média |
| RF03 | Busca e filtragem de produtos | Busca de produtos por critérios específicos (nome, categoria, preço, etc.) | alta |
| RF04 | Carrinho de compras | Possibilidade para os usuáris irem adicionando os produtos do seu interesse em um carrinho de compras virtual | alta |
| RF05 | Registro de vendas | Possibilidade ao usuário de finalizar a compra dos produtos que adicionou ao carrinho de compras | alta |
| RF06 | Histórico de compras | Possibilidade para o usuário acessar todas as compras anteriores que realizou no sistema | baixa |
| RF07 | Gerenciamento de entregas | Gerenciar o processo entrega dos itens adiquiridos por um dado usuário | médio |
| RF08 | Gerenciamento reserva de produtos | Possibilitar que usuários possam reservar produtos, para compra futura | média |
| RF09 | Gerenciamento de fila de espera | Possibilidade de registrar o interesse de um usuário por um produto que não está disponível (em falta no estoque ou reservado) | média |


## 9. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :--: | :-------: | :-------: | :-----------: |
| NF01 | Implementação em Django/Python | Utilização do framework Django,na linguagem Python | implementação | obrigatório |
| NF02 | Integração com API PagSeguro | Possibilitar que compras sejam mediadas pela API do PagSeguro | implementação | desejável |
| NF03 | Criptografia de dados sensíveis | segurança | obrigatório |
| NF04 | Responsividade para dispositivos móveis | usabilidade | obrigatório |
| NF05 | Seguir normas de acessibilidade | usabilidade | desejável |

