from functions import b_batched, plot

T = 250 # number of repetitions of the experiment
n_0 = 10 # number of balls
n = 10
m = 30 # number of bins

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
    n += n_0

plot(n_values, Gs, n_0, m, 'm-batched-choice')

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
    n += n_0

plot(n_values, Gs, n_0, m, '5m-batched-choice')

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
    n += n_0

plot(n_values, Gs, n_0, m, '10m-batched-choice')

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
    n += n_0

plot(n_values, Gs, n_0, m, '20m-batched-choice')