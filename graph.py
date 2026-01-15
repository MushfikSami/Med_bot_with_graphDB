import os 
from langchain_neo4j import Neo4jGraph
NEO4J_URI='neo4j+s://5c4048d0.databases.neo4j.io'
NEO4J_USER='neo4j'
NEO4J_PASSWORD='vjetHC2FpoE0-IHaJ-L6z_ShDN1apfA_sFCnNNXOo3E'


os.environ["NEO4J_URI"]=NEO4J_URI
os.environ["NEO4J_USER"]=NEO4J_USER
os.environ["NEO4J_PASSWORD"]=NEO4J_PASSWORD

graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USER, password=NEO4J_PASSWORD)
medicine_query = """
LOAD CSV WITH HEADERS FROM
'https://drive.google.com/uc?export=download&id=14oHvT-j3Du4fgOKBol6yOtkgFGgChRg7'
AS row

// Medicine node
MERGE (m:Medicine {name: row.`Medicine Name`})

// Uses: comma-separated
FOREACH (use IN split(row.Uses, ',') |
    MERGE (u:Use {name: trim(use)})
    MERGE (m)-[:USED_FOR]->(u)
)

// Composition: split components on '+'
FOREACH (comp IN split(row.Composition, '+') |
    MERGE (c:Composition {name: trim(comp)})
    MERGE (m)-[:CONTAINS]->(c)
)

// Side effects: comma-separated
FOREACH (se IN split(row.Side_effects, ',') |
    MERGE (s:SideEffect {name: trim(se)})
    MERGE (m)-[:HAS_SIDE_EFFECT]->(s)
)
"""
graph.query(medicine_query)
graph.refresh_schema()