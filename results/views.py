import json
import os

import requests
from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
from datetime import date, timedelta, datetime

from .forms import ChooseParamsDataForm
from .models import Region
from .utils import make_timestamp, construct_title


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

        existing = [[make_timestamp(el["date"]), el["cases"]] for el in data_points]

        context = {
            "existing" : existing,
            "start" : date(2020, 6, 1).strftime("%Y-%m-%d"),
            "end" : end_date.strftime("%Y-%m-%d")
        }

        return render(request, template_name = "index.html", context = context)


class FetchDataView(View) :

    def get(self, request) :

        # Show form
        form = ChooseParamsDataForm(initial = {
            "region" : Region.objects.filter(name = "France")[0].id,
            "start_date" : date(2020, 6, 1),
            "end_date" : date.today() + timedelta(days = 10)
        })

        context = {
            "form" : form
        }

        return render(request, template_name = "get_data.html", context = context)

    def post(self, request) :
        form = ChooseParamsDataForm(request.POST)
        if form.is_valid() :

            start_date = date(2020, 6, 1)
            end_date = date.today() + timedelta(days = 10)
            region = "FRA"

            if form.cleaned_data["region"] :
                region = Region.objects.filter(id = form.cleaned_data["region"])[0]
                region = region.code
            if form.cleaned_data["start_date"] :
                start_date = form.cleaned_data["start_date"]
            if form.cleaned_data["end_date"] :
                end_date = form.cleaned_data["end_date"]

            # Get data
            base_url = os.getenv("BASE_API_URL")
            endpoint = f"{base_url}/api/v1/covid/data"

            params = {
                "start_date" : start_date,
                "end_date" : end_date,
                "region" : region
            }

            response = requests.get(endpoint, params = params)

            data = json.loads(response.content.decode("UTF-8"))
            data_points = data["body"]["data"]

            predicted = [[make_timestamp(el["date"]), el["cases"]]
                         for el in data_points if el["predicted"]]
            existing  = [[make_timestamp(el["date"]), el["cases"]]
                         for el in data_points if not el["predicted"]] + [predicted[0]]

            data = True

            middle_date = min([datetime.strptime(el["date"], "%Y-%m-%d") for el in data_points if el["predicted"]])

            context = {
                "existing" : existing,
                "predicted" : predicted,
                "start"    : start_date.strftime("%Y-%m-%d"),
                "end"      : end_date.strftime("%Y-%m-%d"),
                "middle" : middle_date,
                "data" : data,
                "form" : form,
                "region_title_info" : construct_title(region)
            }
            return render(request, template_name = "get_data.html", context = context)
