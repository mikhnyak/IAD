import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

string_data = []
numeric_data = []


def sort_data(data, series):
    for i in series:
        if type(data[i][0]) == type('str'):
            string_data.append(i)
        else:
            numeric_data.append(i)


def hist(data):
    axes = data[numeric_data].plot(kind='hist', alpha=0.5, figsize=(11, 9), subplots=True)
    data[string_data].apply(pd.value_counts).plot(kind='bar', alpha=0.5, figsize=(11, 9), subplots=True)
    for ax in axes:
        ax.set_ylabel('Frequency')


def dot(data):
    axes = data[numeric_data].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
    data[string_data].apply(pd.value_counts).plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9),
                                                  subplots=True)
    for ax in axes:
        ax.set_ylabel('')


def scatter(data, cols):
    axes = data[cols].plot(kind='scatter', x=cols[0], y=cols[1], alpha=0.5, linestyle='None', figsize=(11, 9),
                           subplots=True)
    for ax in axes:
        ax.set_ylabel('')


def visualize(data, cols_plot):
    sort_data(data, cols_plot)
    if len(string_data) + len(numeric_data) == 2:
        t = input(
            'You have only two variables,  to see complex correlations between two variables you can use scatter.\n'
            'Enter kind of graphic (line, box, hist, scatter, dot):\n')
    else:
        t = input('Enter kind of graphic (line, box, hist, dot):\n')
    sns.set(rc={'figure.figsize': (11, 10)})
    if t == 'hist':
        hist(data)
    elif t == 'dot':
        dot(data)
    elif t == 'scatter':
        scatter(data, cols_plot)
    else:
        axes = data[numeric_data].plot(kind=t, figsize=(11, 9), subplots=True)
        data[string_data].apply(pd.value_counts).plot(kind=t, figsize=(11, 9), subplots=True)
        if t == 'kde':
            for ax in axes:
                ax.set_ylabel('density')
    plt.show()
