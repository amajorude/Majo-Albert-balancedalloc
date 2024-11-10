from functions import b_batched, b_batched_plot


T = 250             # number of repetitions of the experiment 
m = 40              # number of bins
n = 10              # number of balls
increment = 10      # increment the number of balls

Gs = []             # save the average gap of the T experiments for each value of n
n_values = []       # save the values of n to plot 

b = m               # batch size

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