# Projeto GoHacks

## Introdução
Este projeto utiliza o Typesense para busca e o N8N para automação de workflows. O objetivo é disponibilizar um agente que pode ser acessado via API.

## Pré-requisitos
- Docker e Docker Compose instalados
- Acesso ao N8N para importar o workflow

## Instruções de Execução
Para rodar o projeto, execute o seguinte comando para iniciar o Typesense com Docker Compose:

```bash
docker-compose up -d
```

## Importação de Dados
Para importar a base de dados para o Typesense, execute o script `import_to_typesense.py`:

```bash
python import_to_typesense.py
```

## Configuração do N8N
Importe o arquivo `GoConcierge N8N.json` no N8N. Após a importação, atualize as variáveis de chave presentes no workflow para disponibilizar o agente ao público.

## Comunicação com o Bot
Para se comunicar com o bot, faça um POST na URL do webhook do workflow do N8N. O corpo da requisição deve conter `sessionId` e `chatInput`. A resposta será um JSON com a chave `output`.

### Exemplo de Requisição
```bash
curl -X POST \
  <URL_DO_WEBHOOK> \
  -H 'Content-Type: application/json' \
  -d '{"sessionId": "12345", "chatInput": "Olá, como posso ajudar?"}'
```

A resposta será algo como:
```json
{
  "output": "Resposta do bot"
}
```