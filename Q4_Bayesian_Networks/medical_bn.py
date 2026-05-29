from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def build_medical_network():
    # 1. Define network structure (Modeling)
    # Edges define: Smoker -> LungCancer -> Cough
    model = BayesianNetwork([('Smoker', 'LungCancer'), ('LungCancer', 'Cough')])

    # 2. Represent Problems via Conditional Probability Tables (CPTs)
    
    # Prior probability of being a smoker: P(Smoker)
    # [P(Smoker=False), P(Smoker=True)]
    cpd_smoker = TabularCPD(variable='Smoker', variable_card=2, values=[[0.7], [0.3]])

    # Conditional probability of Lung Cancer given Smoking status: P(LungCancer | Smoker)
    # Matrix shape: [Variable_Card, Parent_Product_Card]
    # Rows: Cancer=False, Cancer=True | Columns: Smoker=False, Smoker=True
    cpd_cancer = TabularCPD(
        variable='LungCancer', 
        variable_card=2,
        values=[[0.9, 0.6],  # Cancer = False
                [0.1, 0.4]], # Cancer = True
        evidence=['Smoker'], 
        evidence_card=[2]
    )

    # Conditional probability of Cough given Lung Cancer status: P(Cough | LungCancer)
    # Rows: Cough=False, Cough=True | Columns: Cancer=False, Cancer=True
    cpd_cough = TabularCPD(
        variable='Cough', 
        variable_card=2,
        values=[[0.8, 0.2],  # Cough = False
                [0.2, 0.8]], # Cough = True
        evidence=['LungCancer'], 
        evidence_card=[2]
    )

    # Associate CPTs with the structural model
    model.add_cpds(cpd_smoker, cpd_cancer, cpd_cough)

    # Validate model structures and probabilities sum to 1.0
    assert model.check_model(), "Model validation failed!"
    return model

def perform_inference(model):
    # 3. Initialize the Inferencing Engine using Variable Elimination
    inference = VariableElimination(model)

    print("--- Running Bayesian Inference ---")

    # Scenario A: Diagnostic Query (What is the chance of cancer if a patient has a cough?)
    print("\nQuery 1: P(LungCancer | Cough = True)")
    q1 = inference.query(variables=['LungCancer'], evidence={'Cough': 1})
    print(q1)

    # Scenario B: Interventional/Causal Query (What is the chance of a cough if we know they smoke?)
    print("\nQuery 2: P(Cough | Smoker = True)")
    q2 = inference.query(variables=['Cough'], evidence={'Smoker': 1})
    print(q2)

if __name__ == "__main__":
    medical_model = build_medical_network()
    perform_inference(medical_model)
