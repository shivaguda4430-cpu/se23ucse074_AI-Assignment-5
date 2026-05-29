from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.plugins.sparql import prepareQuery

# Namespaces for our domain
TRAVEL = Namespace("http://example.org/travel#")
WINE = Namespace("http://example.org/wine#")

class KnowledgeBaseManager:
    def __init__(self):
        self.graph = Graph()
        self.graph.bind("travel", TRAVEL)
        self.graph.bind("wine", WINE)
        self._load_mock_existing_kbs()

    def _load_mock_existing_kbs(self):
        """Simulates loading pre-existing distinct ontologies into a unified triplestore."""
        # 1. Existing Tourist Places KB
        self.graph.add((TRAVEL.Paris, RDF.type, TRAVEL.Destination))
        self.graph.add((TRAVEL.Paris, TRAVEL.hasActivity, TRAVEL.EiffelTower))
        self.graph.add((TRAVEL.EiffelTower, TRAVEL.cost, Literal(25)))
        self.graph.add((TRAVEL.EiffelTower, TRAVEL.category, TRAVEL.Sightseeing))
        
        self.graph.add((TRAVEL.Bordeaux, RDF.type, TRAVEL.Destination))
        self.graph.add((TRAVEL.Bordeaux, TRAVEL.hasActivity, TRAVEL.ChateauTour))
        self.graph.add((TRAVEL.ChateauTour, TRAVEL.cost, Literal(40)))
        self.graph.add((TRAVEL.ChateauTour, TRAVEL.category, TRAVEL.WineTasting))

        # 2. Existing Wine & Food Pairing Ontology Interaction
        self.graph.add((TRAVEL.Bordeaux, TRAVEL.famousForFood, TRAVEL.SteakFrites))
        self.graph.add((TRAVEL.SteakFrites, WINE.pairsWith, WINE.CabernetSauvenon))
        self.graph.add((WINE.CabernetSauvenon, RDF.type, WINE.RedWine))

    def query_activities_and_pairings(self, destination_name):
        """Cross-references the Tourist KB and Wine/Food Ontology using SPARQL."""
        dest_uri = URIRef(f"http://example.org/travel#{destination_name}")
        
        query_str = """
        SELECT ?activity ?cost ?food ?wine WHERE {
            ?dest travel:hasActivity ?activity .
            ?activity travel:cost ?cost .
            OPTIONAL {
                ?dest travel:famousForFood ?food .
                ?food wine:pairsWith ?wine .
            }
        }
        """
        query = prepareQuery(query_str, initNs={"travel": TRAVEL, "wine": WINE})
        return self.graph.query(query, initBindings={'dest': dest_uri})
