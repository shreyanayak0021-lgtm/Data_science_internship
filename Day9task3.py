import pandas as pd
s=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print("use vectorized string operation to:")
print("Removing leading/trailing whitespace:\n",s.str.strip())
print("Converting all names to lowercase:\n",s.str.lower())
print("Checks which names contain the letter 'a':\n",s.str.contains('a'))