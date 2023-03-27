from city_bike_data import CityBikeData
import matplotlib.pyplot as plt

JC = CityBikeData("JC-202302.csv")


class GenerateGraph:
    def generate_start_id_graph(self):
        """
        Diagramme en bars pour les start id
        """
        start_id = CityBikeData.start_station_id()
        start_id.plt.bar()

        return start_id

    def generate_end_id_graph(self):
        """
        Diagramme en bars pour les end id
        """
        end_id = CityBikeData.end_station_id()

        return end_id
