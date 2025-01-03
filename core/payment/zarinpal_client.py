import requests
import json
from django.conf import settings
from django.shortcuts import redirect
from .models import PaymentModel
from order.models import OrderModel
from django.http import HttpResponse

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
    # ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"
    _payment_page_url = "https://sandbox.zarinpal.com/pg/StartPay/"
    _callbackURL = "http://127.0.0.1:8000/payment/verify/"

    def __init__(self, merchant,amount):
        self.MERCHANT = merchant
        self.amount = amount

    def payment_request(self,description="پرداختی کاربر"):
        req_data = {
            "merchant_id": "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897",
            "amount": float(self.amount),
            "callback_url": self._callbackURL,
            "description": description,
        }
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        response = requests.post(url=self.ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)

        
        authority = response.json()['data']['authority']
        return authority

        

    def payment_verify(self, amount,authority):
        req_data = {
            "merchant_id": "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897",
            "amount": amount,
            "authority": authority
        }
        
        req_header = {
        'Content-Type': 'application/json'  
        }
        
        req = requests.post(url=self.ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if req is not None:
        
            return req.json()['data']
        else:
            return HttpResponse(f'تراکنش ناموفق بوده است یا توسط کاربر لغو شده است')
            
    
    def generate_payment_url(self, authority):
        return f"{self._payment_page_url}{authority}"