from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime, timedelta

def index(request):

    return render(request, "index.html")
def home(request):

    return render(request, "info.html")

def time(request):
    #getting current time
    date = datetime.today()

    day_s = int(request.POST['day'])
    month_s = int(request.POST['month'])
    year_s = int(request.POST['year'])

    #getting current date
    now = datetime.now()
    #collecting user data
    then = datetime(year_s, month_s, day_s)
    #calculting days spend 
    delta = now - then
    #calcultaing leap year
    year_l = (date.year - year_s) / 4
    #calcultating months
    months = int(delta.days / 30.8)
    #accurate days
    days = delta.days
    #calculating year spend
    cal_year = int(date.year - year_s)
    #total hours
    hours = int(days * 24)
    #total seconds
    minutes = hours * 60
    seconds = (hours * 60) * 60
    #total weeks
    weeks = int(days / 7)

    context = {
        "date" : date,
        'sec': seconds,
        'hour': hours,
        'minute': minutes, 
        'day': days, 
        'week': weeks,
        'month': months,
        'years': cal_year
    }

    return render(request, "time.html", context)
