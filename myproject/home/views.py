from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    print(f"I am in Index function")
    return render (request, 'index.html')



def about(request):
    return HttpResponse("This is about page")


def services(request):
    return HttpResponse("This is services page")


def contact(request):
    return HttpResponse("This is a contact page")

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message','')

            response_data = {"response" : f"You said {user_message}",
                            "problem_statement" : "Network Connectivity issues",
                            "root_cause_categorization":["Error","warning","Ignored"],
                            "message":[{"engTitle":"loss of frame","engresolutionSummary":'reset the device'},
                            {"engTitle":"loss of data","engresolutionSummary":'reset the device lost'}],
                            "resolution_summary" :"issue resolved with the reset of the device"}

            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid JSON Format"}, status=400)
    return JsonResponse({"error":"Only POST requests are allowed"}, status = 405)
