from city_bike_data import CityBikeData
import matplotlib.pyplot as plt
import pandas as pd


class GenerateGraph:
    def __init__(self):
        self.city_bike = CityBikeData("JC-202302.csv")

    def generate(self):
        self.city_bike.generate()
        self.graph_member_or_casual()
        self.rideable_type_graph()

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
        end_id.plt_bar()

        return end_id

    def hourly_rentals_graph(self):
        hours = self.city_bike.df["started_at"].dt.hour
        plt.hist(hours, bins=24, edgecolor="black")
        plt.xticks(range(0, 24), range(0, 24))
        plt.xlabel("Heure de la journée")
        plt.ylabel("Nombre de locations")
        return plt

    def most_popular_stations_graph(self):
        pop = self.city_bike.most_popular_stations_start()
        pop.plot(kind="bar", legend="popular stations")

    def rideable_type_graph(self):
        rideable_type = self.city_bike.df["rideable_type"].value_counts()
        rideable_type.plot(
            kind="pie", title="rideable_type", autopct="%1.1f%%", ylabel=""
        )
        plt.savefig("rideable_type_graph.png")
        plt.show()

    def graph_member_or_casual(self):
        selected_columns = ["rideable_type", "member_casual"]
        ride_type = self.city_bike.df[selected_columns].value_counts()
        type_pivot = (
            ride_type.reset_index()
            .pivot(index="rideable_type", columns="member_casual", values=0)
            .fillna(0)
        )
        fig = plt.figure("figure2")
        type_pivot.plot(kind="bar", ax=fig.gca())
        plt.savefig("member_or_casual_graph.png")
        plt.show()
