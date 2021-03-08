import math
from run_TU import find_equilibrium_TU
from run_NTU import find_equilibrium_NTU


tol = 1e-12     # Absolute tolerance level for the fixed-point iteration

# TRANSFERABLE UTILITY (TU)

# FIGURE 1
print("FIGURE 1")
delta = 1
rho = 100
r = 1
def production_function(x, y): return x * y


nList = [10, 50, 100, 500]
for i in range(len(nList)):
    n = nList[i]
    fig_name = "fig1_" + str(i+1) + ".pdf"
    find_equilibrium_TU(n, delta, rho, r, production_function, fig_name, tol)




# From here, all the figures (except fig. 2B) are built with n = 500
n = 500




# FIGURE 2
print("FIGURE 2")
# FIGURE 2.1
delta = 1
rho = 100
r = 1
def production_function(x, y): return (x + y - 1) ** 2


fig_name = "fig2_1.pdf"
find_equilibrium_TU(n, delta, rho, r, production_function, fig_name, tol)

# FIGURE 2.2
# Here we take n = 501 because the algorithme does not converge for n=500
n_fig2B = 501
delta = 1
rho = 35
r = 1
def production_function(x, y): return (x + y) ** 2


fig_name = "fig2_2.pdf"
find_equilibrium_TU(n_fig2B, delta, rho, r, production_function, fig_name, tol)


# FIGURE 2.3
delta = 1
rho = 750
r = 1
def production_function(x, y): return x + y + x * y


fig_name = "fig2_3.pdf"
find_equilibrium_TU(n, delta, rho, r, production_function, fig_name, tol)


# FIGURE 2.4
delta = 0.5
rho = 50
r = 1
def production_function(x, y): return x + y + x * y


fig_name = "fig2_4.pdf"
find_equilibrium_TU(n, delta, rho, r, production_function, fig_name, tol)




# NON-TRANSFERABLE UTILITY (NTU)


# FIGURE 3
print("FIGURE 3")
# FIGURE 3.1
delta = 0.1
rho = 30
r = 0.3
def production_function(x, y): return math.exp(x * y)


fig_name = "fig3_1.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, fig_name, tol)


# FIGURE 3.2
delta = 1.1
rho = 30
r = 0.3
def production_function(x, y): return math.exp(x * y)


fig_name = "fig3_2.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, fig_name, tol)


# FIGURE 3.3
delta = 0.1
rho = 3
r = 0.3
def production_function(x, y): return x + y + x * y


fig_name = "fig3_3.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, fig_name, tol)


# FIGURE 3.4
delta = 1.1
rho = 3
r = 0.3
def production_function(x, y): return x + y + x * y


fig_name = "fig3_4.pdf"
find_equilibrium_NTU(n, delta, rho, r, production_function, fig_name, tol)




# NORMAL DISTIBUTION OF TYPES

# FIGURE 4
print("FIGURE 4")
delta = 1
rho = 1000
r = 1
def production_function(x, y): return x * y


mu_list = [0.2, 0.5, 0.8]
sigma_list = [0.01, 0.1, 0.2]
i = 1
for sigma in sigma_list:
    for mu in mu_list:
        fig_name = "fig4_" + str(i) + ".pdf"
        find_equilibrium_TU(n, delta, rho, r, production_function, fig_name, tol, "normal", mu, sigma)
        i += 1
