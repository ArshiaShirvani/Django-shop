from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import PaymentModel, PaymentStatusType
from django.urls import reverse_lazy
from .zarinpal_client import ZarinPalSandbox
from order.models import OrderModel, OrderStatusType


class PaymentVerifyView(View):
    def get(self, request, *args, **kwargs):
        authority_id = request.GET.get("Authority")
        if not authority_id:
            return redirect(reverse_lazy("order:order-failed"))

        # finding the related payment and order models
        payment_obj = get_object_or_404(PaymentModel, authority_id=authority_id)

        try:
            order = OrderModel.objects.get(payment=payment_obj)
        except OrderModel.DoesNotExist:
            return redirect(reverse_lazy("order:order-failed"))

        # create client of the zarinpal
        zarin_pal = ZarinPalSandbox(
            merchant="4ced0a1e-4ad8-4309-9668-3ea3ae8e8897",
            amount=int(payment_obj.amount),
        )

        # checking the response of the payment request verify
        response = zarin_pal.payment_verify(
            int(payment_obj.amount), payment_obj.authority_id
        )

        # checking for the presence of required keys in the response
        ref_id = response.get("ref_id")
        status_code = response.get("code")

        if ref_id and status_code is not None:
            # update the status of the payment
            payment_obj.ref_id = ref_id
            payment_obj.response_code = status_code
            payment_obj.status = (
                PaymentStatusType.success.value
                if status_code in {100, 101}
                else PaymentStatusType.failed.value
            )
            payment_obj.response_json = response
            payment_obj.save()

            # update the status of the order
            order.status = (
                OrderStatusType.success.value
                if status_code in {100, 101}
                else OrderStatusType.failed.value
            )
            order.save()

            # redirecting to an appropriate page
            if status_code in {100, 101}:
                return redirect(reverse_lazy("order:order-completed"))
            else:
                return redirect(reverse_lazy("order:order-failed"))

        # if ref_id is none or status is failed
        else:
            order.status = OrderStatusType.failed.value
            payment_obj.status = PaymentStatusType.failed.value
            payment_obj.response_json = response
            payment_obj.save()  # saving the status of the order and payment
            order.save()
            return redirect(reverse_lazy("order:order-failed"))
