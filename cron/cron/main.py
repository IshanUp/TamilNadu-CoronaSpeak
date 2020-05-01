import requests
x = requests.get("https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv")
line  = '\n'.join(x.text.split("\n")[1:])
file = open("info.csv","w")
file.write(line)
