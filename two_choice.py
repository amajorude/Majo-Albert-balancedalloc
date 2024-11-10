from functions import two_choice, plot

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
        G += two_choice(n, m, board)
    Gs.append(G/T)
    n_values.append(n)  
    n += increment


plot(n_values, Gs, m, 'two-choice')         # plot the results