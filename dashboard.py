import matplotlib.pyplot as plt
plt.subplot(1,2,1)
categories=['Electronics', 'Clothing', 'Home'] 
values=[300,450,200]
plt.bar(categories,values)
plt.xlabel("categories")
plt.ylabel("values")
plt.subplot(1,2,2)
plt.plot(categories,values)
plt.xlabel("categories")
plt.ylabel("values")
plt.tight_layout()
plt.show()