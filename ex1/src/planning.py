"""
Transport planning problem exercise.
"""
from z3 import *

example_problem = dict(
    nc=4,
    np=3,
    na=2,
    src=[2,1,0],
    dst=[0,3,2],
    start=[3,3]
)

simple_example = dict (
    nc = 2,
    np = 1,
    na = 1,
    src = [0],
    dst = [1],
    start = [0]
)

example_solution = dict(
    city_packages=[[[2], [1], [0], []],
                   [[2], [1], [0], []],
                   [[2], [], [], []],
                   [[2], [], [], []],
                   [[0], [], [], []],
                   [[0], [], [], []],
                   [[0], [], [2], [1]]],
    city_airplanes=[[[], [], [], [0, 1]],
                    [[], [0], [1], []],
                    [[], [0], [1], []],
                    [[0, 1], [], [], []],
                    [[1], [0], [], []],
                    [[], [], [1], [0]],
                    [[], [], [1], [0]]],
    airplane_packages=[[[], []],
                       [[], []],
                       [[1], [0]],
                       [[1], [0]],
                       [[1], [2]],
                       [[1], [2]],
                       [[], []]],
)


def print_problem(nc, np, na, src, dst, start):
    print "There are {} cities".format(nc)
    print "There are {} packages".format(np)
    print "There are {} airplanes".format(na)
    print

    assert len(src) == len(dst) == np
    assert len(start) == na

    for i in range(np):
        print "Package P{} starts at city C{} and should be transported to city C{}".format(
            i, src[i], dst[i])
    print

    for i in range(na):
        print "Airplane A{} starts at city C{}".format(i, start[i])
    print


def print_plan(city_packages, city_airplanes, airplane_packages):
    assert len(city_packages) == len(city_airplanes)
    assert len(city_packages) == len(airplane_packages)

    times = range(len(city_packages))
    nc = len(city_packages[0])
    print "plan:"

    def print_row(row):
        print ' | '.join([''] + ['{:^20}'.format(x) for x in row] + [''])

    def format_airplane(i, t):
        return 'A{}[{}]'.format(
            i,
            ','.join(['P{}'.format(j) for j in airplane_packages[t][i]])
        )

    print_row(['time'] + ['C{}'.format(i) for i in range(nc)])
    for t in times:
        print_row([t] + [
            ','.join(['P{}'.format(j) for j in city_packages[t][i]] +
            [format_airplane(j, t) for j in city_airplanes[t][i]])
            for i in range(nc)
        ])
    print


'''
Current Status:
    there is a basic structure for conditions...
    problems:
        1. need to strengthen starting conditions - for some reason the example problem they provided doesn't work well - for now I was trying to work with a simple example
        2. the loading of the packages to plane... the plane doesn't stay in the city

    we might need to change the entire way the conditions of the steps work.
    1 big loop of going over city,plane,package might not work...
    might have to split it to:
        1 loop for city/package
        1 loop for plane/package
        1 loop for city/plane?
        ... not sure about this one

'''

def get_transport_plan(nc, np, na, src, dst, start):

    t_max = nc*4
    # 1 plane could go to each city,
    # pick all packages,
    # then go each city and drop all relevant packages

    sol = None
    curr_max_time = 1
    while curr_max_time <= t_max:

        packageAtCity = [[[Bool('PackageAtCity_p{}_c{}_t{}'.format(p, c, t))
                for c in range(nc)]
               for p in range(np)]
              for t in range(curr_max_time+1)]

        packageOnPlane = [[[Bool('PackageOnPlane_p{}_a{}_t{}'.format(p, a, t))
              for a in range(na)]
              for p in range(np)]
              for t in range(curr_max_time+1)]

        planeAtCity = [[[Bool('AirplaneAtCity_ap{}_c{}_t{}'.format(p, c, t))
                for c in range(nc)]
               for p in range(np)]
              for t in range(curr_max_time+1)]


        s = Solver()

        # starting constraints

        # package is at start
        for pckg in range(np):
            for city in range(nc):
                if city == src[pckg]:
                    s.add(packageAtCity[0][pckg][city])
                else:
                    s.add(Not(packageAtCity[0][pckg][city]))

        #package is not on any plane at start
        for pckg in range(np):
            for airplane in range(na):
                s.add(Not(packageOnPlane[0][pckg][airplane]))

        # plane start city
        for plane in range(na):
            for city in range(nc):
                if city == start[plane]:
                    s.add(planeAtCity[0][plane][city])
                else:
                    s.add(Not(planeAtCity[0][plane][city]))


        #package movement
        for time in range(1,curr_max_time):
            #pckg will be in a city if
            # 1. same city as last turn
            # 2. dropped by a plane:
            #   a. package was on plane last turn
            #   b. plane has to stay in city
            #   c. plane was in city last turn
            # otherwise - not in city
            #for pckg in range(np):
            #    for city in range(nc):
            #        for plane in range(na):
            #            s.add(
            #                Or(
            #                    And(packageAtCity[time][pckg][city], packageAtCity[time-1][pckg][city]),
            #                    And(packageAtCity[time][pckg][city], packageOnPlane[time-1][pckg][plane], planeAtCity[time][plane][city], planeAtCity[time-1][plane][city]),
            #                    Not(packageAtCity[time][pckg][city])
            #                )
            #            )

            #package can be on a plane if
            #  1. same plane as last turn
            #  2. loaded by plane:
            #       a. package and plane in same city last turn
            #       b. plane has to stay in city
            #  otherwise - not on plane
            #for pckg in range(np):
            #    for plane in range(na):
            #        for city in range(nc):
            #            s.add(
            #                Or(
            #                    And(packageOnPlane[time][pckg][plane], packageOnPlane[time-1][pckg][plane]),
            #                    And(packageOnPlane[time][pckg][plane], packageAtCity[time-1][pckg][city], planeAtCity[time-1][plane][city], planeAtCity[time][plane][city]),
            #                    Or(Not(packageOnPlane[time][pckg][plane]), Not(planeAtCity[time][plane][city]))
            #                )
            #            )

            '''
            All things package can do:
            1. stay at same city -      requirements: was in city last turn
            2. stay on same plane -     requirements: was on plane last turn
            3. be dropped at a city -   requirements: a. on a plane that is in the city. package is on the plane
            4. be loaded to a plane -   requirements: a. plane & package on same city last turn. plane stays same city
            '''
            for pckg in range(np):
                for city in range(nc):
                    for plane in range(na):
                        s.add(
                            Or(
                                And(packageAtCity[time][pckg][city], packageAtCity[time-1][pckg][city], Not(packageOnPlane[time][pckg][plane])),
                                And(packageOnPlane[time][pckg][plane], packageOnPlane[time][pckg][plane], Not(packageAtCity[time][pckg][city])),
                                And(packageAtCity[time][pckg][city], planeAtCity[time][plane][city], planeAtCity[time-1][plane][city], packageOnPlane[time-1][pckg][plane], Not(packageOnPlane[time][pckg][plane])),
                                And(Not(packageAtCity[time][pckg][city]), packageOnPlane[time][pckg][plane], planeAtCity[time][plane][city], planeAtCity[time-1][plane][city], packageAtCity[time-1][pckg][city]),
                                And(Not(packageAtCity[time][pckg][city]), Not(packageOnPlane[time][pckg][plane]))
                            )
                        )

            #Plane can only be at one place at a time....

        #End package movement
            for plane in range(na):
                for city in range(nc):
                    for other_city in range(nc):
                        if city == other_city:
                            continue
                        s.add(
                            Or(
                                Not(planeAtCity[time][plane][city]),
                                And(planeAtCity[time][plane][city], Not(planeAtCity[time][plane][other_city]))
                            )
                        )

        #every package is where it should be at the end
        for pckg in range(np):
            pckg_start_loc = dst[pckg]
            for city in range(nc):
                if city == pckg_start_loc:
                    s.add(packageAtCity[curr_max_time-1][pckg][city])
                else:
                    s.add(Not(packageAtCity[curr_max_time-1][pckg][city]))

        # package is not on any plane at end
        for pckg in range(np):
            for airplane in range(na):
                s.add(Not(packageOnPlane[curr_max_time-1][pckg][airplane]))

        res = s.check()

        #print curr_max_time
        #print res

        #if curr_max_time == 4:
        #    print s

        if res == sat:
            m = s.model()
            #print m
            city_packages = [ [[] for i in range(nc)]  for j in range(curr_max_time) ]
            city_airplanes = [[[] for i in range(nc)] for j in range(curr_max_time)]
            airplane_packages = [[[] for i in range(na)] for j in range(curr_max_time)]

            for time in range(curr_max_time):
                for package in range(np):
                    for city in range(nc):
                        if is_true(m[packageAtCity[time][pckg][city]]):
                            city_packages[time][city].append(package)

            for time in range(curr_max_time):
                for plane in range(na):
                    for city in range(nc):
                        if is_true(m[planeAtCity[time][plane][city]]):
                            city_airplanes[time][city].append(plane)

            for time in range(curr_max_time):
                for package in range(np):
                    for plane in range(na):
                        if is_true(m[packageOnPlane[time][pckg][plane]]):
                            airplane_packages[time][plane].append(package)


            sol = {
                'airplane_packages' : airplane_packages,
                'city_packages' : city_packages,
                'city_airplanes' : city_airplanes
            }


            return sol

        curr_max_time = curr_max_time + 1

    return sol


if __name__ == '__main__':
    #print_problem(**example_problem)
    #print_plan(**example_solution)

    print_problem (**simple_example)

    sol = get_transport_plan(**simple_example)
    city_airplanes = sol.get('city_airplanes')
    city_packages = sol.get('city_packages')
    airplane_packages = sol.get('airplane_packages')
    print_plan(city_packages, city_airplanes, airplane_packages)
    #
    # Uncomment after you implement get_transport_plan:
    #
    # city_packages, city_airplanes, airplane_packages = get_transport_plan(**example_problem)
    # print
    # print_plan(city_packages, city_airplanes, airplane_packages)

    #
    # Add more tests here...
    #

#print example_solution
