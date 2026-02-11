import pandas as pd
s=pd.Series([85, None, 92, 45, None, 78, 55])
print("original series:\n",s)
print("values missing :\n",s.isnull())
print("missing value filled with 0(filled series)\n:",s.fillna(0))
#boolean mask
print("filtered results:\n",s[s>60])