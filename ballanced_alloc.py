import random 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math

T = 250 # number of repetitions of the experiment
n_0 = 10 # number of balls
n = 10
m = 30 # number of bins

# ONE CHOICE
Gs = []
n_values = []
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        max_bin = 0
        ind_max = 0
        for i in range(n):
            x = random.randint(0, m-1)
            board[x] += 1
            max_bin = max(max_bin, board[x])  
        G += max_bin - n/m
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += n_0

plt.plot(n_values, Gs, marker='o', label="Average Gap")

# Highlight specific points with colors
highlight_points = {m: 'red', m**2: 'green'}
for n_val, color in highlight_points.items():
    if n_val in n_values:
        idx = n_values.index(n_val)
        plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
        plt.axvline(x=n_val, color=color, linestyle="--")
        label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
        plt.scatter([], [], color=color, label=label)

# Highlight the maximum G value in the plot
max_G = max(Gs)
max_idx = Gs.index(max_G)
plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

# Add labels, title, grid, and legend
plt.xlabel("Number of Balls")
plt.ylabel("Average Gap")
plt.title("Average Gap in One-Choice Process")
plt.grid(True)
plt.legend()
plt.show()

# TWO CHOICE
n = 10
Gs = []
n_values = []
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        max_bin = 0
        ind_max = 0
        for i in range(n):
            x1, x2 = random.sample(range(m), 2)
            if board[x1] > board[x2]:
                x = x2
            elif board[x2] > board[x1]: 
                x = x1
            else: 
                x = random.choice([x1, x2])
            board[x] += 1
            max_bin = max(max_bin, board[x])  
        G += max_bin - n/m
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += n_0

plt.plot(n_values, Gs, marker='o', label="Average Gap")

# Highlight specific points with colors
highlight_points = {m: 'red', m**2: 'green'}
for n_val, color in highlight_points.items():
    if n_val in n_values:
        idx = n_values.index(n_val)
        plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
        plt.axvline(x=n_val, color=color, linestyle="--")
        label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
        plt.scatter([], [], color=color, label=label)

# Highlight the maximum G value in the plot
max_G = max(Gs)
max_idx = Gs.index(max_G)
plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

# Add labels, title, grid, and legend
plt.xlabel("Number of Balls")
plt.ylabel("Average Gap")
plt.title("Average Gap in Two-Choice Process")
plt.grid(True)
plt.legend()
plt.show()

# 1 + beta CHOICE
## beta = 1/3
n = 10
Gs = []
n_values = []
beta = 1/3
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        max_bin = 0
        ind_max = 0
        for i in range(n):
            if random.random() < beta:
                x = random.randint(0, m-1)
                board[x] += 1
                max_bin = max(max_bin, board[x]) 
            else:
                x1, x2 = random.sample(range(m), 2)
                if board[x1] > board[x2]:
                    x = x2
                elif board[x2] > board[x1]: 
                    x = x1
                else: 
                    x = random.choice([x1, x2])
                board[x] += 1
                max_bin = max(max_bin, board[x])  
        G += max_bin - n/m
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += n_0

plt.plot(n_values, Gs, marker='o', label="Average Gap")

# Highlight specific points with colors
highlight_points = {m: 'red', m**2: 'green'}
for n_val, color in highlight_points.items():
    if n_val in n_values:
        idx = n_values.index(n_val)
        plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
        plt.axvline(x=n_val, color=color, linestyle="--")
        label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
        plt.scatter([], [], color=color, label=label)

# Highlight the maximum G value in the plot
max_G = max(Gs)
max_idx = Gs.index(max_G)
plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

# Add labels, title, grid, and legend
plt.xlabel("Number of Balls")
plt.ylabel("Average Gap")
plt.title("Average Gap in (1+1/3)-Choice Process")
plt.grid(True)
plt.legend()
plt.show()

## beta = 1/2
n = 10
Gs = []
n_values = []
beta = 1/2
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        max_bin = 0
        ind_max = 0
        for i in range(n):
            if random.random() < beta:
                x = random.randint(0, m-1)
                board[x] += 1
                max_bin = max(max_bin, board[x]) 
            else:
                x1, x2 = random.sample(range(m), 2)
                if board[x1] > board[x2]:
                    x = x2
                elif board[x2] > board[x1]: 
                    x = x1
                else: 
                    x = random.choice([x1, x2])
                board[x] += 1
                max_bin = max(max_bin, board[x])  
        G += max_bin - n/m
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += n_0

plt.plot(n_values, Gs, marker='o', label="Average Gap")

# Highlight specific points with colors
highlight_points = {m: 'red', m**2: 'green'}
for n_val, color in highlight_points.items():
    if n_val in n_values:
        idx = n_values.index(n_val)
        plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
        plt.axvline(x=n_val, color=color, linestyle="--")
        label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
        plt.scatter([], [], color=color, label=label)

# Highlight the maximum G value in the plot
max_G = max(Gs)
max_idx = Gs.index(max_G)
plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

# Add labels, title, grid, and legend
plt.xlabel("Number of Balls")
plt.ylabel("Average Gap")
plt.title("Average Gap in (1+1/2)-Choice Process")
plt.grid(True)
plt.legend()
plt.show()

## beta = 2/3
n = 10
Gs = []
n_values = []
beta = 2/3
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        max_bin = 0
        ind_max = 0
        for i in range(n):
            if random.random() < beta:
                x = random.randint(0, m-1)
                board[x] += 1
                max_bin = max(max_bin, board[x]) 
            else:
                x1, x2 = random.sample(range(m), 2)
                if board[x1] > board[x2]:
                    x = x2
                elif board[x2] > board[x1]: 
                    x = x1
                else: 
                    x = random.choice([x1, x2])
                board[x] += 1
                max_bin = max(max_bin, board[x])  
        G += max_bin - n/m
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += n_0

plt.plot(n_values, Gs, marker='o', label="Average Gap")

# Highlight specific points with colors
highlight_points = {m: 'red', m**2: 'green'}
for n_val, color in highlight_points.items():
    if n_val in n_values:
        idx = n_values.index(n_val)
        plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
        plt.axvline(x=n_val, color=color, linestyle="--")
        label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
        plt.scatter([], [], color=color, label=label)

# Highlight the maximum G value in the plot
max_G = max(Gs)
max_idx = Gs.index(max_G)
plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

# Add labels, title, grid, and legend
plt.xlabel("Number of Balls")
plt.ylabel("Average Gap")
plt.title("Average Gap in (1+2/3)-Choice Process")
plt.grid(True)
plt.legend()
plt.show()

# B-BATCHED
n = 10
Gs = []
b = m
n_values = []
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        for i in range(0, n, b):
            board_prime = [0 for x in range(m)]
            for k in range(b):
                x1, x2 = random.sample(range(m), 2)
                if board[x1] > board[x2]:
                    x = x2
                elif board[x2] > board[x1]: 
                    x = x1
                else: 
                    x = random.choice([x1, x2])
                board_prime[x] += 1
            board = [board[y] + board_prime[y] for y in range(m)]
        max_bin = max(board)  
        G += max_bin - n/m
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += n_0

plt.plot(n_values, Gs, marker='o', label="Average Gap")

# Highlight specific points with colors
highlight_points = {m: 'red', m**2: 'green'}
for n_val, color in highlight_points.items():
    if n_val in n_values:
        idx = n_values.index(n_val)
        plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
        plt.axvline(x=n_val, color=color, linestyle="--")
        label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
        plt.scatter([], [], color=color, label=label)

# Highlight the maximum G value in the plot
max_G = max(Gs)
max_idx = Gs.index(max_G)
plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

# Add labels, title, grid, and legend
plt.xlabel("Number of Balls")
plt.ylabel("Average Gap")
plt.title("Average Gap in Two-Choice Process")
plt.grid(True)
plt.legend()
plt.show()