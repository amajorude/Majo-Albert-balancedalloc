import random 
import matplotlib.pyplot as plt
from statistics import median
import numpy as np


def plot(n_values, Gs, m, method):
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


def b_batched_plot(n_values, Gs, m, b, method):
    plt.plot(n_values, Gs, marker='o', label="Average Gap")
    
    # Highlight specific points with colors for n = m and n = m^2
    highlight_points = {m: 'red', m**2: 'green'}
    for n_val, color in highlight_points.items():
        if n_val in n_values:
            idx = n_values.index(n_val)
            plt.scatter(n_values[idx], Gs[idx], color=color, s=100, zorder=5)
            plt.axvline(x=n_values[idx], color=color, linestyle="--")
            label = f"n = m, G ≈ {Gs[idx]:.2f}" if n_val == m else f"n = m^2, G ≈ {Gs[idx]:.2f}"
            plt.scatter([], [], color=color, label=label)

    # Highlight the maximum G value in the plot
    max_G = max(Gs)
    max_idx = Gs.index(max_G)
    plt.scatter(n_values[max_idx], max_G, color="blue", s=100, zorder=5)
    plt.axvline(x=n_values[max_idx], color="blue", linestyle="--")
    plt.scatter([], [], color="blue", label=f"Max G ≈ {max_G:.2f} at n = {n_values[max_idx]}")

    # Add dashed lines for each n divisible by b
    for i, n in enumerate(n_values):
        if n % b == 0:  # Check if n is divisible by b
            plt.axvline(x=n, color="gray", linestyle="--", linewidth=0.5)

    # Add labels, title, grid, and legend
    plt.xlabel("Number of Balls")
    plt.ylabel("Average Gap")
    plt.title(f"Average Gap in {method} Process")
    plt.grid(True)
    plt.legend()
    plt.show()
 

def get_bucket_two_choice(m, board):
    x1, x2 = random.sample(range(m), 2)     # for each ball select randomly two possible bins and choose the emptiest one
    if board[x1] > board[x2]:
        x = x2
    elif board[x2] > board[x1]: 
        x = x1
    else:                                   # break ties at random                
        x = random.choice([x1, x2])
    return x

def get_bucket_one_plus_beta_choice(m, beta, board):
    if random.random() < beta:                          # with probability beta apply the one_choice strategy
        x = random.randint(0, m-1)
    else:                                               # with probability (1-beta) apply the two_choice strategy
        x = get_bucket_two_choice(m, board)
    return x

def get_bucket_partial_information(m, board):
    median_board = median(board)
    x1, x2 = random.sample(range(m), 2)
    if board[x1] > median_board:
        if board[x2] > median_board:
            x = random.choice([x1, x2])                 # if both are over the median select at random
        else:                                           # if only x1 is, pick x2
            x = x2
    elif board[x2] > median_board:                      # if only x2 is, pick x1
        x = x1
    else:                                               # if both are under or equal the median pick bucket at random
        x = random.choice([x1, x2])
    return x

def get_bucket_partial_information_2(m, board):
    median_board = median(board)
    x1, x2 = random.sample(range(m), 2)
    value_1 = board[x1]
    value_2 = board[x2]
    if value_1 > median_board:
        if value_2 > median_board:                      # if both are over the median ask if they are in the top 75% most loaded
            if value_1 > np.percentile(board, 75):
                if value_2 > np.percentile(board, 75):
                    x = random.choice([x1, x2])
                else:
                    x = x2
            elif value_2 > np.percentile(board, 75):
                x = x1
            else:
                x = random.choice([x1, x2])
        else:
            x = x2
    elif value_2 > median_board:
        x = x1
    elif value_1 > np.percentile(board, 25):           # if both are under or equal the median ask if they are in the 25% least loaded
        if value_2 > np.percentile(board, 25):
            x = random.choice([x1,x2])
        else: 
            x = x2
    elif value_2 > np.percentile(board, 25):
        x = x1
    else:
        x = random.choice([x1,x2])
    return x
    


def one_choice(n, m, board):  
    for i in range(n):
        x = random.randint(0, m-1) # randomly select a bin for every ball
        board[x] += 1 
    return max(board) - n/m        # return the gap

def two_choice(n, m, board):               
    for i in range(n):
        x = get_bucket_two_choice(m, board)     # select a bin using the two_choice strategy
        board[x] += 1
    return max(board) - n/m                     # return the gap

def one_plus_beta_choice(beta, n, m, board):
    for i in range(n):
        x = get_bucket_one_plus_beta_choice(m, beta, board)     # select the bin using the one_plus_beta_strategy
        board[x] += 1
    return max(board) - n/m                                     # return the gap

def b_batched(n, m, b, board):
    for i in range(0, n, b):
        batch_size = min(b, n - i)
        board_prime = [0 for _ in range(m)]         # board to save the position of the batch without altering the initial bins
        for k in range(batch_size):
            x = get_bucket_two_choice(m, board)     # chose the bucket using two_choice without knowing the selection of the rest of the batch
            board_prime[x] += 1
        for y in range(m):
            board[y] += board_prime[y]              # update the load of the bins
    return max(board) - n/m                         # return the gap

def partial_information(n, m, board):
    for i in range(n):
        x = get_bucket_partial_information(m, board)    # chose the bin with partial information
        board[x] += 1
    return max(board) - n/m

def partial_information_2(n, m, board):
    for i in range(n):
        x = get_bucket_partial_information_2(m, board)  # chose the bin with 2 questions of partial information 
        board[x] += 1
    return max(board) - n/m