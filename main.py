from city_bike_data import CityBikeData
from generate_graph import GenerateGraph

JC = CityBikeData("JC-202302.csv")


if __name__ == "__main__":
    JC.generate()
