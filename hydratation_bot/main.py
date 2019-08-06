import json
import os
import time

import requests
import slack
from dotenv import load_dotenv

load_dotenv()

openwthr_api_key = os.getenv("OPENWTHR_API_KEY", None)
city_name = os.getenv("CITY", "Paris")
slack_hook_url = os.getenv("SLACK_HOOK_URL", None)

openwthr_base_url = "http://api.openweathermap.org/data/2.5/weather?"
openwthr_url = f"{openwthr_base_url}appid={openwthr_api_key}&q={city_name}"

def get_temp(url):
    """
    Get current temperature outside for a given city
    """
    response = requests.get(url)
    obj = response.json()
    print(obj)
    current_temp = None
    if not obj["cod"] in [404, 401]:
        wthr_obj = obj["main"]
        current_temp = wthr_obj["temp"]

    return current_temp

def slack_post(msg, hook_url):
    """
    Post a message on a given slack channel
    """
    requests.post(
    hook_url,
    data=json.dumps(
        {"text": msg}
    ),
    headers={'Content-Type': 'application/json'}
    )

def main():
    current_temp = get_temp(openwthr_url)
    print(current_temp)
    if 25 < current_temp < 50:
        msg = f"""
        It's currently {current_temp} outside, in {city_name}.\n
        Stay hydrated :droplet:
        """
        slack_post(msg, slack_hook_url)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(
            4*60*60
        )