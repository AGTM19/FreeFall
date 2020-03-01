from Input import getInput
from Solver import solve
from Output import visualize


def main():
    args = getInput()
    res = solve(args)
    visualize(res)
