#!/usr/bin/env python
# coding: utf-8

# ## Radial Distribution Functions

# The second function important in describing atomic orbitals is a radial distribution function, which are described by Laguerre polynomials. The program below outputs both the original graph, as well as a graph where each probability is squared. If we recall the formula for the surface area of a sphere; 4πr2, we see that the surface area increases in proportion to r2. Therefore, as distance from the nucleus increases, the probability must be squared.
# 
# You will notice that on the graphs below, the probability never reaches zero but instead asymptotes to zero. Theoretically, an electron in an orbital can be found at any distance from the nucleus. However, as the distance from the nucleus increases, the probability of finding an electron becomes incredibly small. For this reason, chemists typically represent orbitals as the region in which there is a 90% chance of finding an electron or a pair of electrons.
# 
# Unfortunately, scipy does not have a neat function for radial distribution functions like it does for the spherical harmonics, so we are required to solve by hand.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

colour = ['b-']

def  radial_wave_function (r, n, l, ):
    Z = 1     
    p = Z*r
    rho = 0
    if n == 1  and l == 0 :
        return 2*(Z**1.5)*np.exp(-p)
    elif n == 2  and l == 0 :
         return ((Z/2)**1.5)*(2-p)*np.exp(-p/2)
    elif n == 2  and l == 1:
         return (1/(np.sqrt(3))*((Z/2)**1.5)*p*np.exp(-p/2))
    elif n == 3  and l == 0 :
         return (2/27)*((Z/3)**1.5)*(27-18*p+2*(p**2))*np.exp(-p/3)
    elif n == 3 and l == 1 :
         return (1/27)*((2*Z/3)**1.5)*p*(6-p)*np.exp(-p/3)
    elif n == 3  and l == 2 :
         return (4/(27*np.sqrt(10)))*((Z/3)**1.5)*(p**2)*np.exp(-p/3)
        
# Quantum number setting 
n = 1
l = 0

# Graph drawing 
r = np.linspace ( 0 , 30 , 500 )

h_rad = 31
'''
plt.figure ()
plt.plot (r, 0*radial_wave_function (r, n, l)) 
plt.plot (r, radial_wave_function (r, n, l), colour[0])  
plt.xlabel ( "Distance from nucleus" , fontsize = 14 )
plt.ylabel ( "Radial wave function" , fontsize = 14 )
plt.show ()
'''
names = [['1s'], ['2s', '2p'], ['3s', '3p', '3d']]
# a_0 is the Bohr radius of a hydrogen atom
plt.figure ()
#plt.plot (r, 0*radial_wave_function (r, n, l)) 
for n in  range ( 4 ):
     for l in  range (0,n):
            fig = plt.figure (figsize = ( 4.0 , 4.0 ))
            plt.plot (r, (radial_wave_function (r, n, l) ** 2 ) * (r ** 2 ), colour[0])   # Radial distribution function 
            plt.xlabel ( "Distance from nucleus" , fontsize = 14 )
            plt.ylabel ( "Radial distribution function" , fontsize = 14 )
            plt.title(names[n-1][l])
            function = (radial_wave_function (r, n, l) ** 2 ) * (r ** 2 )

plt.show ()


# In[ ]:




