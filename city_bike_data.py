import pandas as pd


class CityBikeData:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)

    def generate(self, filename):
        pass

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


if __name__ == "__main__":
    JC = CityBikeData("JC-202302.csv")
    JC.clean()
