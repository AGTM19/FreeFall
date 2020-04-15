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
    #list = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    #print(list[1][0])
