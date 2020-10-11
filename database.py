import pandas as pd
db=pd.read_excel('Book1.xlsx')
for i in db.columns:
    db[i]=db[i].astype(str)
print(db.loc[0][1])
