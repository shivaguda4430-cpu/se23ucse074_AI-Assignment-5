from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD

def create_knowledge_graph():
    # 1. Initialize an empty Graph
    g = Graph()

    # 2. Define Custom Namespaces
    EX = Namespace("http://example.org/ontology/")
    g.bind("ex", EX)
    g.bind("foaf", FOAF)

    # 3. Add Schema Definitions (Ontology Layer)
    # Define Classes
    g.add((EX.Scientist, RDF.type, EX.Profession))
    g.add((EX.Award, RDF.type, EX.Concept))

    # Define Relationships (Predicates)
    g.add((EX.hasWon, RDF.type, RDF.Property))
    g.add((EX.fieldOfStudy, RDF.type, RDF.Property))

    # 4. Ingest Instance Data (Data Layer)
    # Entity: Marie Curie
    marie_curie = EX.MarieCurie
    g.add((marie_curie, RDF.type, FOAF.Person))
    g.add((marie_curie, FOAF.name, Literal("Marie Curie", datatype=XSD.string)))
    g.add((marie_curie, EX.fieldOfStudy, Literal("Radioactivity", datatype=XSD.string)))
    g.add((marie_curie, EX.hasWon, EX.NobelPrizeInPhysics))
    g.add((marie_curie, EX.hasWon, EX.NobelPrizeInChemistry))

    # Entity: Nobel Prizes
    g.add((EX.NobelPrizeInPhysics, RDF.type, EX.Award))
    g.add((EX.NobelPrizeInPhysics, FOAF.name, Literal("Nobel Prize in Physics", datatype=XSD.string)))
    g.add((EX.NobelPrizeInChemistry, RDF.type, EX.Award))
    g.add((EX.NobelPrizeInChemistry, FOAF.name, Literal("Nobel Prize in Chemistry", datatype=XSD.string)))

    return g

def query_knowledge_graph(graph):
    # 5. Query the Graph using SPARQL (Semantic Querying)
    print("Executing SPARQL Query to find all awards won by Marie Curie...")
    
    query = """
    PREFIX ex: <http://example.org/ontology/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    
    SELECT ?awardName WHERE {
        ?person foaf:name "Marie Curie" .
        ?person ex:hasWon ?award .
        ?award foaf:name ?awardName .
    }
    """
    
    results = graph.query(query)
    for row in results:
        print(f"Result: Marie Curie won the {row.awardName}")

if __name__ == "__main__":
    kg = create_knowledge_graph()
    query_knowledge_graph(kg)
    
    # Optional: Save the graph to a standard semantic format (Turtle)
    kg.serialize(destination="knowledge_graph.ttl", format="turtle")
    print("\nKnowledge graph successfully saved to 'knowledge_graph.ttl'")
