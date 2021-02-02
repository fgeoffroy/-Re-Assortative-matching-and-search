import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import sys



def find_equilibrium_TU(n, delta, rho, r, production_function, figName, distribution="uniform", mu=0.5, sigma=0.1):
    # market fluidity parameter
    theta = rho / (2 * (r + delta))

    # The distribution of types is discretized to perform a midpoint Riemann sum with n subdivisions
    contributions = np.linspace(1/n/2, 1-1/n/2, n)
    if distribution == "uniform":
        lDensity = 1
    elif distribution == "normal":
        # Normal distribution
        lDensity = np.exp(- ((contributions - mu) ** 2) / (2 * sigma ** 2) ) / (sigma * math.sqrt(2 * math.pi))
        # Truncated between 0 and 1
        lDensity /= (math.erf((1 - mu) / (sigma * math.sqrt(2))) - math.erf((- mu) / (sigma * math.sqrt(2)))) / 2
    else:
        sys.exit("Warning: The distribution of type should be 'uniform' or 'normal'")

    # Initial values
    alphas = np.ones((n, n))
    values = np.repeat(0., n)
    uDensity = np.repeat(0., n)

    # Computing the payoffs for all the types combinations
    payoffs = np.empty([n, n])
    for i in range(n):
        x = contributions[i]
        for j in range(n):
            y = contributions[j]
            payoffs[i,j] = production_function(x, y)


    listAllAlphas = [alphas.tolist()]
    keepIterating = True

    while keepIterating:

        # Updating the unemployment density
        # """ Fixed point algorithm """
        tol = 1e-12
        e = 1
        uPrev = uDensity
        while(e > tol):
            uDensity = delta * lDensity / (delta + rho * np.dot(alphas, uPrev) / n)  # fixed point iteration
            e = np.linalg.norm(uPrev - uDensity)
            uPrev = uDensity

        # Updating the values
        P = alphas * uDensity + np.identity(n) * ((n / theta) + np.dot(alphas, uDensity))
        q = np.dot(alphas * payoffs, uDensity)
        values = np.dot(np.linalg.inv(P), q)


        # Updating the matching set
        newAlphas = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                if payoffs[i,j] >= values[i] + values[j]:
                    newAlphas[i,j] = 1
        print(n**2 - (newAlphas == alphas).sum())

        # Checking if convergence, or infinite loop
        if (newAlphas == alphas).all():
            isConvergence = True
            keepIterating = False
        elif newAlphas.tolist() in listAllAlphas:
            isConvergence = False
            keepIterating = False
        else:
            alphas = newAlphas
            listAllAlphas.append(alphas.tolist())

    if isConvergence:
        print("Algorithm converged.\n")
        plot_matching_set(alphas, n, figName, distribution, contributions, lDensity)
    else:
        print("Infinite loop. Algorithm fails to converge.\n")










def plot_matching_set(alphas, n, figName, distribution, contributions, lDensity):
    colorMatching = "Blues"
    X = np.linspace(1/n/2, 1-1/n/2, n)
    Y = X
    levels = [0.1, 1]
    plt.figure(figsize=(10, 10))
    plt.rc('axes', labelsize=40)
    plt.rc('xtick', labelsize=30)
    plt.rc('ytick', labelsize=30)


    if distribution == "uniform":
        plt.contour(X, Y, alphas, levels, colors='k')
        plt.contourf(X, Y, alphas, levels, cmap=colorMatching)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xticks(np.arange(0, 1.1, 0.2))
        plt.yticks(np.arange(0, 1.1, 0.2))
        plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%g'))
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%g'))
        plt.gca().tick_params(axis='x', pad=10)
        plt.gca().tick_params(axis='y', pad=10)
        plt.xlabel('x')
        plt.ylabel('y')

    else:
        # Defining the 3 zones
        left, width = 0.1, 0.65
        bottom, height = 0.1, 0.65
        bottom_h = left_h = left + width + 0.02
        rect_set = [left, bottom, width, height]
        rect_histx = [left, bottom_h, width, 0.2]
        rect_histy = [left_h, bottom, 0.2, height]
        axSet = plt.axes(rect_set)
        axHistx = plt.axes(rect_histx)
        axHisty = plt.axes(rect_histy)

        # Plotting the matching set and the two density functions
        axSet.contour(X, Y, alphas, levels, colors='k')
        axSet.contourf(X, Y, alphas, levels, cmap=colorMatching)
        axHistx.axis('off')
        axHisty.axis('off')
        axHistx.plot(contributions, lDensity)
        axHistx.fill_between(contributions, 0, lDensity, alpha = 0.2)
        axHisty.plot(lDensity, contributions)
        axHisty.fill_betweenx(contributions, 0, lDensity, alpha = 0.2)
        axHistx.set_xlim((0, 1))
        axHisty.set_ylim((0, 1))
        axSet.set_xlim((0, 1))
        axSet.set_ylim((0, 1))
        axSet.set_xticks(np.arange(0, 1.1, 0.2))
        axSet.set_yticks(np.arange(0, 1.1, 0.2))
        axSet.xaxis.set_major_formatter(FormatStrFormatter('%g'))
        axSet.yaxis.set_major_formatter(FormatStrFormatter('%g'))
        axSet.tick_params(axis='x', pad=10)
        axSet.tick_params(axis='y', pad=10)
        axSet.set_xlabel('x')
        axSet.set_ylabel('y')

    plt.savefig("../figures/" + figName, bbox_inches='tight', pad_inches=0)
    plt.close()





if __name__ == '__main__':
    # If run_TU.py is run independently, a simulation is run with the following parameters
    n = 500
    delta = 1
    rho = 100
    r = 1
    production_function = lambda x,y : x * y
    # Here choose a name for the figure
    figName = "matching_set_TU.pdf"
    find_equilibrium_TU(n, delta, rho, r, production_function, figName, "normal", 0.5, 0.1)
