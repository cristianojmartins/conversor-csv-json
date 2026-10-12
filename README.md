# Conversor CSV para JSON e Excel

Aplicação desenvolvida em Python para converter arquivos CSV
em JSON ou planilhas Excel (.xlsx), com validação de dados
e testes automatizados.

O projeto faz parte de um portfólio prático de programação,
com foco em tratamento, organização e conversão de dados.

## Funcionalidades

- Conversão de CSV para JSON.
- Conversão de CSV para Excel (.xlsx).
- Interface web para enviar arquivos pelo navegador.
- Execução também pelo terminal.
- Preservação de caracteres acentuados.
- Validação de campos ausentes ou extras.
- Identificação de cabeçalhos duplicados.
- Validação de valores de idade.
- Limite de upload de 5 MB na aplicação web.
- Proteção do nome do arquivo enviado.
- Testes automatizados para conversões e erros.

## Tecnologias

- Python 3
- Flask
- openpyxl
- unittest
- HTML e CSS na interface web

## Requisitos

Python 3 instalado e acesso ao terminal.

Instale as dependências:

```bash
python -m pip install flask openpyxl
```

## Executar a versão web

Entre na pasta do projeto:

```bash
cd ~/freelancer_dados/conversor_csv_json
```

Inicie a aplicação:

```bash
python app_web.py
```

No navegador do mesmo dispositivo, abra:

http://127.0.0.1:8000

Selecione um arquivo CSV e escolha JSON ou Excel como formato
de saída. Depois, envie o arquivo para iniciar a conversão.

Para encerrar a aplicação, volte ao terminal e pressione
Ctrl+C.

## Executar pelo terminal

Para converter CSV em JSON:

```bash
python conversor.py clientes.csv clientes.json
```

O primeiro argumento é o arquivo CSV de entrada.
O segundo argumento é o arquivo JSON de saída.

## Executar os testes

Execute todos os testes automatizados:

```bash
python -m unittest discover -v
```

Os testes verificam conversões válidas, dados inválidos,
campos ausentes ou extras, cabeçalhos duplicados, arquivos
vazios, formato de saída não suportado, limite de upload,
nome seguro de arquivo e tratamento de erros internos.

## Arquivos de exemplo e teste

- `clientes.csv`: exemplo de entrada.
- `clientes.json`: exemplo de saída JSON.
- `incompleto.csv`: exemplo de campos ausentes.
- `extras.csv`: exemplo de campos extras.
- `duplicado.csv`: exemplo de cabeçalhos duplicados.
- `idade_invalida.csv`: exemplo de idade inválida.
- `vazio.csv`: exemplo de arquivo vazio.
- `test_conversor.py`: testes do conversor de terminal.
- `test_app_web.py`: testes da aplicação web.

## Segurança e limitações

A aplicação foi configurada para testes locais. Não a exponha
diretamente à internet sem uma revisão adicional de segurança
e uma configuração apropriada para produção.

O limite de upload da aplicação web é de 5 MB.

## Objetivo profissional

Demonstrar habilidades práticas em Python, manipulação de
arquivos, validação de dados, automação, testes e criação
de uma interface web para processamento de informações.

## Melhorias futuras

- Adicionar capturas de tela da aplicação.
- Organizar exemplos de entrada e saída.
- Ampliar a documentação e os testes.
- Preparar uma demonstração para o portfólio.
