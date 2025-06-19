from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models.airport_models import Airports
from .forms.forms import AirportForm
from .utilities import find_distance_header




def landing_view(request):
    return render(request, 'dashboard.html')



# --- Login View ---
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            if user.role == 'superadmin':
                return redirect('superadmin_dashboard')
            elif user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return render(request, 'login.html', {'error': 'Access Denied'})  # fallback
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def search_port(request):
    if request.method == 'POST':
        airport_code = request.POST.get('airport_code')
        position = request.POST.get('position')
        
        
        ports = Airports.objects.filter(is_active=True)

        if not ports:
            return render(request, 'airport.html')  # custom 404 page
        

        def find_child(ports,airport_code,position):
            for port in ports:
                if port.parent_port == airport_code and port.position == position:
                    print("portt",port)
                    return [{"airport_code":port.airport_code,
                              "position":port.position,
                              "duration":port.duration,
                              "parent_port":port.parent_port}]
            return []



        results = []
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
                
                
                results.clear()
                results.append(datas)
                print("resultsresultsresults[0]",results[0])
        else:
            return render(request,'airport.html' , {
                                                'airports': []
                                            })

    return render(request,'search.html')




    
    



def shortest_distance(request):
    if request.method == 'POST':
        left_distance, right_distance = find_distance_header(request)

        result = left_distance if left_distance[0]['node_distance'] < right_distance[0]['node_distance'] else right_distance
        print("====================================")
        print(result)
        print("====================================")

        

        return render(request,'airport.html' , {
                                            'airports': result
                                        })
       

    return render(request,'shortest.html')
        

def longest_distance(request):
    # if request.method == 'POST':
    #     airport_code = request.POST.get('airport_code')

    #     ports = Airports.objects.filter(is_active=True)

    #     if not ports:
    #         return render(request, 'airport.html')  # custom 404 page
        
    #     left_distance = find_lenght(request,ports,airport_code,'left')
    #     right_distance = find_lenght(request,ports,airport_code,'right')

        
    #     result = left_distance if left_distance[0]['node_distance'] > right_distance[0]['node_distance'] else right_distance
        
    #     return render(request,'airport.html' , {
    #                                         'airports': result
    #                                     })
       

    # return render(request,'shortest.html')
    if request.method == 'POST':
        left_distance, right_distance = find_distance_header(request)

        result = left_distance if left_distance[0]['node_distance'] > right_distance[0]['node_distance'] else right_distance
        print("====================================")
        print(result)
        print("====================================")

        

        return render(request,'airport.html' , {
                                            'airports': result
                                        })
       

    return render(request,'longest.html')
           
 

@require_http_methods(["GET", "POST"])
def manage_airport(request):
    # if request.user.role not in ['superadmin','admin']:
    #     return redirect('login')

    # Handle POST request (Create task)
    if request.method == 'POST':
        # form  = AirportForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('manage_airport')
        # else:
        #     form = AirportForm()

        
        airport_code = request.POST.get('airport_code')
        position = request.POST.get('position')
        duration = request.POST.get('duration')
        # master_airport = request.POST.get('master_airport')
        parent_port = request.POST.get('parent_port')


    
       
        Airports.objects.create(
            airport_code = airport_code,
            position = position,
            duration = duration,
            master_airport = 'A',
            parent_port = parent_port,
            is_active=True
        )
       
    
        return redirect('manage_airport')  # Ensure this is the name in your urls.py

    airports = Airports.objects.filter(is_active=True)
   
    
    return render(request,'airport.html' , {
        'airports': airports
    })
    




