import os
import sys

from HillClimber import HillClimber

def main():
    if len(sys.argv) <= 1 or sys.argv[1] == None:
        sys.exit('need a secret message as first param')
    input_file = open(sys.argv[1], 'r')
    height_map = input_file.read().splitlines()

    hill_climber = HillClimber()
    n_steps = hill_climber.getMinStepsToGoal(height_map)
    if n_steps >= 0:
        print('need {} steps to reach the goal'.format(n_steps))
    else:
        print('no path found')

if __name__ == '__main__':
    main()