from IO.Input import Input
from solver.Solver import solve
from IO.Output import Output
import numpy

def main():
    params = Input()
    params.retrieve_input()
    visualizer = Output()
    x = solve(params.x0, params.t, params.mass, params.chute_manager)
    print(repr(x[:,0]))
    visualizer.visualize(x, params.t)


if __name__ == '__main__':
    main()
