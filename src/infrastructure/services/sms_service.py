import threading

import requests
from decouple import config


class SmsService():
    login_url = "https://notify.eskiz.uz/api/auth/login"
    send_sms_url = "https://notify.eskiz.uz/api/message/sms/send"

    payload = {'email': 'valleyboy.uz@gmail.com',
               'password': 'qubn1dOBkbIrehYIAupXGoo4zJRjOaMiT2JlyEkn'}

    def __init__(self) -> None:
        self.token = self._get_token()

    def _get_token(self) -> str:
        response = requests.post(self.login_url, data=self.payload)
        if response.status_code == 200:
            return response.json()['data']['token']
        else:
            raise Exception("Failed to retrieve token")

    def _get_headers(self) -> dict:
        return {
            'Authorization': f"Bearer {self.token}"
        }

    def _send_sms_request(self, phone, text) -> requests.Response:
        phone_number = str(phone).replace('+', '')
        payload = {'mobile_phone': phone_number,
                   'message': text,
                   'from': '4546',
                   'callback_url': None}
        response = requests.post(
            self.send_sms_url, data=payload, headers=self._get_headers())
        return response

    def _send_sms(self, phone, text):
        response = self._send_sms_request(phone, text)
        if response.status_code == 401:  # If token is expired or invalid
            self.token = self._get_token()  # Refresh token
            response = self._send_sms_request(
                phone, text)  # Retry the request
        return response

    def _send_sms_in_thread(self, phone, text):
        thread = threading.Thread(target=self._send_sms, args=(phone, text))
        thread.start()
        thread.join()
        return True

    def send_accept_order_sms(self, phone, order_number):
        text = f"{order_number}-sonli buyurtmangiz qabul qilindi."
        self._send_sms_in_thread(phone=phone, text=text)

    def send_done_order_sms(self, phone, order_number):
        text = f"MyDMTT\n{order_number}-sonli buyurtmangiz bo'yicha mahsulotlar yetkazildi"
        self._send_sms_in_thread(phone=phone, text=text)
