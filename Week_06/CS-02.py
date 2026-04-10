from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Disease': ['Flu', 'Flu', 'COVID', 'COVID', 'Allergy', 'Allergy', 'Flu', 'COVID'],
    'Fever': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'],
    'Cough': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes'],
    'Fatigue': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes']
})

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue')
])

model.fit(data)

inference = VariableElimination(model)

result = inference.query(
    variables=['Disease'],
    evidence={'Fever': 'No', 'Cough': 'Yes'}
)

print("\n=== Diagnosis Result ===")
print(result)