from django.urls import path
from .views import WareHouseView

app_name = "warehouses_app"

urlpatterns = [
    path("", WareHouseView.as_view(), name="warehouse")
]