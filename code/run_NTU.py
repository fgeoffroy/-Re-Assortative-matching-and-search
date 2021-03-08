import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import sys


def find_equilibrium_NTU(n, delta, rho, r, production_function, fig_name, tol=1e-12, distribution="uniform", mu=0.5, sigma=0.1):
    # market friction parameter
    psy = (r + delta) / rho

    # The distribution of types is discretized to perform a midpoint Riemann sum with n subdivisions
    contributions = np.linspace(1/n/2, 1-1/n/2, n)
    if distribution == "uniform":
        l_density = 1
    elif distribution == "normal":
        # Normal distribution
        l_density = np.exp(- ((contributions - mu) ** 2) / (2 * sigma ** 2)) / \
            (sigma * math.sqrt(2 * math.pi))
        # Truncated between 0 and 1
        l_density /= (math.erf((1 - mu) / (sigma * math.sqrt(2))) -
                     math.erf((- mu) / (sigma * math.sqrt(2)))) / 2
    else:
        sys.exit("Warning: The distribution of type should be 'uniform' or 'normal'")

    # Initial values
    alphas = np.ones((n, n))
    u_density = np.repeat(0., n)

    # Computing the payoffs for all the types combinations
    payoffs = np.empty([n, n])
    for i in range(n):
        x = contributions[i]
        for j in range(n):
            y = contributions[j]
            payoffs[i, j] = production_function(x, y)

    list_all_alphas = [alphas.tolist()]
    keep_iterating = True

    # Main loop
    while keep_iterating:

        # Updating the unemployment density. Equation (1)
        # """ Fixed point algorithm """
        e = sys.float_info.max
        u_prev = u_density
        while e > tol:
            u_density = delta * l_density / \
                (delta + rho * np.dot(alphas, u_prev) / n)  # fixed point iteration
            e = np.linalg.norm(u_prev - u_density)
            u_prev = u_density

        # Updating the values. Equation (2b)
        values = (np.dot(alphas * payoffs, u_density)) / (n * psy + (np.dot(alphas, u_density)))

        # Updating the matching set. Equation (3b)
        new_alphas = np.zeros([n, n])
        for i in range(n):
            for j in range(n):
                if payoffs[i, j] >= values[i] and payoffs[j, i] >= values[j]:
                    new_alphas[i, j] = 1
        # Printing the number of changes in the matrix alphas after update
        print(n**2 - (new_alphas == alphas).sum())

        # Checking if convergence, or infinite loop
        if (new_alphas == alphas).all():
            is_convergence = True
            keep_iterating = False
        elif new_alphas.tolist() in list_all_alphas:
            is_convergence = False
            keep_iterating = False
        else:
            alphas = new_alphas
            list_all_alphas.append(alphas.tolist())

    if is_convergence:
        print("Algorithm converged.\n")
        plot_matching_set(alphas, n, fig_name, distribution, contributions, l_density)
    else:
        print("Infinite loop. Algorithm fails to converge.\n")


def plot_matching_set(alphas, n, fig_name, distribution, contributions, l_density):
    color_matching = "Greens"
    X = np.linspace(1/n/2, 1-1/n/2, n)
    Y = X
    levels = [0.1, 1]
    plt.figure(figsize=(10, 10))
    plt.rc('axes', labelsize=40)
    plt.rc('xtick', labelsize=30)
    plt.rc('ytick', labelsize=30)

    if distribution == "uniform":
        plt.contour(X, Y, alphas, levels, colors='k')
        plt.contourf(X, Y, alphas, levels, cmap=color_matching)
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
        rect_hist_x = [left, bottom_h, width, 0.2]
        rect_hist_y = [left_h, bottom, 0.2, height]
        ax_set = plt.axes(rect_set)
        ax_hist_x = plt.axes(rect_hist_x)
        ax_hist_y = plt.axes(rect_hist_y)

        # Plotting the matching set and the two density functions
        ax_set.contour(X, Y, alphas, levels, colors='k')
        ax_set.contourf(X, Y, alphas, levels, cmap=color_matching)
        ax_hist_x.axis('off')
        ax_hist_y.axis('off')
        ax_hist_x.plot(contributions, l_density, color='g')
        ax_hist_x.fill_between(contributions, 0, l_density, color='g', alpha=0.2)
        ax_hist_y.plot(l_density, contributions, color='g')
        ax_hist_y.fill_between(l_density, 0, contributions, color='g', alpha=0.2)
        ax_set.set_xlim((0, 1))
        ax_set.set_ylim((0, 1))
        ax_set.set_xticks(np.arange(0, 1.1, 0.2))
        ax_set.set_yticks(np.arange(0, 1.1, 0.2))
        ax_set.xaxis.set_major_formatter(FormatStrFormatter('%g'))
        ax_set.yaxis.set_major_formatter(FormatStrFormatter('%g'))
        ax_set.tick_params(axis='x', pad=10)
        ax_set.tick_params(axis='y', pad=10)
        ax_set.set_xlabel('x')
        ax_set.set_ylabel('y')

    plt.savefig("./figures/" + fig_name, bbox_inches='tight', pad_inches=0)
    plt.close()


if __name__ == '__main__':
    # If run_NTU.py is run independently, a simulation is run with the following parameters
    tol = 1e-12     # Absolute tolerance level for the fixed-point iteration
    n = 500
    delta = 0.1
    rho = 30
    r = 0.3
    def production_function(x, y): return math.exp(x * y)
    # Here choose a name for the figure
    fig_name = "matching_set_NTU.pdf"
    find_equilibrium_NTU(n, delta, rho, r, production_function, fig_name, tol, "normal", 0.5, 0.1)
