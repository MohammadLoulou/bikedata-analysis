from city_bike_data import CityBikeData
from generate_graph import GraphGenerator
from jinja2 import Environment, FileSystemLoader


jc = CityBikeData("JC-202302.csv")

# JC = CityBikeData("JC-202302.csv")
gg = GraphGenerator()

if __name__ == "__main__":
    # gg.generate()
    dic = jc.generate()

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("template.html")

    filename = "report.html"
    context = dic
    with open(filename, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))
        print(f"... wrote {filename}")
