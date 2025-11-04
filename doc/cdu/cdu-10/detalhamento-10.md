# CDU10. Nome.

- **Ator principal**:Usuário (Cliente/Visitante) — um cliente navegando pelo catálogo
- **Atores secundários**: Sistema Web (Front-end), Controlador de Produtos (ProductController), Serviço de Produtos (ProductService), Repositório/Banco de Dados (ProductRepository), Serviço de Categorias/Marcas (CategoryService/BrandService)
- **Resumo**:Permitir que o usuário aplique critérios de filtro (categoria, preço, faixa de preço, marca, avaliação, disponibilidade, atributos) ao catálogo de produtos para refinar a lista exibida.
- **Pré-condição**:O usuário está na página de catálogo/produtos ou em uma busca prévia; o catálogo contém produtos cadastrados.
- **Pós-Condição**:O sistema exibe a lista de produtos que satisfaçam os critérios de filtro aplicados; paginação e ordenação são mantidas.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 -Usuário acessa a página de catálogo/lista de produtos.

| Sistema carrega a lista padrão de produtos (primeira página) e mostra painel de filtros. |  
| 2 -Usuário escolhe critérios de filtro (ex.: categoria, marca, preço mínimo/máximo, avaliação mínima, disponibilidade) e clica em "Aplicar filtros".

| Sistema valida os critérios, monta uma consulta/objeto FilterCriteria e envia para ProductService.
| 3 - Usuário aguarda resultados.

3 - ProductService consulta ProductRepository com os filtros, recebe lista filtrada, aplica ordenação e paginação (se necessário).
4 - Usuário visualiza a lista filtrada e pode selecionar produto ou ajustar filtros.

4 - Sistema apresenta resultados filtrados e atualiza contadores (ex.: "120 produtos encontrados").

## Fluxo Alternativo I - ...
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - Usuário aplica filtros muito restritivos que retornam 0 produtos.|Sistema detecta lista vazia e exibe mensagem "Nenhum produto encontrado" e sugestões (limpar filtros, ampliar faixa de preço, ver produtos relacionados).|  
| | 1.2 - Usuário escolhe limpar filtros ou alterar critérios.|Sistema recarrega produtos de acordo com novos critérios ou com a lista padrão.

## Fluxo Alternativo II - ...
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - Usuário informa valores inválidos (ex.: preço mínimo > preço máximo).|
Sistema valida e exibe erro inline (ex.: "Preço mínimo não pode ser maior que o máximo").|  
| | 2.2 - Usuário corrige o valor e reaplica.
    Sistema processa normalmente.

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...
