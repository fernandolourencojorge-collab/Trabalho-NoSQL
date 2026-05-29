# Trabalho-NoSQL
Trabalho-NoSQL
# Sistema de Persistência NoSQL para Catálogo Dinâmico de E-commerce


O projeto consiste na implementação de uma camada de dados de alta performance e escalabilidade utilizando o SGBD orientado a documentos **MongoDB**, orquestrado em ambiente de contentores **Docker**. O sistema foi validado com uma massa crítica de **100.000 documentos reais e desnormalizados**.

##  Estrutura do Repositório

* `docker-compose.yml`: Ficheiro de orquestração que levanta o motor do MongoDB e a interface de gestão.
* `povoamento.py`: Script automatizado em Python que gera e injeta 100.000 registos realistas com alta fidelidade de mercado (Bulk Insert).
* `consultas.py`: Script de validação que executa as 5 queries complexas exigidas, cronometrando a latência em milissegundos.

##  Requisitos Prévios

Antes de executar a aplicação, garanta que tem instalado na sua máquina:
1.  **Docker Desktop** ativo (com suporte a WSL2/Linux Backend).
2.  **Python 3.x** instalado localmente.
3.  O driver do MongoDB para Python instalado via terminal:
    ```bash
    pip install pymongo
    ```

##  Instruções de Execução (Passo a Passo)

Siga rigorosamente a sequência abaixo para reproduzir o ambiente de testes:

### 1. Inicializar a Infraestrutura
Na raiz do projeto (onde se encontra o ficheiro `docker-compose.yml`), execute o comando para levantar os serviços isolados em segundo plano:
```bash
docker-compose up -d
## CREDENCIAIS DO SISTEMA

username: admin
password:password123
