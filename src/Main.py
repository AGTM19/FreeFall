from IO.Input import Input
from solver.Solver import solve
from IO.Output import Output
from Environment import Environment


# Environment.demo()

def main():
    params = Input()
    params.retrieve_input()
    visualizer = Output()
    t, x = solve(params.x0, params.t, params.rocket_manager.mass, params.drag_manager)
    visualizer.visualize(x, t)
    print(x)


if __name__ == '__main__':
    main()