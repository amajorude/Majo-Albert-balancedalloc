from functions import partial_information, partial_information_2, plot


T = 100             # number of repetitions of the experiment 
m = 40              # number of bins
n = 10              # number of balls
increment = 10      # increment the number of balls

Gs = []             # save the average gap of the T experiments for each value of n
n_values = []       # save the values of n to plot 

while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        G += partial_information(n, m, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

plot(n_values, Gs, m, '1 question partial information two-choice')


Gs = []
n_values = []
n = 10

while n <= m**2:
    G = 0
    for j in range(T):
        board = [0 for x in range(m)] 
        G += partial_information_2(n, m, board)
    Gs.append(G/T)
    n_values.append(n)  # Keep track of n values
    n += increment

plot(n_values, Gs, m, '2 question partial information two-choice')