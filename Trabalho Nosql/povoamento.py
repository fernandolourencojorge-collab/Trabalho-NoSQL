import random
from pymongo import MongoClient
from faker import Faker

# 1. Conexão ao MongoDB que está a correr no  Docker
# Usamos o utilizador 'admin' e a senha 'password123' que configuraste
client = MongoClient("mongodb://admin:password123@localhost:27017/")
db = client["ecommerce_db"]       # Isto cria automaticamente a base de dados
produtos_col = db["produtos"]     # Isto cria a coleção (tabela NoSQL) de produtos

# 2. Inicializar o gerador de dados fictícios (Faker)
fake = Faker()

print(" A iniciar o povoamento de dados... Isto vai demorar apenas alguns segundos.")

# Listas de apoio para gerar dados realistas de um catálogo de e-commerce
marcas = ["Samsung", "Apple", "Xiaomi", "Sony", "LG", "Asus", "HP", "Lenovo", "Dell", "Huawei"]
categorias_disponiveis = ["Eletrónicos", "Informática", "Telemóveis", "Áudio", "Gadgets", "Acessórios", "Gaming"]
cores = ["Preto", "Branco", "Cinzento", "Azul", "Dourado", "Vermelho"]
tipos_produto = ["Smartphone", "Portátil", "Auscultadores", "Smartwatch", "Monitor", "Teclado Mecânico", "Rato Gaming"]

#  Inserção em Lote (Bulk Insert) para ser mas rápido
lote_produtos = []
total_registos = 100000  #  requisito mínimo do trabalho!

for i in range(1, total_registos + 1):
    marca = random.choice(marcas)
    tipo = random.choice(tipos_produto)
    nome_produto = f"{tipo} {fake.first_name()} Pro {random.choice(['X', 'V2', 'Ultra', 'Max'])}"
    
    # Criar a estrutura do documento JSON (Modelagem Desnormalizada)
    produto = {
        "nome": nome_produto,
        "descricao": fake.sentence(nb_words=12),
        "preco": round(random.uniform(15.0, 1800.0), 2),
        "stock": random.randint(5, 450),
        "marca": marca,
        "categorias": random.sample(categorias_disponiveis, k=random.randint(1, 3)),
        "atributos": {
            "cor": random.choice(cores),
            "modelo_ano": random.randint(2024, 2026),
            "garantia_meses": random.choice([12, 24, 36])
        },
        "avaliacoes": [
            {
                "utilizador": fake.user_name(),
                "estrelas": random.randint(3, 5),
                "comentario": "Excelente equipamento, superou as expectativas.",
                "data": "2026-05-24"
            } for _ in range(random.randint(1, 3)) # Embutir de 1 a 3 avaliações dentro do produto
        ],
        "media_avaliacoes": round(random.uniform(3.5, 5.0), 1)
    }
    
    lote_produtos.append(produto)
    
    # Quando o lote chega a 10.000, envia para o banco de dados de uma só vez
    if len(lote_produtos) == 10000:
        produtos_col.insert_many(lote_produtos)
        print(f" {i} produtos processados e inseridos...")
        lote_produtos = [] # Limpa a memória para o próximo lote

print(" Sucesso Absoluto! 100.000 documentos foram injetados no  MongoDB!")