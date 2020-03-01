from IO.Input import getInput
from solver.Solver import solve
from IO.Output import visualize


def main():
    args = getInput()
    res = solve(args)
    visualize(res)
