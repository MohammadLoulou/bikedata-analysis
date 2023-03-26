import pandas as pd


class CityBikeData:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def generate(self):
        dict_infos = {}
        self.clean()
        # dict_infos["number_ride"] = self.rides_number(self.df)
        dict_infos["average"] = self.average_duration()
        dict_infos["most_popular_station_start"] = self.most_popular_station_start()

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
            return count["docked_bikes"]
        elif "total" in bike_type:
            return self.df["rideable_types"].count()

    def average_duration(self):
        self.df["duration"] = self.df["ended_at"] - self.df["started_at"]
        average = self.df["duration"].mean()
        return average

    def most_popular_station_start(self):
        return self.df["start_station_name"].value_counts()[0]

    def most_popular_station_start(self):
        return self.df["end_station_name"].value_counts()[0]


if __name__ == "__main__":
    JC = CityBikeData("JC-202302.csv")
    JC.clean()
