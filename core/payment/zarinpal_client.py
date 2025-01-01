import requests
import json
from django.conf import settings
from django.shortcuts import redirect
from .models import PaymentModel
from order.models import OrderModel

def get_domain():
    # for fixing issue with the sites model before migration
    try:
        from django.contrib.sites.models import Site
        return Site.objects.get_current().domain
    except:
        return "example.com"


def get_protocol():
    # Determine the protocol based on the SECURE_SSL_REDIRECT setting
    return 'https' if getattr(settings, 'SECURE_SSL_REDIRECT', False) else 'http'



class ZarinPalSandbox:
    ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
    ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
    ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"
    _payment_page_url = "https://sandbox.zarinpal.com/pg/StartPay/"

    def __init__(self, merchant, call_back_url):
        self.MERCHANT = merchant
        self.callbackURL = call_back_url

    def payment_request(self, description="پرداختی کاربر"):
        req_data = {
            "merchant_id": "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897",
            "amount": float(10000),
            "callback_url": self.callbackURL,
            "description": description,
        }
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        response = requests.post(url=self.ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)

        
        authority = response.json()['data']['authority']
        return authority

        

    def payment_verify(self, amount, authority):
        payload = {
            "MerchantID": self.merchant_id,
            "Amount": amount,
            "Authority": authority
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_verify_url, headers=headers, data=json.dumps(payload))
        return response.json()
    
    def generate_payment_url(self, authority):
        return f"{self._payment_page_url}{authority}"