from IO.Input import getInput
from solver.Solver import solve
from IO.Output import visualize


def main():
    mass, chutes, x0, t = getInput()
    args = (mass, chutes)
    res = solve(x0, t, args)
    visualize(res)
