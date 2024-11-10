# Balanced Allocation. Assignment 2 Randomized Algorithms
## Overview

This project consists of various Python scripts that simulate different balanced allocation strategies and analyze the resulting gap between the maximum load of a bin and the expected load. The goal is to compare and visualize the results of several allocation strategies, such as the "one-choice," "two-choice," and "partial information" methods, among others. The project is structured into different files, each focusing on a specific strategy and its corresponding analysis. The core functionality is implemented in the functions.py file, while other scripts conduct experiments and generate plots to visualize the results.

## Files Overview
### functions.py

Contains the core functions used in the simulations. It defines the following:

#### Helper Functions for Ball Distribution:
    get_bucket_two_choice(m, board): Randomly selects two bins and chooses the emptiest one.
    get_bucket_one_plus_beta_choice(m, beta, board): A hybrid strategy with probability beta of performing one_choice and (1-beta) of performing two_choice for each ball.
    get_bucket_partial_information(m, board): Chooses a bin based on partial information (median of the board).
    get_bucket_partial_information_2(m, board): Chooses a bin based on more refined partial information (percentiles and median).

#### Main Allocation Functions:
    one_choice(n, m, board): One-choice method for distributing balls into bins.
    two_choice(n, m, board): Two-choice method for distributing balls into bins.
    one_plus_beta_choice(beta, n, m, board): One plus beta-choice method with a given beta parameter.
    b_batched(n, m, b, board): Batched method, processes balls in groups (batches).
    partial_information(n, m, board): Allocation method using partial information (median-based).
    partial_information_2(n, m, board): Refined partial information method, considering percentiles.

#### Plotting Functions:
    plot(n_values, Gs, m, method): Plots the average gap (G) as a function of the number of balls (n) for a given method.
    b_batched_plot(n_values, Gs, m, b, method): Similar to plot(), but for batched experiments, adding a discountinuos line at every n multiple of b (size of the batch).

### one_choice.py

This file runs an experiment using the one-choice method for ball distribution and plots the average gap (G) over several repetitions.
### two_choice.py

Runs an experiment using the two-choice method for ball distribution and plots the average gap (G) over several repetitions.
### one_plus_beta_choice.py

Conducts experiments using the one plus beta-choice method with various beta values (1/3, 1/2, 2/3). It generates plots for each beta setting.
### b-batched.py

Experiments with the b-batched method. The balls are distributed in batches, and the plot visualizes the average gap for different batch sizes (b), such as m, 5m, 10m, and 20m.
### partial_information.py

Simulates the partial information methods (1-partial and 2-partial) where the ball selection process is based on partial information of the bins' states. It plots the average gap for each strategy.
## Installation Requirements

To run this project, you need to have Python 3.x installed, along with the following libraries:

    matplotlib: For plotting the results.
    numpy: For numerical calculations, particularly for percentiles and handling arrays.
    statistics: For calculating medians.
    random: for generating random values.

You can install the necessary libraries by running:

pip install matplotlib, numpy, statistics, random

## Usage

Each of the Python scripts (e.g., one_choice.py, two_choice.py, etc.) can be run individually to conduct experiments with different ball distribution methods. The script will automatically execute the corresponding simulation and generate a plot showing the average gap (G) of T experiments against the number of balls (n).
### Example: Running an Experiment

To run the one-choice experiment, execute the one_choice.py script:

python one_choice.py

This will:

    Simulate the one-choice process for distributing balls into bins.
    Repeat the experiment for different numbers of balls.
    Plot the average gap against the number of balls.

Plots

The plots will show:

    The average gap (G), which represents the difference between the most loaded bin and the expected number of balls per bin.
    Highlights for specific points like n = m (red) and n = m^2 (green), as well as the maximum gap observed across all repetitions (blue).

## Parameters

Each script has the following parameters that can be adjusted:

    T: The number of repetitions for the experiment.
    increment: The step size for the number of balls.
    n: The starting number of balls.
    m: The number of bins.
    b: The batch size (only for batched methods).
    beta: The parameter controlling the randomization in the one-plus-beta method.


## License

This project is open-source and available under the MIT License.


