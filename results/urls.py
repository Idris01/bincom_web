from django.urls import path
from . import views
app_name="results"

urlpatterns=[
    path('',views.index, name="homepage"),
    path('lga_results/', views.lgaView, name="lga"),
]