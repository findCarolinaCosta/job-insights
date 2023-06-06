# Job Insights

# Entregáveis

<details>
  <summary><strong>👨‍💻 O que deverá foi desenvolvido</strong></summary><br />
  <p align="center">
    <img src="/.images/job.png" alt="Logo Aplicação" width="300"/>
  </p>

  Neste projeto foi implementado análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Você também foi escrito testes para a implementação de uma análise de dados. Por fim, como bônus, você será feito o desafio de escrever uma rota e view para um recurso novo usando Flask!

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponibilizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades a trabalhadas:

<ul>
    <li>Utilização do terminal interativo do Python.</li>
    <li>Utilização de estruturas condicionais e de repetição.</li>
    <li>Utilização de funções built-in do Python.</li>
    <li>Utilização de tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrita de funções.</li>
    <li>Escrita de testes com Pytest.</li>
    <li>Escrita de módulos e importação em outros códigos.</li>
  </ul>
</details>

# Orientações

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />

```
  Legenda:
  🔸Arquivos pré existentes, que não podem ser alterados para avaliação.
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── src
  │   ├──🔸app.py
  │   ├──🔸brazilian_jobs.py
  │   ├──🔸counter.py
  │   ├──🔹insights.py
  │   ├──🔸jobs.csv
  │   ├──🔹jobs.py
  │   ├──🔸more_insights.py
  │   ├──🔹routes_and_views.py
  │   ├──🔸sorting.py
  │   └── templates
  │       ├──🔸base.jinja2
  │       ├── includes
  │       │   └──🔸nav.jinja2
  │       ├──🔸index.jinja2
  │       ├──🔸job.jinja2
  │       └──🔸list_jobs.jinja2
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔹test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_insights.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
```
</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, foi utilizo neste projeto o linter `Flake8`.
  Para o código estar alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

```bash
  python3 -m flake8
```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **criar o ambiente virtual**

```bash
  $ python3 -m venv .venv
```

2. **ativar o ambiente virtual**

```bash
  $ source .venv/bin/activate
```

3. **instalar as dependências no ambiente virtual**

```bash
  $ python3 -m pip install -r dev-requirements.txt
```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate".

  O arquivo `dev-requirements.txt` contém todas as dependências que são utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  `<strong>`Executação dos testes`</strong>`

```bash
  $ python3 -m pytest
```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
  python3 -m pytest -s -vv
```

  Para executar apenas um arquivo de testes basta executar o comando:

```bash
  python3 -m pytest tests/nomedoarquivo.py
```

  Para executar apenas uma função de testes basta executar o comando:

```bash
  python3 -m pytest -k nome_da_func_de_tests
```

  Para os testes pararem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

```bash
  python3 -m pytest -x tests/test_jobs.py
```

  Para executar um teste específico de um arquivo, basta executar o comando:

```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

<p align="center">
    <img src="/.images/flask-logo.png" alt="Logo Flask" width="200"/>
  </p>

  Além dos testes com o Pytest, é possível rodar a aplicação flask para visualizar no navegador o resultado do desenvolvimento das funções.
  Para isso, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`.

<p align="center">
    <img src="/.images/sistema.png" alt="Tela Aplicação" width="800"/>
  </p>

</details>

# Requisitos Obrigatórios

## 1 - Implementação da função `read`

> **Implementado em:** src/jobs.py

Para começarmos a processar os dados, antes carregá-los em nossa aplicação. Esta função é responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- A função recebe um _path_ (uma string com o caminho para um arquivo).
- A função abre o arquivo e ler seus conteúdos.
- A função trata o arquivo como CSV.
- A função retorna uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  Se o conteúdo do arquivo for:

```
nome,cidade,telefone
Ana,Curitiba,1111111
Bernardo,Santos,999999
```

  O retorno da função deverá ser:

```python
  [
    {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
    {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
  ]
```

</details>

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando estas funções através do comando <code>python3 -i src/jobs.py</code> e invocar a função utilizando diferentes _paths_.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função abre o arquivo passado como parâmetro
- A função retorna uma lista de dicionários
- A função retorna a quantidade correta de itens na lista
- Nos dicionários retornados pela função, as chaves correspondem aos cabeçalhos do arquivo

</details>

## 2 - Implementação da função `get_unique_job_types`

> **Implementado em:** `src/insights.py`

Após ter como carregar os dados, foi feito a extração das informação. Primeiro, foi identificado quais tipos de empregos existem.

- A função recebe o _path_ do arquivo csv com os dados.
- A função invoca a função `jobs.read` com o _path_ recebido para obter os dados.
- A função retorna uma lista de valores únicos presentes na coluna `job_type`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função desconsidera valores vazios

</details>

## 3 - Implementação da função `get_unique_industries`

> **Implementado em:** `src/insights.py`

Da mesma forma, é possível identificar quais indústrias estão representadas nesse conjunto de dados.

- A função obtém os dados da mesma forma que o requisito 2.
- A função retorna uma lista de valores únicos presentes na coluna `industry`.
- A função desconsidera valores vazios

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna a quantidade correta de valores
- A função retorna os valores corretos

</details>

## 4 - Implementação da função `get_max_salary`

> **Implementado em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Com essa função é possível encontrar o maior valor de todas as faixas.

- A função obtém os dados da mesma forma que o requisito 2.
- A função ignora os valores ausentes.
- A função retorna *um valor inteiro* com o maior salário presente na coluna `max_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna o valor correto

</details>

## 5 - Implementação da função `get_min_salary`

> **Implementado em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Com essa função é possível encontrar o menor valor de todas as faixas.

- A função obtém os dados da mesma forma que o requisito 2.
- A função ignora os valores ausentes.
- A função retorna *um valor inteiro* com o menor salário presente na coluna `min_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna o valor correto

</details>

## 6 - Implementação da função `filter_by_job_type`

<p align="center">
  <img src="/.images/filter.png" alt="Contagem" width="400"/>
</p>

> **Implementado em:** `src/insights.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, foi implementado um filtro.

- A função recebe uma lista de dicionários `jobs` como primeiro parâmetro.
- A função recebe uma string `job_type` como segundo parâmetro.
- A função retorna uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função retorna os valores na ordem correta
- A função retorna uma lista vazia para `job_types` ausentes nos `jobs` recebidos

</details>

## 7 - Implementação da função `filter_by_industry`

> **Implementado em:** `src/insights.py`

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Para isso foi implementado esse filtro também.

- A função recebe uma lista de dicionários `jobs` como primeiro parâmetro.
- A função recebe uma string `industry` como segundo parâmetro.
- A função retorna uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função retorna os valores na ordem correta
- A função retorna uma lista vazia para `job_types` ausentes nos `jobs` recebidos

</details>

## 8 - Implementação da função `matches_salary_range`

> **Implementado em:** `src/insights.py`

O aplicativo precisa filtrar os empregos por salário também. Como uma função auxiliar, foi implementado `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Também é conferido se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- A função recebe um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`.
- A função recebe um inteiro `salary` como segundo parâmetro.
- A função lança um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- A função retorna `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função retorna o booleano correto
- A função lança um `ValueError` se o valor de `min_salary` for maior que o valor de `max_salary`
- A função lança um `ValueError` se as chaves `min_salary` ou `max_salary` tiverem valores não numéricos
- A função lança um `ValueError` se o parâmetro `salary` tiver valor não numérico
- A função lança um `ValueError` se as chaves `min_salary` ou `max_salary` estiverem ausentes no dicionário

</details>

## 9 - Implementação da função `filter_by_salary_range`

> **Implementado em:** `src/insights.py`

Foi implementado o filtro propriamente dito. Para esta filtragem, na função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- A função recebe uma lista de dicionários `jobs` como primeiro parâmetro.
- A função recebe um inteiro `salary` como segundo parâmetro.
- A função ignora os empregos com valores inválidos para `min_salary` ou `max_salary`.
- A função retorna uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função retorna os valores na ordem correta
- Empregos onde as chaves `min_salary` ou `max_salary` tiverem valores não numéricos devem ser ignorados
- Empregos onde o valor de `min_salary` for maior que o valor de `max_salary` devem ser ignorados

</details>

## 10 - Implementação de um teste para a função `count_ocurrences`

> **Implementado em:** `tests/counter/test_counter.py`

<p align="center">
    <img src="/.images/flask.png" alt="Imagem sobre contar ocorrências" width="600"/>
  </p>

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra *Python* e *Javascript* nos dados e, para isso, temos a implementação em `src/counter.py`. Durante o desenvolvimento, ocorreram alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da entrega, no entanto, e não corrermos riscos, precisaremos de *testes automatizados* que garantam isso!

O nome do teste é `test_counter`, e ele garante que atenda as seguintes especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`src/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada.
- Garante que a função retorna corretamente a quantidade de ocorrências da palavra solicitada
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas

<details>
  <summary>
    <b>📌Como o teste é testado</b>
  </summary>
  Um teste irá avaliar se o <strong>seu teste feito</strong> está passando conforme seu objetivo e confirmará se ele está falhando em alguns casos que deve falhar.
  Para os testes que devem falhar, o requisito é considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code> ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- O teste rejeita implementações que não retornam a quantidade de palavras corretamente.
- O teste aprova implementações corretas.
- Se o teste não é um falso positivo, ou seja, teste que passa sem realmente testar o código.

</details>

## 11 - Implementação um teste para a função `read_brazilian_file`

> **Implementado em:** `tests/brazilian/test_brazilian_jobs.py`

A empresa cliente analisa relatórios em inglês, porém agora ela quer expandir seus negócios aqui para o Brasil e deseja analisar relatórios em português também. No entanto, as chaves do `dict` que usamos pra organizar os dados **devem** continuar em inglês. Ou seja: para gerar o relatório, deveremos ler as chaves em português e traduzi-las para inglês para povoar os nossos dados.

Já foi implementou a função `read_brazilian_file`, na qual é adotado a estratégia de chamar o método original `read`, que implementado no `requisito 1`, e depois é traduzido as chaves para o inglês. Para esse requisito foi criado testes para ter certeza que esta tudo certo!

O nome deste teste é `test_brazilian_jobs`, e ele garante que atenda as seguintes especificações:

- **Chama** a função `read_brazilian_file` e ela deve receber um parâmetro:
  - `path` que é uma string com o caminho do arquivo csv em português (`tests/mocks/brazilians_jobs.csv`);
  - Retorna uma lista de dicionários com as chaves em inglês

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  O dicionário: <code>{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}</code>

  Deve ser traduzido para: `<code>`{"title": "Maquinista", "salary": "2000", "type": "trainee"}`</code>`

</details>
<details>
  <summary>
    <b>📌Como o teste é testado</b>
  </summary>
  Um teste avalia se o <strong>teste implementado</strong> está passando conforme seu objetivo e confirmará se ele está falhando em alguns casos que deve falhar.
  Para os testes que são esperado que falhe, o requisito será considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code> ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

<details>
  <summary>
    <b>🤖 O que é verificado pelo teste</b>
  </summary>

- O teste rejeita implementações que não retornam as chaves traduzidas corretamente.
- O teste aprova implementações corretas.
- Se o teste não é um falso positivo, ou seja, teste que passa sem realmente testar o código.

</details>

## 12 - Implementação um teste para a função `sort_by`

> **Implementado em:** `tests/sorting/test_sorting.py`

Por fim, a pessoa usuária pode escolher um critério de ordenação para exibir os empregos. Já existe implementação para essa ordenação em `src/sorting.py`, mas queremos ter certeza de que ela funciona e, principalmente, que não deixará de funcionar conforme vamos implementando novos recursos. Precisamos então escrever um *teste*!

Esse teste é chamado de `test_sort_by_criteria` e garante que a função funciona segundo esta especificação:

- A função `sort_by` recebe dois parâmetros:
  - `jobs` uma lista de dicionários com os detalhes de cada emprego;
  - `criteria` uma string com uma chave para ser usada como critério de ordenação.
- O parâmetro `criteria` deve ter um destes valores: `min_salary`, `max_salary`, `date_posted`
- A ordenação para `min_salary` deve ser crescente, mas para `max_salary` ou `date_posted` devem ser decrescentes.
- Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.

<details>
  <summary>
    <b>📌Como o teste é teste</b>
  </summary>
  O <strong>teste</strong> é avaliado se o <strong>teste implementado</strong> está passando conforme seu objetivo e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code> ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- O teste rejeita implementações que não ordenam corretamente.
- O teste rejeita implementações que não ordenam em ordem crescente quando o critério é `min_salary`.
- O teste aprova implementações corretas.
- Se o teste não é um falso positivo, ou seja, teste que passa sem realmente testar o código.

</details>

---

# Requisitos Bônus

## 13 - (`Bônus`) Implementação de uma página de um job

> **Implementado em:** `src/routes_and_views.py`

Foi testado o quanto se consegue aprender de Flask apenas vendo como foi feito as páginas de `index` e de `jobs`, e tentar criar uma página que é exibido todas as informações de um job em específico,

- A função é decorada com a rota `/job/<index>`.
- A função recebe um parâmetro `index`.
- A função chama a `read` para ter uma lista com todos os jobs.
- A função chama a `get_job`, declarada no arquivo `src/more_insights.py`, para selecionar um job específico pelo `index`.
- A função renderiza o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Após criar a view, na página que lista os jobs, aparecem links para jobs específicos nos números que identificam cada job. Ao clicar em um destes links, deve ser levado a uma página que lista todas as informações do job.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo teste</b>
  </summary>

- A rota `/job/<index>` existe.
- A view `job` existe no arquivo `src/routes_and_views.py` e recebe o parâmetro `index` (e somente ele).
- A página de cada um dos jobs deve retornar o status code 200.
- A página de um job específico (escolhido previamente) deve retornar o HTML exato esperado.

</details>
