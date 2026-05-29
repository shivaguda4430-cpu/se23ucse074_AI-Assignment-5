# AI-Based Knowledge Reuse Travel Planner

An intelligent travel planning engine designed to reuse, link, and reason across independent, domain-specific semantic knowledge bases (such as separate Ontologies for Tourism, Gastronomy, and Enology/Wine pairing).

## Architectural Design Highlights
- **Semantic Data Integration:** Uses `rdflib` to represent distinct domain knowledge structures using a single linked Graph mechanism.
- **Cross-Domain Reasoning:** Leverages descriptive **SPARQL** syntax queries to bridge gaps between distinct properties (e.g., matching a location's signature dish to a corresponding grape variety structure).
- **Constraint-Driven Optimization:** Evaluates financial and preference thresholds dynamically to build personal trip portfolios.

## System Workflow
1. **Extraction:** SPARQL matches available location assets alongside multi-domain characteristics.
2. **Evaluation:** The optimization routine filters items sequentially based on remaining budget parameters.
3. **Personalization:** Tailors gastronomic highlights according to whether an individual enables wine pairing logic.

## Execution and Testing
Run the evaluation test coverage suite directly from your terminal workspace layout using:

```bash
python -m unittest discover -s tests
