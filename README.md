## Apresentação

Este projeto busca demonstrar o funcionamento de um API desenvolvida em DRF que utiliza de um container NGINX para realizar o balanço de carga entre 3 containers contendo a aplicação DRF, todos os containers se comunicam com um container que contém um DB em Postgres. Uma simples demonstração de como se opera aplicações em microserviços.

## Arquivo .env

Esquemático do arquivo .env usado neste projeto

```bash
SECRET_KEY=chave_secreta_django
DB_NAME=nome_do_banco
DB_USER=usuario_do_banco
DB_PASSWORD=senha_do_banco
DB_HOST=db
DB_PORT=5432
```

## Execução

Para execução dos containers

```bash
  docker-compose up --build -d
```

Aplicar migrações na primeira execução

```bash
  docker exec -it api1 python manage.py makemigrations
  docker exec -it api1 python manage.py migrate
```

Apagar containers e volumes

```bash
   docker-compose down -v  
```

## Sugestões
Até o momento não consegui aplicar o padrão de estilos quando acessado o admin via WEB. 
