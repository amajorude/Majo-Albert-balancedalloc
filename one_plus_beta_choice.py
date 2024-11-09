from functions import one_plus_beta_choice, plot

T = 100 # number of repetitions of the experiment
increment = 10 # number of balls
n = 10
m = 40 # number of bins

Gs = []
n_values = []

beta = 1/3

while n <= m**2:
    G = 0
    for j in range(T):  
        board = [0 for x in range(m)] 
        G += one_plus_beta_choice(beta, n, m, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

plot(n_values, Gs, m, '(1+1/3)-choice')

beta = 1/2

Gs = []
n_values = []
n = 10

while n <= m**2:
    G = 0
    for j in range(T):  
        board = [0 for x in range(m)] 
        G += one_plus_beta_choice(beta, n, m, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

plot(n_values, Gs, m, '(1+1/2)-choice')

beta = 2/3

Gs = []
n_values = []
n = 10

while n <= m**2:
    G = 0
    for j in range(T):  
        board = [0 for x in range(m)] 
        G += one_plus_beta_choice(beta, n, m, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

plot(n_values, Gs, m, '(1+2/3)-choice')
