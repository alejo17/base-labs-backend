import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db.models import Sum

from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from baselabs.models import Sales, Purchases


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "username": user.username
            })

        return JsonResponse({"error": "Invalid credentials"}, status=401)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    return JsonResponse({
        "authenticated": True,
        "username": request.user.username
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_top_ten(request):
    sales = list(
        Sales.objects
        .values("brand", "description")
        .annotate(
            quantity=Sum("salesquantity"),
            price=Sum("salesdollars")
        )
    )

    purchases = list(
        Purchases.objects
        .values("brand")
        .annotate(
            quantity=Sum("quantity"),
            price=Sum("dollars")
        )
    )

    purchases_dict = {c["brand"]: c for c in purchases}

    result = []

    for venta in sales:
        compra = purchases_dict.get(venta["brand"])

        if compra:
            profit = round(venta["price"] - compra["price"], 2)
            margin = round((profit / venta["price"]) * 100, 2)

            result.append({
                "brand": venta["description"],
                "profit": profit,
                "margin": margin
            })


    result.sort(key=lambda x: x["margin"], reverse=True)

    return Response(result[:10], status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_negative_margin(request):
    sales = list(
        Sales.objects
        .values("brand", "description")
        .annotate(
            quantity=Sum("salesquantity"),
            price=Sum("salesdollars")
        )
    )

    purchases = list(
        Purchases.objects
        .values("brand")
        .annotate(
            quantity=Sum("quantity"),
            price=Sum("dollars")
        )
    )

    purchases_dict = {c["brand"]: c for c in purchases}

    result = []

    for venta in sales:
        compra = purchases_dict.get(venta["brand"])

        if compra:
            profit = round(venta["price"] - compra["price"], 2)
            margin = round((profit / venta["price"]) * 100, 2)

            result.append({
                "brand": venta["description"],
                "profit": profit,
                "margin": margin
            })


    negatives = [r for r in result if r["margin"] < 0]
    negatives.sort(key=lambda x: x["margin"], reverse=False)

    return Response(negatives[:30], status=status.HTTP_200_OK)