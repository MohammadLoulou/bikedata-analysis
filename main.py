from city_bike_data import CityBikeData
from generate_graph import GraphGenerator
from jinja2 import Environment, FileSystemLoader
import pandas as pd


jc = CityBikeData("JC-202302.csv", "jersey_city")
gg = GraphGenerator("jersey_city")
dic = jc.generate()
gg.generate()
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("template.html")

filename = "report.html"
context = dic
with open(filename, mode="w", encoding="utf-8") as results:
    results.write(template.render(context))
    print(f"... wrote {filename}")
