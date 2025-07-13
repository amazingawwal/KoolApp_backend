from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

# def activity(req):
#     list_items = ''
#     months = list(monthlyActivities.keys())
    
#     for month in months:
#         url = f'/home/{month}'
#         # url = reverse('monthly-activity', args=[month])
#         list_items += f"<li><a href={url}>{month}<a/></li>"
#         response_data = f"<ul>{list_items}</ul>"
#         # response_data = month

#     return HttpResponse(response_data)

def activity(req):
    months = list(monthlyActivities.keys())
    response_data = render_to_string('activities/home.html', {'months' : months})
    return HttpResponse(response_data)


def activities(req, month):
    try:
        monthlyActivity = monthlyActivities[month]
        response = f'<h2>{monthlyActivity}</h2>'
        return HttpResponse(response)
    except:
        return HttpResponseBadRequest('Invalid Entry')



def activities2(req, month):
    monthKey = list(monthlyActivities.keys())
    if month > len(monthKey):
        return HttpResponseBadRequest('Invalid Input')
    monthIndex = month - 1

    # redirect = f'/home/{monthKey[monthIndex]}'
    redirect = reverse('monthly-activity', args=[monthKey[monthIndex]])
    return HttpResponseRedirect( redirect )



def render_html(req, month):
    context = {
    'text': monthlyActivities[month],
    'month': month
    }
    try:
        # activity_text = monthlyActivities[month]
        return render(req, 'activities/activity.html', context)
        # response = render_to_string('activities/activity.html', context)
        # return HttpResponse(response)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('Bad entry')