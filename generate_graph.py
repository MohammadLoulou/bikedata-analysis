from city_bike_data import CityBikeData
import matplotlib.pyplot as plt


class GraphGenerator:
    def __init__(self):
        self.city_bike = CityBikeData("JC-202302.csv")

    def start_id_graph(self):
        """
        Diagramme en bars pour les start id
        """
        start_id = self.city_bike.start_station_id()
        start_id.plt.bar()

        return start_id

    def end_id_graph(self):
        """
        Diagramme en bars pour les end id
        """
        end_id = self.city_bike.end_station_id()

        return end_id

    def hourly_rentals_graph(self):
        hours = self.city_bike.df["started_at"].dt.hour
        plt.hist(hours, bins=24, edgecolor="black")
        plt.xticks(range(0, 24), range(0, 24))
        plt.xlabel("Heure de la journée")
        plt.ylabel("Nombre de locations")
        return plt

    def most_popular_stations_graph(self):
        pop = self.city_bike.popular_start_stations()
        pop.plot(kind="bar", legend="popular stations")

    def rideable_type_graph(self):
        rideable_type = self.city_bike.df["rideable_type"].value_counts()
        rideable_type.plot(kind="pie", autopct="%1.1f%%", startangle=90, ylabel="")
