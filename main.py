from city_bike_data import CityBikeData
from generate_graph import GenerateGraph
import matplotlib.pyplot as plt


# JC = CityBikeData("JC-202302.csv")
GG = GenerateGraph()

if __name__ == "__main__":
    GG.generate()
