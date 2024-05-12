from django.urls import path
from .views import WorkerView, WorkerMonth, WorkerHour, WorkersDetail

app_name = "worker_app"

urlpatterns = [
    path("", WorkerView.as_view(), name="worker_view"), 
    path("monthly/", WorkerMonth.as_view(), name="worker_month"), 
    path("hourly/", WorkerHour.as_view(), name="worker_hour"), 
    # path("<type:string>/", WorkerView.as_view(), name="worker_view"),
    # path("<type:string>/", WorkerView.as_view(), name="worker_view"),
    path("<int:pk>/", WorkersDetail.as_view(), name="worker"),
    path("month/<int:pk>/", WorkersDetail.as_view(), name="worker_detail_month"),
]
