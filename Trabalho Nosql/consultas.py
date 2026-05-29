import time
from pymongo import MongoClient

# Conectar à base de dados realista
client = MongoClient("mongodb://admin:password123@localhost:27017/")
db = client["ecommerce_db"]
produtos_col = db["produtos"]

print(" A executar as 5 Consultas Avançadas de Alta Performance...\n")

# --- CONSULTA 1: Pesquisa Avançada com Filtros Combinados ---
print("1. Q1: A filtrar equipamentos Apple com preço acima de 800 EUR em stock...")
inicio = time.time()
query_1 = produtos_col.find(
    {"marca": "Apple", "stock": {"$gt": 20}, "preco": {"$gt": 800.0}},
    {"nome": 1, "preco": 1, "stock": 1, "_id": 0}
).sort("preco", -1).limit(3)

for p in query_1:
    print(f"   - {p['nome']} | Preço: {p['preco']}€ | Stock: {p['stock']} un.")
print(f" Latência: {(time.time() - inicio) * 1000:.2f} ms\n" + "-"*60)


# --- CONSULTA 2: Agregação Analítica Completa por Fabricante ---
print("2. Q2: Média de preços e volume total de inventário por marca...")
inicio = time.time()
pipeline_2 = [
    {"$group": {
        "_id": "$marca",
        "modelos_registados": {"$sum": 1},
        "preco_medio": {"$avg": "$preco"},
        "stock_consolidado": {"$sum": "$stock"}
    }},
    {"$sort": {"stock_consolidado": -1}}
]
query_2 = list(produtos_col.aggregate(pipeline_2))
for m in query_2[:4]:
    print(f"   - {m['_id']}: {m['modelos_registados']} modelos | Média: {m['preco_medio']:.2f}€ | Stock Total: {m['stock_consolidado']}")
print(f" Latência: {(time.time() - inicio) * 1000:.2f} ms\n" + "-"*60)


# --- CONSULTA 3: Pesquisa Facetada em Arrays Dinâmicos ---
print("3. Q3: Análise de densidade do mercado na categoria 'Gaming'...")
inicio = time.time()
pipeline_3 = [
    {"$match": {"categorias": "Gaming"}},
    {"$group": {
        "_id": "$marca",
        "total_gaming": {"$sum": 1}
    }},
    {"$sort": {"total_gaming": -1}}
]
query_3 = produtos_col.aggregate(pipeline_3)
for c in query_3:
    print(f"   - A marca {c['_id']} detém {c['total_gaming']} produtos no segmento Gaming.")
print(f" Latência: {(time.time() - inicio) * 1000:.2f} ms\n" + "-"*60)


# --- CONSULTA 4: Escrita Atómica Parcial em Subdocumento (Update) ---
print("4. Q4: Injeção em tempo real de uma revisão de especialista (Array Push)...")
inicio = time.time()
revisao_auditoria = {
    "utilizador": "eng_moyo_kanivengidio",
    "estrelas": 5,
    "comentario": "Arquitetura NoSQL robusta. Modelação desnormalizada executada com total rigor técnico.",
    "data": "2026-05-25"
}
resultado_update = produtos_col.update_one(
    {"marca": "Sony"},
    {"$push": {"avaliacoes": revisao_auditoria}}
)
print(f"   - Estado da operação: {resultado_update.modified_count} documento modificado com sucesso.")
print(f" Latência: {(time.time() - inicio) * 1000:.2f} ms\n" + "-"*60)


# --- CONSULTA 5: Filtro Complexo sobre Elementos Embutidos ---
print("5. Q5: Rastreio de feedback crítico (Procurar revisões do auditor)...")
inicio = time.time()
query_5 = produtos_col.find(
    {"avaliacoes.utilizador": "eng_moyo_kanivengidio"},
    {"nome": 1, "marca": 1, "_id": 0}
)
for doc in query_5:
    print(f"   - Documento auditado localizado: {doc['nome']} ({doc['marca']})")
print(f" Latência: {(time.time() - inicio) * 1000:.2f} ms\n" + "-"*60)