from IO.Input import Input
from solver.Solver import solve
from IO.Output import Output
from Environment import Environment


# Environment.demo()

def main():
    params = Input()
    params.retrieve_input()
    visualizer = Output()
    t1, x1 = solve(params.x0, params.t, params.rocket_manager.mass, params.drag_manager)
    visualizer.visualize(x1, t1)

    #params = Input()
    #params.x0[1] = 105000
    #params.x0[2] = 318
    #t2, x2 = solve(params.x0, params.t, params.rocket_manager.mass, params.drag_manager)
    # visualizer.visualize(x2, t2)
    #visualizer.compare(x1, x2, t1, t2)


if __name__ == '__main__':
    main()