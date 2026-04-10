from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame(data={'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
'TrafficJam': ['Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No'],
'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']})

model = DiscreteBayesianNetwork([('Rain', 'TrafficJam'), ('TrafficJam', 'ArriveLate')])

model.fit(data)

print(model.get_cpds())

inference = VariableElimination(model)
query_result = inference.query(variables=['Rain'], evidence={'ArriveLate': 'Yes'})
print(query_result)
