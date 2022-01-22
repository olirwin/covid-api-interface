from datetime import datetime

from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request) :

    body = {
      "start_date": "2020-06-20",
      "end_date": "2022-01-22",
      "region": "FRA"
    }
    response = requests.post("http://127.0.0.1:8000/api/v1/covid/data", json = body)

    data = json.loads(response.content.decode("UTF-8"))
    data_points = data["body"]["data"]

    predicted = [[datetime.timestamp(datetime.strptime(el["date"], "%Y-%m-%d")) * 1000, el["cases"]]
                for el in data_points if el["predicted"]]

    existing = [[datetime.timestamp(datetime.strptime(el["date"], "%Y-%m-%d")) * 1000, el["cases"]]
                for el in data_points if not el["predicted"]] + [predicted[0]]

    return render(request, "index.html",
                  context = {
                      "existing" : existing,
                      "predicted" : predicted,
                      "raw" : json.dumps(data_points),
                      "start" : "2021-06-20",
                      "end" : "2022-01-22",
                      "middle" : "2022-01-18"
                  })


