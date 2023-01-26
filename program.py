# Program for reading a content from CSv file
# Developed by: Prajeeth K T
# Reg.no: 22002267
import pandas as pd
df=pd.read_csv('nba.csv')
print(df.head(10))
print(df.tail())
print("Number of rows:",len(df.axes[0]))
print("Number of columns:",len(df.axes[1]))