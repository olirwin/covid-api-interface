import json
import os

import requests
from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
from datetime import date, timedelta, datetime

from .forms import ChooseParamsDataForm


load_dotenv()


class HomePageView(View) :

    def get(self, request) :

        # Get all data until a couple of days ago
        base_url = os.getenv("BASE_API_URL")
        endpoint = f"{base_url}/api/v1/covid/data"

        end_date = date.today() - timedelta(days = 3)

        params = {
            "end_date" : end_date
        }

        response = requests.get(endpoint, params = params)

        data = json.loads(response.content.decode("UTF-8"))
        data_points = data["body"]["data"]

        def make_timestamp(from_date : str) -> int :
            str_date = datetime.strptime(from_date, "%Y-%m-%d")
            return int(str_date.timestamp() * 1000)

        existing = [[make_timestamp(el["date"]), el["cases"]] for el in data_points]

        context = {
            "existing" : existing,
            "start" : date(2020, 6, 1).strftime("%Y-%m-%d"),
            "end" : end_date.strftime("%Y-%m-%d")
        }

        return render(request, template_name = "index.html", context = context)
