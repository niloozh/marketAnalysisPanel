from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import viewsets, permissions, status, views, response, decorators, response, pagination
from django.contrib.auth import get_user_model
import stripe

from core.permissions import IsAdminOrReadOnly
from stripe_payment.models import StripeCustomerModel

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCustomerViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        stripe_customer_qs = StripeCustomerModel.objects.filter(user__email=request.user.email)
        current_customer = None
        try:
            if not stripe_customer_qs.count():
                current_customer = stripe.Customer.create(
                    email=request.user.email, name=f"{request.user.first_name} {request.user.last_name}")
                new_stripe_customer_model = StripeCustomerModel()
                new_stripe_customer_model.user = request.user
                new_stripe_customer_model.stripe_customer_id = current_customer.id
                new_stripe_customer_model.save()
            else:
                current_customer = stripe.Customer.retrieve(
                    stripe_customer_qs[0].stripe_customer_id)
            return response.Response(status=status.HTTP_200_OK, data={"payload": current_customer})
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Product id is a required field"})


class RetrieveStripeCustomerViewSet(views.APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request, format=None):
        customer_id = request.data.get("customer_id", "")
        if customer_id:
            try:
                current_customer = stripe.Customer.retrieve(customer_id)
                return response.Response(status=status.HTTP_200_OK, data={"payload": current_customer})
            except Exception as e:
                return response.Response(status=status.HTTP_400_BAD_REQUEST, data={"message": str(e)})
        return response.Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Customer id is a required field"})
