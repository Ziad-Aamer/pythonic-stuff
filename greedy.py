"""
Greedy algorithms: 
    * Idea: at each step you pick the locally optimal solution,
    and you hope to end up with a globally optiomal solution.
    
    * Greedy aren't perfect, but they are pretty close.

Approximation algorithms:
    * Used when the exact solution will take too much time.
    * Judged by how: 1- Fast and 2- Close to the optimal solution.

"""


# The set-covering problem using a greedy approximation algorithm:
def get_minimum_number_of_stations_greedy(stations, states_needed):
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        print(states_covered)
        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


def test_get_minimum_stations():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    min_stations_list = get_minimum_number_of_stations_greedy(stations, states_needed)

    print(min_stations_list)
