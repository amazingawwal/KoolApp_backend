from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

monthlyActivities = {
    "January": "Set yearly goals",
    "February": "Plan a short trip",
    "March": "Spring cleaning",
    "April": "Visit a museum",
    "May": "Go camping",
    "June": "Go to the beach",
    "July": "Host a barbecue",
    "August": "Take a vacation",
    "September": "Visit a farmers' market",
    "October": "Carve pumpkins",
    "November": "Host a Friends-giving",
    "December": "Decorate for holidays"
}

# Create your views here.

def activities(req, month):
    try:
        monthlyActivity = monthlyActivities[month]
        return HttpResponse(monthlyActivity)
    except:
        return HttpResponseBadRequest('Invalid Entry')

def activities2(req, month):
    monthKey = list(monthlyActivities.keys())
    if month > len(monthKey):
        return HttpResponseBadRequest('Invalid Input')
    monthIndex = month - 1
    return HttpResponseRedirect( monthKey[monthIndex])
    # return HttpResponse(monthKey[monthIndex])   