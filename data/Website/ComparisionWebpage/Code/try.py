import pandas as pd

mandis = pd.read_csv('../Data/Information/mandis.csv')
mandisStates = pd.read_csv('../Data/Information/states.csv')
states = mandisStates['state']


for state in states:
	stateCode = list(mandisStates[mandisStates['state'] == state]['statecode'])[0]
	print(state,stateCode)
	mandisname = list(mandis[mandis['statecode'] == stateCode ]['mandiname'])
	print(mandisname)
