from datetime import datetime


def make_timestamp(from_date: str) -> int :
    str_date = datetime.strptime(from_date, "%Y-%m-%d")
    return int(str_date.timestamp() * 1000)


def construct_title(region_code: str) -> str :
    if region_code == "FRA" :
        return "en France"
    else :
        return f"dans le {region_code}"
