from IO.Input import Input
from solver.Solver import solve
from IO.Output import Output


def main():
    params = Input()
    params.retrieve_input()
    visualizer = Output()
    x = solve(params.x0, params.t, params.mass, params.chute_manager)
    visualizer.visualize(x, params.t)


if __name__ == '__main__':
    main()
