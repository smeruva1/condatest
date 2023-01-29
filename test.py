import pandas as pd

countries = [ { "id": 4, "name": 'New Zealand' }, { "id": 1, "name": 'USA' }, { "id": 2, "name": 'England' }, { "id": 3, "name": 'Russia' }, ]

df1 = pd.DataFrame(countries)

print(df1)