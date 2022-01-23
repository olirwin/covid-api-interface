import json
import os

from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
from datetime import date, timedelta

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

        response = request.get(endpoint, params = params)

        data = json.loads(response.content.decode("UTF-8"))

        return render(request, template_name = "index.html")