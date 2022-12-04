import pandas as pd

# create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'B', 'B', 'C'],
                   'conference': ['East', 'East', 'East', 'West', 'West', 'East'],
                   'points': [11, 8, 10, 6, 6, 5]})

for x in df.conference.unique():
    print(x)
print(df.team.value_counts())
