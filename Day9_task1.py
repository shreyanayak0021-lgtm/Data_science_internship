import pandas as pd
data=pd.Series([700,150,300],index=["Laptop","Mouse","Keyboard"])
print(data['Laptop'])
print(data[0:2])