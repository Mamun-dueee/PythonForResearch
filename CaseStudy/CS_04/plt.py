import matplotlib.pyplot as plt
plt.figure(figsize = (10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")
