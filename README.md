### Arquivo .env

`SECRET_KEY=chave_secreta_django`

`DB_NAME=nome_do_banco`

`DB_USER=usuario_banco`

`DB_PASSWORD=senha_banco`

`DB_HOST="db"`

`DB_PORT="5432"`

### Execução

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

