import pandas as pd

# create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'B', 'B', 'C'],
                   'conference': ['East', 'East', 'East', 'West', 'West', 'East'],
                   'points': [11, 8, 10, 6, 6, 5]})

for x in df.conference.unique():
    print(x)

# print((df.conference == 'East').sum())
print(len((df.conference.unique())))

# monthly_mean.plot(x=df.index, y='A')
# monthly_mean.plot(y='A')
# monthly_mean.reset_index().plot(x='index', y='A')
# monthly_mean.plot(y='A', use_index=True)
