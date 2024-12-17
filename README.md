# 📚 Projeto FastAPI: API de Gerenciamento de Cursos

## 📄 Descrição do Projeto

Esta é uma API desenvolvida em FastAPI para gerenciar um catálogo de cursos, permitindo operações CRUD (Create, Read, Update, Delete). A API possibilita adicionar, listar, atualizar e deletar cursos, proporcionando uma estrutura simples e eficiente para gerenciamento de dados.

---

## 🚀 Tecnologias Utilizadas  

-   **Python 3.10+**
-   **FastAPI**
-   **Uvicorn** (servidor ASGI)
-   **PostgreSQL** (banco de dados)
-   **Postman** (para testar as rotas)
---

## 📦 Como Executar  

### Pré-requisitos  
1. Tenha o **Python 3.10+** instalado em sua máquina.
   
2. **Criar e Ativar um Ambiente Virtual (venv)**  
   Para isolar as dependências do projeto e garantir que não haja conflitos com outros projetos, é recomendado criar um ambiente virtual. Siga os passos abaixo:

   - No terminal, navegue até o diretório do projeto e execute o seguinte comando para criar um ambiente virtual:
     ```bash
     python -m venv venv
     ```
   
   - Para ativar o ambiente virtual:
     - **No Windows:**
       ```bash
       .\venv\Scripts\activate
       ```
     - **No macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Instalar as dependências**  
   Com o ambiente virtual ativado, instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

4. **Configurar o Banco de Dados PostgreSQL**

-   Certifique-se de ter o PostgreSQL instalado e em execução.
-   Crie um banco de dados para o projeto. Você pode fazer isso usando o terminal do PostgreSQL:
  ```sql
  CREATE DATABASE nome_do_banco;
 ```
- Crie um usuário e conceda permissões ao banco de dados:
```
CREATE USER nome_do_usuario WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO nome_do_usuario;
```

5. **Configurar Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:
```
DATABASE_URL=postgresql://nome_do_usuario:sua_senha@localhost/nome_do_banco
```

## 🚀 Como Rodar a API

1. **Iniciar o servidor Uvicorn**
2. **Execute o seguinte comando no terminal para iniciar o servidor:**
  ```bash
   uvicorn main:app --reload
  ```

3. **Acessar a API**
Após iniciar o servidor, a API estará disponível em **http://localhost:8000**. Você pode acessar as rotas e testar as funcionalidades.

4. **Testar as rotas com Postman**
Use o Postman para testar as rotas da API, como:

      **GET /cursos – Listar todos os cursos.**
      
      **POST /cursos – Adicionar um novo curso.**
      
      **PUT /cursos/{id} – Atualizar um curso existente.**
      
      **DELETE /cursos/{id} – Deletar um curso.**


## 📄 Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, siga os passos abaixo:

1.  Faça um fork do repositório.
2.  Crie uma nova branch (`git checkout -b feature/nome-da-sua-feature`).
3.  Faça suas alterações e commit (`git commit -m 'Adicionando nova feature'`).
4.  Envie para o repositório remoto (`git push origin feature/nome-da-sua-feature`).
5.  Abra um Pull Request.

* * * * *

## 📞 Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: joaol324j@gmail.com
