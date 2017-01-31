import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

# Import data

data = genfromtxt('/Users/mikelevine/PycharmProjects/ENSO_VS_HURRICANES/ENSO_VS_NAMED_HURRICANES.csv',
                  delimiter=',')

# Define arrays and remove nan values

hurr = np.zeros(len(data))

for i in range(len(data)):
    hurr[i] = data[i][12]

hurr = hurr[~np.isnan(hurr)]

ensomonths = np.delete(data,[12,13,14,15,16,17,18,19],1)

for i in range(4):
    ensomonths = np.delete(ensomonths,len(ensomonths)-1,0)

# Hurricane Season on Average, runs from June to November (eliminate other months and average enso signal)

ensohseason = np.delete(ensomonths, 11, 1)
for i in range(5):
    ensohseason = np.delete(ensohseason, 0, 1)

# Average hurricane season ENSO signal for each year

ensohseasonmean = np.mean(ensohseason, 1)

fig, ax = plt.subplots()
lns1=ax.plot(np.arange(1950,2015,1), ensohseasonmean, 'r-', label="Mean ENSO Signal (June-November)")
lns2=ax.plot(np.arange(1950,2015,1), hurr, 'b-', label="Number of Hurricanes")
ax.set_xlabel("Year")
ax.set_ylabel("Mean ENSO Signal / Number of Hurricanes")
lns = lns1+lns2
labs = [l.get_label() for l in lns]
legend1 = ax.legend(lns,labs,loc=0, prop={'size':10})
plt.title("Annual Mean ENSO Signal vs Number of Named Hurricanes")
plt.show()

# Define and plot derivatives

densohseasonmean = np.gradient(ensohseasonmean)
dhurr = np.gradient(hurr)

fig, ax = plt.subplots()
lns1=ax.plot(np.arange(1950,2015,1), densohseasonmean, 'r-', label="Change in Mean ENSO Signal")
lns2=ax.plot(np.arange(1950,2015,1), dhurr, 'b-', label="Change in Number of Hurricanes")
ax.set_xlabel("Year")
ax.set_ylabel("Change in Mean ENSO Signal / Number of Hurricanes")
lns = lns1+lns2
labs = [l.get_label() for l in lns]
legend1 = ax.legend(lns,labs,loc=0, prop={'size':10})
plt.title("Change in Annual Mean ENSO Signal vs Number of Named Hurricanes")
plt.show()