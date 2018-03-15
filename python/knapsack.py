from argparse import ArgumentParser
from time import time


####################################################################
################ TODO your code here ###############################

def brute_force(items, values, weights, capacity):
    '''
    The brute force implementation for the 0-1 knapsack problem.

    :return: returns the best value-sum for the given problem
    '''
    best_value_sum = None #TODO
    return best_value_sum


def dynamic_programming(items, values, weights, capacity):
    '''
    The Dynamic Programming implementation for the 0-1 knapsack problem.

    :return: returns the best value-sum for the given problem
    '''
    best_value_sum = None #TODO
    return best_value_sum


####################################################################
################ TODO your additional functions here ###############



####################################################################


def parse_csv(fname):
    '''
    parses a csv file with the following format:

    , items, values, weights
    ,item_0, value_0, weight_0
    ,item_1, value_1, weight_1
      ...

    :param fname:
    :return: lists for items, values, weights
    '''
    with open(fname, "r") as f:
        lines = f.readlines()[1:]
        items = [int(line.split(",")[1]) for line in lines]
        values = [int(line.split(",")[2]) for line in lines]
        weights = [int(line.split(",")[3].replace("\n", "")) for line in lines]
    return items, values, weights


def print_results(result, runtime):
    '''
    prints results of the algorithms that were run.
    :param result:
    :param runtime:
    :return:
    '''
    for key in result.keys():
        print "\nAlgorithm: {}".format(key)
        print   "Result   : {}".format(float(result[key]))
        print   "Runtime  : {0:.4f} s".format(runtime[key])

    if len(result.keys()) == 2:
        ratio = runtime["brute_force"] / runtime["dynamic_programming"]
        print "\nYour Dynamic Programming implementation is {0:.2f} " \
              "times faster than the brute-force implementation.".format(ratio)

        if result.values()[0] != result.values()[1]:
            print "\nWARNING: Your implementations do not yield the same solutions!"


def parse_options():
    parser = ArgumentParser()
    # You should always have -b or -d (or both) active.
    parser.add_argument("-b", "--brute_force", required=False, default=False,
                        action="store_true",
                        help="Run the brute-force algorithm.")
    parser.add_argument("-d", "--dynamic_programming", required=False,
                        default=False, action="store_true",
                        help="Run the Dynamic Programming algorithm.")

    # Optional parameters
    parser.add_argument("-i", "--items", required=False,
                        default="reference_problem.csv",
                        help=".csv that describes the items."
                             "Please use the default setting for question 1.")
    parser.add_argument("-c", "--capacity", required=False,
                        default=50, type=int,
                        help="The capacity of the knapsack."
                             "Please use the default setting for question 1.")
    parser.add_argument("-r", "--rerun", required=False,
                        default=1, type=int,
                        help="Sets how often each algorithm is run."
                             "For measuring the time, it is advised to pick a "
                             "higher number than 1. For testing, you should use "
                             "the default.")

    options = parser.parse_args()
    if not (options.brute_force or options.dynamic_programming):
        print "You need to set the brute-force or dynamic programming flags." \
              "You can also set both!"
        sys.exit(1)

    return options


if __name__ == "__main__":
    options = parse_options()

    # problem definition
    items, values, weights = parse_csv(options.items)
    capacity = options.capacity

    runtime = {}
    result = {}

    # run the brute force implementation and time it
    if options.brute_force:
        start = time()
        for i in xrange(options.rerun):
            result["brute_force"] = \
                brute_force(items, values, weights, capacity)
        runtime["brute_force"] = (time() - start) / float(options.rerun)

    # run the dynamic programming implementation and time it
    if options.dynamic_programming:
        start = time()
        for i in xrange(options.rerun):
            result["dynamic_programming"] = \
                dynamic_programming(items, values, weights, capacity)
        runtime["dynamic_programming"] = (time() - start) / float(options.rerun)

    # visualize the results
    print_results(result, runtime)
