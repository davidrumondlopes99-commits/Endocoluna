# EndoColuna Brasil — Docker

Deploy local ou em servidor próprio com um comando:

```bash
docker compose up -d --build
```

Acesse: **http://localhost** (frontend Nginx serve o React build e faz proxy de `/api/*` para o backend FastAPI).

## Serviços

| Serviço | Imagem base | Porta interna | Porta host |
|---|---|---|---|
| `frontend` | node:20-alpine → nginx:1.27-alpine (multi-stage) | 80 | **80** |
| `backend`  | python:3.11-slim + uvicorn | 8001 | não exposta (só rede interna) |
| `mongo`    | mongo:7 | 27017 | não exposta (só rede interna) |

O MongoDB persiste os dados no volume nomeado `mongo_data`.
Os 69 artigos e a coleção `newsletter` são recriados automaticamente pelo backend na primeira inicialização (seed idempotente).

## Variáveis de ambiente configuráveis

Edite `docker-compose.yml` → serviço `backend` → `environment`:

- `MONGO_URL` (default `mongodb://mongo:27017`)
- `DB_NAME` (default `endocoluna`)
- `CORS_ORIGINS` (default `*`, restrinja em produção)
- `PUBLIC_SITE_URL` (default `https://www.endocolunabrasil.com` — usado no sitemap.xml)

## Frontend com domínio customizado

Se quiser que o frontend embute uma URL absoluta do backend (em vez de rota relativa), rebuilde:

```bash
docker compose build --build-arg REACT_APP_BACKEND_URL=https://api.seudominio.com frontend
docker compose up -d
```

## Comandos úteis

```bash
docker compose logs -f backend      # ver logs do backend
docker compose logs -f frontend     # ver logs do nginx
docker compose exec mongo mongosh   # abrir shell do MongoDB
docker compose down                 # parar (mantém dados)
docker compose down -v              # parar + apagar volume de dados
```
