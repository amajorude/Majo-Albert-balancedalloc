from functions import two_choice, plot

T = 100 # number of repetitions of the experiment
increment = 10 # number of balls
n = 10
m = 40 # number of bins

Gs = []
n_values = []
while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        G += two_choice(n, m, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment


plot(n_values, Gs, m, 'two-choice')