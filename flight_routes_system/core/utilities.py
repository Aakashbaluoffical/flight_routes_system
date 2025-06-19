from .models.airport_models import Airports
from django.shortcuts import render, redirect


def find_child(ports,airport_code,position):
            for port in ports:
                if port.parent_port == airport_code and port.position == position:
                    print("portt",port)
                    return {"airport_code":port.airport_code,
                              "position":port.position,
                              "duration":port.duration,
                              "parent_port":port.parent_port}
            return {}


def find_lenght(request,ports,airport_code,position):
    results = []
    searching = True    
    data = find_child(ports,airport_code,position)

    if data :
        node_distance = data['duration']
        data['node_distance'] = data['duration'] 
        results.append(data)
        print("resultsresultsresults[1sss]",results)
       

        while searching:
            print("data ++",results)
            # print("datadatadatadatadatadata",data.airport_code)
            # print("datadatadatadatadatadata",data.position)
            datas = find_child(ports,results[0]['airport_code'],results[0]['position'])
            print("hererere ",datas)
            try:
                node_distance += datas['duration']
            except:
                node_distance
            
            if not datas:
                # print("datadatadatadatadatadata==========",results)
                # print("datadatadatadatadatadata========",results )
                return results
            
            
            results.clear()
            datas['node_distance'] = node_distance
            results.append(datas)
            print("resultsresultsresults[0]",results)
    else:
        return []
    

def find_distance_header(request):
        airport_code = request.POST.get('airport_code')

        ports = Airports.objects.filter(is_active=True)

        if not ports:
            return render(request, 'airport.html')  # custom 404 page
        
        left_distance = find_lenght(request,ports,airport_code,'left')
        right_distance = find_lenght(request,ports,airport_code,'right')

        return left_distance, right_distance