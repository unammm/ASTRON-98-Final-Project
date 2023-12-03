#!/usr/bin/env python
# coding: utf-8

# In[149]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as scipy
from scipy.optimize import curve_fit
# kepler: period**2 = sm_axis**3


# 0 to 1300days for period
# 0 to 2.5AU for semi-major axis
# Evan #2, #5 
# Una #3, #4, #5
# Note that changed proj. compared to proposal in final report!
df = pd.read_csv('plot (2).tbl(1).csv')
period = dfgood.iloc[:, 0]
sm_axis = dfgood.iloc[:, 1].astype('float')

print(len(period))
def modelcurve(period, k):
    period = np.asarray(period)
    modelval = (period**(2/3))*k
    return modelval

do = np.linspace(0, 1000, num = 1903)


def modelvallist(period):
    modellist = []
    period = np.asarray(period)
    i = 0
    while i < len(period):
        modelval1 = (period[i]**(2/3))*sol[0]
        modellist.append(modelval1)
        i = i+1
    return modellist

modellist1 = np.array(modelvallist(period))

# The code in Line 48, though redundant, was kept because the color it provides to the graph improves the contrast between the fitted curve
# and the points, and makes the graph more aesthetically pleasing. 
plt.figure(figsize = (10, 5))
plt.scatter(period, sm_axis, c = "orange", alpha = 1.0, linewidth = 3)
sol, why = curve_fit(modelcurve, period, sm_axis, p0 = 0.1)
plt.plot(do, modelcurve(do, sol[0]))
plt.errorbar(period, sm_axis, yerr = abs(sm_axis - modellist1), fmt = 'ro', ecolor = 'blue', barsabove = True, alpha=0.5)
plt.tight_layout()
plt.yscale('log')
plt.title('Planet Orbital Period Length versus Semi-Major Axis of Orbit')
plt.xlabel('Period (days)')
plt.ylabel('Semi-Major Axis (AU)')
plt.show()

#The constant k in Kepler's Third Law, as calculated by the scipy.optimize.curve_fit() function and output as sol[0].
print(sol[0], "AU^3/day^2")
print(sol[0]*(365**2), "AU^3/yr^2")



# In[144]:


"""
type(sm_axis[0])
sm_axis[sm_axis == '0 1.292000']

type(period)
"""


# In[7]:


df = pd.read_csv('plot (2).tbl(1).csv')
df


# In[43]:


pattern = "0 "
bad_vals = sm_axis.str.contains(pattern)
sm_axisgood = sm_axis[~bad_vals].astype('float')


# In[45]:


bad_vals = df['SM Axis'].str.contains(pattern)
dfgood = df[~bad_vals]

