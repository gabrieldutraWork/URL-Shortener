# URL Shortener

Este é um projeto de **encurtador de URLs** que permite transformar URLs longas em versões curtas e simples, com a capacidade de rastrear e monitorar acessos. O sistema foi containerizado usando **Docker Compose** para facilitar a execução em ambientes de desenvolvimento ou produção.

## Sobre

O projeto tem como objetivo principal oferecer um serviço de encurtamento de links com as seguintes funcionalidades:

- Criação de URLs curtas personalizadas ou automáticas;
- Redirecionamento eficiente para o link original;
- Armazenamento das URLs em banco de dados;
- Coleta de estatísticas de acesso (opcional).

A arquitetura foi projetada para ser simples, modular e escalável.

## Como Executar com Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/url-shortener.git
   cd url-shortener/url-shortener

2. Execute com Docker Compose:
   ```bash
   docker-compose up --build
   
3. Acesse o sistema (padrão):
   - Frontend: http://localhost:3000
   - API: http://localhost:8000

Obs.: Os serviços e portas podem variar conforme definidos no docker-compose.yml.

## Tecnologias Utilizadas

  - Python / FastAPI ou Node.js / Express (dependendo da stack real)

  - PostgreSQL ou MongoDB (dependendo do backend)

  - Docker e Docker Compose

## Estrutura do Projeto

  ```bash
  url-shortener/
  └── url-shortener/
    └── docker-compose.yml      # Orquestração dos serviços da aplicação

