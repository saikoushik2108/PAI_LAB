from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'IncomeStability': ['High', 'Low', 'Low', 'Low', 'High', 'Low', 'High', 'Low'],
    'CreditHistory': ['Good', 'Bad', 'Bad', 'Bad', 'Good', 'Bad', 'Bad', 'Good'],
    'EmploymentType': ['Salaried', 'Self', 'Salaried', 'Unemployed', 'Self', 'Unemployed', 'Salaried', 'Self'],
    'DefaultRisk': ['No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No']
})

model = DiscreteBayesianNetwork([
    ('IncomeStability', 'DefaultRisk'),
    ('CreditHistory', 'DefaultRisk'),
    ('EmploymentType', 'DefaultRisk')
])


model.fit(data)


inference = VariableElimination(model)

query1 = inference.query(
    variables=['DefaultRisk'],
    evidence={'CreditHistory': 'Bad'}
)

print("\n=== Query 1: Given CreditHistory = Bad ===")
print(query1)

query2 = inference.query(
    variables=['DefaultRisk'],
    evidence={
        'IncomeStability': 'Low',
        'EmploymentType': 'Unemployed'
    }
)

print("\n=== Query 2: Income Low & Unemployed ===")
print(query2)