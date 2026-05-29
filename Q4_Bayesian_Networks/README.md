# Probabilistic Graphical Models: Bayesian Networks

This repository contains an overview of the core architectural framework of Bayesian Networks (BNs), a review of industry-standard modeling tools, and an end-to-end Python implementation of a Medical Diagnosis causal inference network.

---

## 1. Core Framework for Bayesian Networks

A **Bayesian Network (BN)** is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a **Directed Acyclic Graph (DAG)**. 

To work with Bayesian Networks, enterprise AI systems must systematically handle three distinct layers:
1. **Modeling (Structure Design):** Defining the nodes (which represent random variables) and directed edges (which represent causal or probabilistic dependencies).
2. **Problem Representing (Parameters):** Quantifying the precise relationships between connected nodes using **Conditional Probability Tables (CPTs)** for discrete domains or continuous probability distributions.
3. **Inferencing (Reasoning):** Computing the posterior probability distribution of a set of query variables given some observed evidence (for example, calculating $P(\text{Disease} \mid \text{Symptom} = \text{True})$).

---

## 2. Industry Tools & Libraries

Several powerful libraries and software suites exist across different software ecosystems to handle modeling, parameter estimation, and reasoning:

### A. Open-Source Libraries (Code-First)
* **`pgmpy` (Python):** The most popular Python library for probabilistic graphical models. It offers comprehensive support for structure learning, parameter estimation, and both exact inference (e.g., Variable Elimination) and approximate inference (e.g., MCMC sampling).
* **`bnlearn` (R):** An industry-standard R package designed primarily for learning the structure of Bayesian networks from data, supporting continuous and discrete variables.
* **`WebPPL` / `Pyro` / `Stan`:** Probabilistic programming languages (PPLs) that can represent Bayesian networks as generative computer programs, making them highly scalable for complex continuous models.

### B. Graphical User Interfaces (GUI Tools)
* **GeNIe / Smile:** A robust, widely used academic and commercial visual tool for building decision-theoretic models.
* **Hugin Expert:** An enterprise-grade tool known for its highly optimized inference algorithms based on junction trees.

---

## 3. Implementation Example: Medical Diagnosis Network

This pipeline models a classic medical diagnostic problem containing three chained variables to demonstrate causal inference processing:
* **Background/Risk Node:** `Smoker` (True/False)
* **Disease Node:** `LungCancer` (True/False) — Dependent directly on smoking status.
* **Symptom Node:** `Cough` (True/False) — Dependent directly on having lung cancer.

### Dependencies Installation
Install the necessary computational frameworks via your terminal:
```bash
pip install pgmpy networkx
