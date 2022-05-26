import json
import pickle
import csv

s = {
  100: "test value",
  "test tuple": (1,2,3,4,5),
  "width": 3840,
  "height": 2100,
  "resolution": 90,
  "quality": 90,
  "settings": [
    {
      "filename": "_largePreview1.jpg",
      "seek": 10
    },
    {
      "filename": "_largePreview2.jpg",
      "seek": 35
    },
    {
      "filename": "_largePreview3.jpg",
      "seek": 70
    },
    {
      "filename": "_largePreview4.jpg",
      "seek": 95
    }
  ]
}

jsoned_str = json.dumps(s)
print(json.loads(jsoned_str))

with open("test.json", 'w') as f:
    json.dump(s, f)

with open("test.json", 'r') as f:
    new_object = json.load(f)

print(new_object)
print(new_object["test tuple"])

print(pickle.dumps(s))
print(pickle.dumps(print))

with open("test.pickle", 'wb') as f:
    pickle.dump(print, f)

with open("test.pickle", 'rb') as f:
    new_print = pickle.load(f)

print(new_print)
new_print("hello from new copy of the print")

data_v1 = {"model":["80 1.6 Specs", "80 1.6 Specs"], "year":[1986, 1993], "horsepower":[69, 102], "engine size": ["1595 cm", "1595 cm"]} 

data_v2 = [{"model":"80 1.6 Specs", "year":1986, "horsepower":69, "engine size":"1595 cm"},
            {"model":"80 1.6 Specs", "year":1993, "horsepower":102, "engine size":"1595 cm"}]

data_v1["model"][0]
data_v2[0]["model"]

headline = list(data_v1.keys())

with open("v1.json", 'w') as f:
    json.dump(data_v1, f)

with open("v2.json", 'w') as f:
    json.dump(data_v2, f)

with open("v1.pickle", 'wb') as f:
    pickle.dump(data_v1, f)

with open("v2.pickle", 'wb') as f:
    pickle.dump(data_v2, f)

with open("v1.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headline)
    for i in range(len(data_v1[headline[0]])):
        row = []
        for key in headline:
            row.append(data_v1[key][i])
        writer.writerow(row)

with open("v2.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headline)
    for item in data_v2:
        row = []
        for key in headline:
            row.append(item[key])
        writer.writerow(row)