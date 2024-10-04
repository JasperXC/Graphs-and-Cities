#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

int maxDistance = 0;

void findMaxRoute(int currentCity, int currentDistance, std::vector<int> visited, std::vector<std::vector<int>> distances, std::vector<std::string> cities) {
    if (currentDistance > maxDistance) {
        maxDistance = currentDistance;
    }

    for (int i = 0; i < cities.size(); i++) {
        if (distances[currentCity][i] != 0 && std::find(visited.begin(), visited.end(), i) == visited.end()) {
            visited.push_back(i);
            findMaxRoute(i, currentDistance + distances[currentCity][i], visited, distances, cities);
            visited.pop_back();
        }
    }
}

main() {
    std::ifstream citiesFile("cities.txt");
    std::ifstream navigationFile("navigation.txt");

    std::vector<std::string> cities;
    std::string city;
    std::map<std::string, int> cityIndex;
    int idx = 0;

    while (citiesFile >> city) {
        cities.push_back(city);
        cityIndex[city] = idx;
        idx++;
    }

    int n = cities.size();
    std::vector<std::vector<int>> distances(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            navigationFile >> distances[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        std::vector<int> visited;
        visited.push_back(i);
        findMaxRoute(i, 0, visited, distances, cities);
        std::cout << "Maximum route from " << cities[i] << ": " << maxDistance << std::endl;
        maxDistance = 0;
    }

    citiesFile.close();
    navigationFile.close();

    return 0;
}