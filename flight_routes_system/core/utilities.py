

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages

from .models.airport_models import Airports
from .forms.forms import AirportForm



def search_port(request):
    if request.method == 'POST':
        airport_code = request.POST.get('airport_code')
        position = request.POST.get('position')
        
        ports = Airports.objects.filter(is_active=True)

        if not ports:
            return render(request, 'airport.html')  # custom 404 page
        
        
        def find_child(ports,airport_code,position):
            # print("port.parent_port",ports.parent_port)
            # print("port.position",port.position)
            
            for port in ports:
                if port.parent_port == airport_code and port.position == position:
                    print("portt",port)
                    return [{"airport_code":port.airport_code, "position":port.position,"duration":port.duration,"parent_port":port.parent_port}]
                

            return []



        results = []
        first_try = 1
        searching = True
        
        data = find_child(ports,airport_code,position)
        
        
        if data :
            
            results.append(data)
            print("resultsresultsresults[1sss]",results[0])
            while searching:
                print("data ++",results[0])
                # print("datadatadatadatadatadata",data.airport_code)
                # print("datadatadatadatadatadata",data.position)
                datas = find_child(ports,results[0][0]['airport_code'],results[0][0]['position'])
                print("hererere ",datas)
                if not datas:
                    # print("datadatadatadatadatadata==========",results)
                    # print("datadatadatadatadatadata========",results )
                    return render(request,'airport.html' , {
                                                'airports': results[0]
                                            })
                
                # print("thissss",)
                results.clear()
                results.append(datas)
                print("resultsresultsresults[0]",results[0])
        else:
            return render(request,'airport.html' , {
                                                'airports': []
                                            })

     
    
    return render(request,'search.html')