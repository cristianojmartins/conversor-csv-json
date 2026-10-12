# Conversor CSV para JSON

## Sobre o projeto

Ferramenta desenvolvida em Python para converter dados de
arquivos CSV para o formato JSON.

O projeto faz parte de um portfólio de programação voltado
a serviços de tratamento, validação e organização de dados.

## Funcionalidades

- Leitura de arquivos CSV.
- Conversão de registros para JSON.
- Validação de campos dos registros.
- Identificação de campos ausentes.
- Identificação de campos extras.
- Identificação de nomes de colunas repetidos.
- Validação de valores de idade.
- Mensagens de erro para dados inválidos.

## Requisitos

- Python 3 instalado.
- Termux, Linux ou outro ambiente compatível com Python.

## Como executar

No terminal, entre na pasta do projeto:

```bash
cd ~/freelancer_dados/conversor_csv_json
```

Execute a conversão:

```bash
python conversor.py clientes.csv clientes.json
```

O primeiro argumento é o arquivo CSV de entrada.
O segundo argumento é o arquivo JSON de saída.

## Arquivos de exemplo

- `clientes.csv`: dados de entrada.
- `clientes.json`: resultado da conversão.
- `incompleto.csv`: teste de campos ausentes.
- `extras.csv`: teste de campos adicionais.
- `duplicado.csv`: teste de nomes de colunas repetidos.
- `idade_invalida.csv`: teste de idade inválida.

## Testes realizados

Foram realizados testes com:

- Conversão de registros válidos.
- Campos ausentes.
- Campos extras.
- Nomes de colunas repetidos.
- Idade inválida.
- Arquivo CSV vazio.
- Arquivo de saída já existente.

Os resultados devem ser conferidos novamente após
alterações no programa.

## Objetivo profissional

Este projeto demonstra conhecimentos práticos de Python,
manipulação de arquivos, conversão de formatos e validação
de dados.

Possíveis aplicações incluem preparação de dados para
planilhas, sistemas e integrações entre ferramentas.

## Próximas melhorias

- Criar testes automatizados.
- Melhorar o tratamento de erros.
- Documentar os formatos de entrada e saída.
- Preparar exemplos de uso para clientes.
- Publicar o projeto no GitHub como portfólio.
