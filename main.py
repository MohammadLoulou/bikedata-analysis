from city_bike_data import CityBikeData

JC = CityBikeData("JC-202302.csv")
JC.clean()

print(JC.rides_number("classic"))
