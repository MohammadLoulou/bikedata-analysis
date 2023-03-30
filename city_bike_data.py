import pandas as pd
import matplotlib.pyplot as plt


class CityBikeData:
    def __init__(self, filename, city):
        try:
            self.df = pd.read_csv(filename)
        except Exception as e:
            print("File not found")
        self.city = city
        self.clean()

    def generate(self):
        dict_infos = {}
        dict_infos["city"] = self.city
        dict_infos["classic_ride"] = self.rides_number("classic")
        dict_infos["electric_ride"] = self.rides_number("electric")
        dict_infos["docked_ride"] = self.rides_number("docked")
        dict_infos["total_ride"] = self.rides_number("total")
        dict_infos["average"] = self.average_duration()
        dict_infos["most_popular_station_start"] = self.start_station_id()[0]
        dict_infos["most_popular_station_end"] = self.end_station_id()[0]
        dict_infos["members"] = self.number_members()["member"]
        dict_infos["casual"] = self.number_members()["casual"]

        return dict_infos

    def clean(self):
        self.df["started_at"] = pd.to_datetime(self.df["started_at"])
        self.df["ended_at"] = pd.to_datetime(self.df["ended_at"])
        self.df.dropna(inplace=True)

    def rides_number(self, bike_type="total"):
        count = self.df["rideable_type"].value_counts()
        if "classic" in bike_type:
            return count["classic_bike"]
        elif "electric" in bike_type:
            return count["electric_bike"]
        elif "docked" in bike_type:
            return count["docked_bike"]
        elif "total" in bike_type:
            return self.df["rideable_type"].count()

    def average_duration(self):
        self.df["duration"] = self.df["ended_at"] - self.df["started_at"]
        average = self.df["duration"].mean()
        return average

    def start_station_id(self):
        dataframe = self.df["start_station_name"].value_counts()
        return dataframe

    def end_station_id(self):
        dataframe = self.df["end_station_name"].value_counts()
        return dataframe

    def most_popular_stations(self):
        start_station = self.data["start_station_name"].value_counts().idxmax()
        end_station = self.data["end_station_name"].value_counts().idxmax()
        return start_station, end_station

    def number_members(self):
        members = self.df["member_casual"].value_counts()
        return members


if __name__ == "__main__":
    jc = CityBikeData("JC-202302.csv")
    df = jc.df
