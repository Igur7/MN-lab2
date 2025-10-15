import numpy as np
import matplotlib.pyplot as plt
import string
import random

def compare_plot(x1, y1, x2, y2, xlabel, ylabel, title, label1, label2):
    # Sprawdzenie poprawności danych
    if (x1.shape != y1.shape or x2.shape != y2.shape or
        min(x1.shape) == 0 or min(x2.shape) == 0):
        return None

    # Tworzenie obiektu wykresu
    fig, ax = plt.subplots()

    # Pierwsza seria – niebieska linia, grubość 4
    ax.plot(x1, y1, color='blue', linewidth=4, label=label1)

    # Druga seria – czerwona linia, grubość 2
    ax.plot(x2, y2, color='red', linewidth=2, label=label2)

    # Ustawienia wykresu
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend()
    ax.grid(True)

    return fig


def parallel_plot(x1, y1, x2, y2, x1label, y1label, x2label, y2label, title, orientation=None):
    if (x1.shape != y1.shape or x2.shape != y2.shape or
        min(x1.shape) == 0 or min(x2.shape) == 0):
        return None
    
    if (
    len(x1) != len(y1)
    or len(x2) != len(y2)
    or len(x1) == 0
    or len(x2) == 0
    or len(x1) != len(x2) 
    ):
        return None

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(x1, y1, 'b', label=y1label)
    ax1.set(xlabel=x1label, ylabel=y1label)
    ax1.set_title(f'{title} - {y1label}')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(x2, y2, 'r', label=y2label)
    ax2.set(xlabel=x2label, ylabel=y2label)
    ax2.set_title(f'{title} - {y2label}')
    ax2.legend()
    ax2.grid(True)

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

    return fig


def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    if x.shape != y.shape or min(x.shape)==0:
        return None
    fig, ax = plt.subplots()
    ax.plot(x, y, 'g', label=ylabel)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend()
    if log_axis == 'x':
        ax.set_xscale('log')
    elif log_axis == 'y':
        ax.set_yscale('log')
    elif log_axis == 'xy':
        ax.set_xscale('log')
        ax.set_yscale('log')
    return fig
