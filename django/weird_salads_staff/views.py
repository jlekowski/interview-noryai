from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Staff


def list_staff(request: HttpRequest) -> HttpResponse:
    staff = Staff.objects.order_by("name")
    return render(request, "weird_salads_staff/list_staff.html", {"all_staff": staff})
