# пункт 1
with open('cities.txt', 'r') as file:
    cities=[line.strip() for line in file]
with open('navigation.txt', 'r') as file:
        navigation = [list(map(int, line.split())) for line in file] 
#пункт 2=4
def path(cities, navigation):
    distance=0    
for i in range(len(cities)):
        for j in range(len(cities)):
            if navigation[i][j]!=0:
                print(cities[i], '->', navigation[i][j], '->', cities[j])
path(cities, navigation)
#пункт 5
def transfer(c1,c2,navigation,cities):
    for i in range(len(cities)):
        if navigation[c1][i]!=0 and navigation[c2][i]!=0 and i!=c1 and i!=c2:                print('pyt iz', cities[c1], 'v', cities[c2], 'cherez gorod', cities[i])
            return True
    print('net pyti c peresadkoi')
    return False
transfer(0,2,navigation,cities)
#пункт 6=7
from collections import deque
def longest_path(cities, navigation, start_city):
    queue = deque([(start_city, [start_city], 0)]) 
    max_distance = 0
    longest_path = []
    while queue:
        current_city, path, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
            longest_path = path
        for next_city in range(len(cities)):
            if navigation[current_city][next_city] != 0 and next_city not in path:
                queue.append((next_city, path + [next_city], distance + navigation[current_city][next_city]))
    print('iz',cities[start_city], 'pyt:')
    for i in range(len(longest_path) - 1):
        city1 = longest_path[i]
        city2 = longest_path[i + 1]
        distance = navigation[city1][city2]    
        print(cities[city1], '->', distance, '->', cities[city2])
    print('Itog:', max_distance)
 longest_path(cities, navigation, 0)
