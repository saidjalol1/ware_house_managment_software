from django.urls import path
from .views import WorkerView, WorkerMonth, WorkerHour, WorkersHourDetail, WorkersMonthDetail, WorkersWorkDetail

app_name = "worker_app"

urlpatterns = [
    path("", WorkerView.as_view(), name="worker_view"), 
    path("monthly/", WorkerMonth.as_view(), name="worker_month"), 
    path("hourly/", WorkerHour.as_view(), name="worker_hour"), 
    # path("<type:string>/", WorkerView.as_view(), name="worker_view"),
    # path("<type:string>/", WorkerView.as_view(), name="worker_view"),
    path("<int:pk>/", WorkersHourDetail.as_view(), name="worker"),
    path("month/<int:pk>/", WorkersMonthDetail.as_view(), name="worker_detail_month"),
    path("workby/<int:pk>/", WorkersWorkDetail.as_view(), name="worker_by"),
]
