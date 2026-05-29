# Comprehensive Guide to Knowledge Graphs

This repository contains an overview of Knowledge Graph (KG) architectures, industry tools, and a complete, executable Python pipeline demonstrating how to build and query a semantic graph.

---

## 1. What is a Knowledge Graph?

A **Knowledge Graph (KG)** is a structured, semantic network of real-world entities, concepts, events, and situations, illustrating how they relate to one another. Instead of storing data in isolated rows and columns like a traditional relational database, a knowledge graph stores information as an interconnected web.

Data in a knowledge graph is represented using **triples**, which follow a strict **Subject $\rightarrow$ Predicate $\rightarrow$ Object** format:
* **Subject (Node):** The entity or concept (e.g., Leonardo da Vinci).
* **Predicate (Edge):** The directed relationship or property (e.g., painted).
* **Object (Node):** The target entity, concept, or literal value (e.g., Mona Lisa).

### Core Components of a Knowledge Graph
To build a functional knowledge graph, the system relies on three layers:
1. **The Graph Data (Instance Layer):** The actual facts and data points stored as interconnected nodes and edges.
2. **The Schema / Ontology (Conceptual Layer):** The formal rules, categories, and relationship definitions that govern the graph. For example, dictating that a `Person` can be an `authorOf` a `Book`, but a `Book` cannot be an `authorOf` a `Person`.
3. **The Identity System:** Utilizing Uniform Resource Identifiers (URIs/IRIs) to ensure every entity is globally unique, eliminating ambiguity (e.g., distinguishing Apple the company from apple the fruit).

---

## 2. Industry Tools to Build Knowledge Graphs

Building a knowledge graph involves multiple stages: **Storage (Graph Databases)**, **Ontology Modeling**, and **Ingestion/Extraction**. Below are the primary industry-standard tools categorized by their function.

### A. Graph Databases & Triplestores (Storage)
Graph databases store the actual data. They are split into two main architectures: **Property Graphs** (optimized for fast traversals and queries) and **RDF Triplestores** (optimized for semantic compliance and logical reasoning).

| Tool | Type | Query Language | Best Used For |
| :--- | :--- | :--- | :--- |
| **Neo4j** | Labeled Property Graph (LPG) | Cypher | High-performance transactional applications, fraud detection, and recommendation engines. Highly intuitive and widely adopted. |
| **GraphDB** | RDF Triplestore | SPARQL | Semantic Web projects, metadata management, and enterprise applications requiring automated logical reasoning (inference). |
| **Amazon Neptune** | Hybrid (LPG + RDF) | Cypher, Gremlin, SPARQL | Managed cloud architectures needing massive scalability and flexibility across both graph paradigms. |
| **Blazegraph** | RDF Triplestore | SPARQL | Ultra-high performance graph queries; famously powers the backend of Wikidata. |

### B. Ontology Engineering & Schema Modeling (Design)
Before writing data, you must define the schema or ontology.
* **Protégé:** An open-source, industry-standard tool developed by Stanford University for creating and managing OWL (Web Ontology Language) ontologies. It features automated reasoners to check for logical inconsistencies in your schema design.
* **TopBraid Composer:** A robust enterprise platform used for modeling semantic data collections, vocabularies, and complex data governance layouts.

### C. Data Ingestion & Information Extraction (Building)
Most knowledge graph data starts as unstructured text (PDFs, articles) or semi-structured data (SQL tables, CSVs).
* **RDFLib / Apache Jena:** Core programming frameworks (Python and Java, respectively) used to programmatically construct, manipulate, and query RDF data structures.
* **LangChain / LlamaIndex:** Modern AI frameworks used to build "GraphRAG" applications. They pass unstructured text to Large Language Models (LLMs) to automatically extract entities and relationships, constructing knowledge graphs out of raw prose.

---

## 3. Implement a Knowledge Graph Pipeline

Below is a complete Python pipeline using `rdflib` to model a basic schema, ingest facts, and execute a semantic query.

### Prerequisites
Install the required semantic web dependencies:
```bash
pip install rdflib
