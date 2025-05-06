# Atividade DW III
Nesse projeto, fizemso uma API que fornece informações sobre filmes, onde é possível verificar os dados dos filmes

## Estrutura do projeto  

- app.py: Arquivo principal que contém a definição da aplicação Flask e seus endpoints.
- requisicoes.http: Arquivo contendo exemplos de requisições HTTP que podem ser utilizadas para testar a API.
- .gitignore: Especifica os arquivos e pastas que devem ser ignorados pelo Git.
- README.md: Este arquivo, contendo informações sobre o projeto.

##  Como rodar

1. Clone o repositório:
```bash
   git clone https://github.com/mariavalentina05/crocodilo.git
   cd crocodilo
```

2. Crie um ambiente virtual:
```bash
   python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
.venv\Scripts\activate
```

4. Instale as bibliotecas necessárias:
```bash
pip install flask psycopg[binary] requests
```

5.Teste as requisiçõoes 
Utilize uma ferramenta como o Insomnia para enviar as requisições 

## Como usar 
1. Inicie a API:
```bash
flask --app app.py run
```
A API está disponível em: http://localhost:5000 

2. Envie suas requisições para a rota http://localhost:5000/consultaid/<id> ou /consultanome/<nomedofilme>

3. Nessa etapa a sua requisição retornará os dados do filme.
