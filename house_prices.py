import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

train_file_path = '/home/matheus/PycharmProjects/HousePrices/data/train.csv'
df_train = pd.read_csv(train_file_path)
one = OneHotEncoder()
one.fit(df_train)
print(df_train)
corrmat = df_train.corr()
atributo = "LotFrontage"
corr  = corrmat[atributo].tolist()
cols = corrmat.columns.tolist()
atributos = []
for i in range(len(corr)):
    atributos.append((cols[i], corr[i]))
atributos.sort(key=lambda tup: tup[1], reverse=True)
for i in range(1, len(atributos)):
    if atributos[i][0] != "SalePrice":
        if atributos[i][1] >= 0.75:
            print("Os atributos",  atributo, "e",  atributos[i][0],  "são altamente correlacionados ("+str(atributos[i][1]) +
                  ").")
        elif atributos[i][1] >= 0.6:
            print("Os atributos", atributo, "e", atributos[i][0], "são bem correlacionados ("+ str(atributos[i][1])+
                  ").")


        #print(i, "- ", atributos[i][0], ": ", atributos[i][1])
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.show()
