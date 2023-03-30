from city_bike_data import CityBikeData
import matplotlib.pyplot as plt
import pandas as pd
import calendar


class GraphGenerator:
    def __init__(self, city):
        self.city_bike = CityBikeData("JC-202302.csv", "jersey_city")
        self.df = self.city_bike.df
        self.city = city

    def generate(self):
        self.city_bike.generate()
        self.member_or_casual_graph()
        self.rideable_type_graph()
        self.rides_per_day_of_week_graph()
        self.hourly_rides_graph()
        self.most_popular_stations_graph()
        self.user_type_ride_duration_graph()

    def hourly_rides_graph(self):
        hours = self.df["started_at"].dt.hour
        plt.figure()
        plt.hist(hours, bins=24, edgecolor="black")
        plt.xticks(range(0, 24), range(0, 24))
        plt.xlabel("Hour of the day")
        plt.ylabel("Number of rides")
        plt.tight_layout()
        plt.savefig(f"{self.city}_hourly_rides.png")

    def most_popular_stations_graph(self):
        pop = self.df["start_station_id"].value_counts().head(10)
        plt.figure()
        pop.plot(kind="bar", legend="popular stations")
        plt.xlabel("Station's name")
        plt.ylabel("Number of rides")
        plt.title(f"Most popular stations of {self.city}")
        plt.tight_layout()
        plt.savefig(f"{self.city}_most_popular_stations.png")

    def rideable_type_graph(self):
        plt.figure()  # create new figure
        rideable_type = self.df["rideable_type"].value_counts()
        rideable_type.plot(
            kind="pie", title="rideable_type", autopct="%1.1f%%", ylabel=""
        )
        plt.tight_layout()
        plt.savefig(f"{self.city}_rideable_type_graph.png")

    def member_or_casual_graph(self):
        selected_columns = ["rideable_type", "member_casual"]
        ride_type = self.df[selected_columns].value_counts()
        type_pivot = (
            ride_type.reset_index()
            .pivot(index="rideable_type", columns="member_casual", values=0)
            .fillna(0)
        )
        fig = plt.figure("figure2")
        type_pivot.plot(kind="bar", ax=fig.gca())
        plt.tight_layout()
        plt.savefig(f"{ self.city }_rideable_type_by_user_category.png")

    def rides_per_day_of_week_graph(self):
        self.df["day_of_week"] = self.df["started_at"].dt.dayofweek
        rides_per_day_of_week = self.df.groupby("day_of_week")["ride_id"].count()

        fig = plt.figure("figure3")
        rides_per_day_of_week.sort_index().plot(kind="bar")
        plt.xlabel("Day_of_week")
        plt.ylabel("Total Rides")
        # plt.xticks(ticks=range(0, 7), labels=calendar.day_name[0:])
        plt.xticks(
            range(7),
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
        )

        plt.title(f"Total Rides per Day_of_week in {self.city}")
        plt.tight_layout()
        plt.savefig(f"{self.city}_total_rides_per_day_of_week.png")

    def user_type_ride_duration_graph(self):
        ride_duration = self.df.groupby("member_casual")["ride_duration"].mean()

        plt.figure(figsize=(5, 5))
        ride_duration.plot(kind="bar")
        plt.xlabel("User Type")
        plt.ylabel("Average ride duration in minutes")
        plt.title(f"Average ride duration per user type in {self.city}")
        plt.tight_layout()
        plt.savefig(f"{self.city}_average_ride_duration_user_type.png")
