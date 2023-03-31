import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
from phaseportrait import PhasePortrait2D
import typing as tp

def printEigenValuesAndVectors(lambda1, lambda2, h1, h2):
    print("Собственные векторы и собственные значения")
    print("lamda1: " )
    smp.pprint(lambda1)
    print('\n')
    print("h1: ")
    smp.pprint(h1)

    print('\n')

    print("lamda2: " )
    smp.pprint(lambda2)
    print('\n')
    print("h2: ")
    smp.pprint(h2)

def getEigenVectors(A: smp.Matrix):
    h1, h2 = A.eigenvects()
    lambda1, lambda2 = h1[0], h2[0]
    h1, h2 = h1[2][0], h2[2][0]
    printEigenValuesAndVectors(lambda1, lambda2, h1, h2)
    h1_f = smp.lambdify([], h1)
    h2_f = smp.lambdify([], h2)
    return h1_f(), h2_f()

def getSystem(A: smp.Matrix()):
    x, y = smp.symbols(r'x y')
    q = smp.Matrix([x, y])
    system_f = smp.lambdify([x, y], A * q)
    def systemFunction(x: float, y: float):
        return system_f(x, y)[0][0], system_f(x, y)[1][0]
    return systemFunction

def plotPhase(h1: np.ndarray, 
              h2: np.ndarray,
              systemFunction: tp.Callable, 
              name: str):
    saveDirectory = 'Plots/'
    savePath = saveDirectory + name + '.svg'
    phasePortrait = PhasePortrait2D(systemFunction, 
                                    [-5, 5], 
                                    Title = name, 
                                    xlabel = 'x', 
                                    ylabel = 'y',
                                    color = 'cool')
    fig, ax = phasePortrait.plot()
    xAx = np.linspace(-5, 5, 1000)
    if abs(h1[0][0]) > 1e-5:
        line_h1 = h1[1][0] * xAx / h1[0][0]
        ax.plot(xAx, 
            line_h1,
            label = 'h1',
            color = 'black',
            linewidth = 2)
    else:
        ax.axvline(0, 
                  label = 'h1',
                  color = 'black',
                  linewidth = 2)
    if abs(h2[0][0]) > 1e-5:
        line_h2 = h2[1][0] * xAx / h2[0][0]
        ax.plot(xAx, 
                line_h2,
                label = 'h2',
                color = 'black',
                linewidth = 2)
    else:
        ax.axvline(0, 
                  label = 'h2',
                  color = 'black',
                  linewidth = 2)
    ax.legend()
    plt.show()
    fig.savefig(savePath)
    
def __main__():
    print("Первая строка матрицы A: ")
    a, b = map(int, input().split())
    print("Вторая строка матрицы A: ")
    c, d = map(int, input().split())
    
    A = smp.Matrix([[a, b], [c, d]])
    print("Имя графика:")
    name = input()
    plotPhase(*getEigenVectors(A), getSystem(A), name)

__main__()
