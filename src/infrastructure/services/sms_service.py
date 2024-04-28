import threading

from decouple import config
from eskiz.client import SMSClient

# _email = config('email', '')
# _pswd = config('password', '')
_pswd = "qubn1dOBkbIrehYIAupXGoo4zJRjOaMiT2JlyEkn"
_email = "valleyboy.uz@gmail.com"
_client = SMSClient(
    api_url="https://notify.eskiz.uz/api/",
    email=_email,
    password=_pswd,
)


def send_sms(phone_number, data):
    phone_number = phone_number.replace('+', '')
    res = _client._send_sms(
        phone_number=phone_number, message=f"Your code is {data}"
    )
    print(res)

    return True
