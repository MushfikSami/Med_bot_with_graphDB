from langchain_neo4j import GraphCypherQAChain
from llm import llm
from graph import graph
chain=GraphCypherQAChain.from_llm(llm=llm, graph=graph,verbose=True,
                                  allow_dangerous_requests=True)

response=chain.run("what is composition of medicine used for diabetes?")
print(response)