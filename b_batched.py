from functions import b_batched, b_batched_plot

T = 100 # number of repetitions of the experiment
increment = 10 # number of balls
n = 10
m = 40 # number of bins

Gs = []
n_values = []

b = m

while n <= m**2:
    G = 0
    for j in range(T): 
        board = [0 for x in range(m)] 
        G += b_batched(n, m, b, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

b_batched_plot(n_values, Gs, m, b, 'm-batched two-choice')

Gs = []
n_values = []
n = 10

b = 5*m

while n <= m**2:
    G = 0
    for j in range(T): 
        board = [0 for x in range(m)] 
        G += b_batched(n, m, b, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

b_batched_plot(n_values, Gs, m, b, '5m-batched two-choice')

Gs = []
n_values = []
n = 10

b = 10*m

while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)]  
        G += b_batched(n, m, b, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

b_batched_plot(n_values, Gs, m, b, '10m-batched two-choice')

Gs = []
n_values = []
n = 10

b = 20*m

while n <= m**2:
    G = 0
    for j in range(T): 
        board = [0 for x in range(m)] 
        G += b_batched(n, m, b, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

b_batched_plot(n_values, Gs, m, b, '20m-batched two-choice')