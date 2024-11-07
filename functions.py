import random 
import matplotlib.pyplot as plt

def plot(n_values, Gs, n_0, m, method):
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
    plt.title(f"Average Gap in {method} Process")
    plt.grid(True)
    plt.legend()
    plt.show()


def one_choice(n, m, board):  
    for i in range(n):
        x = random.randint(0, m-1) # randomly select a bin for every ball
        board[x] += 1 
    return max(board) - n/m        # return the gap

def two_choice(n, m, board):               
    for i in range(n):
        x1, x2 = random.sample(range(m), 2)     # for each ball select  randomly two possible bins and choose the emptiest one
        if board[x1] > board[x2]:
            x = x2
        elif board[x2] > board[x1]: 
            x = x1
        else: 
            x = random.choice([x1, x2])
        board[x] += 1
    return max(board) - n/m                     # return the gap

def one_plus_beta_choice(beta, n, m, board):
    for i in range(n):
        if random.random() < beta:
            x = random.randint(0, m-1)
            board[x] += 1
        else:
            x1, x2 = random.sample(range(m), 2)
            if board[x1] > board[x2]:
                x = x2
            elif board[x2] > board[x1]: 
                x = x1
            else: 
                x = random.choice([x1, x2])
            board[x] += 1
    return max(board) - n/m

def b_batched(n, m, b, board):
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
    return max(board) - n/m