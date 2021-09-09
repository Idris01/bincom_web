from django.shortcuts import render
from .utility import get_serialized_PuResult,get_serialized_Pu

# Create your views here.
def index(request):
    context={
        "data":get_serialized_PuResult()
    }
    return render(request,"results/index.html", context)

def lgaView(request):
    context={
        "lga_data":get_serialized_Pu()
    }
    return render(request,"results/lga.html", context)