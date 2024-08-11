from django.shortcuts import render 
from datetime import datetime, timedelta, timezone 
def get_ist_time(): 
    IST = timezone(timedelta(hours=5, minutes=30)) 
    utc_time = datetime.now(timezone.utc) 
    ist_time = utc_time.astimezone(IST) 
    return ist_time 
def digital_clock(request): 
    current_time = get_ist_time() 
    formatted_time = current_time.strftime('%I:%M:%S') 
    am_pm = current_time.strftime('%p') 
    timezone = current_time.strftime('%Z') 
    formatted_time_with_ist = f"{formatted_time}<span class='am-pm'>{am_pm}</span><span class='time_zone'> {timezone}</span>" 
    # formatted_time_with_ist =f"{formatted_time}<span class='am-pm'>{am_pm}</span><span class='time_zone'> IST</span>" 
    return render(request, 'clock.html', {'current_time': formatted_time_with_ist})