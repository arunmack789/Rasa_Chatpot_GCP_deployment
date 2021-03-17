
import requests
import json
import random
def Calorie(food):
    url = "https://food-calorie-data-search.p.rapidapi.com/api/search"

    querystring = {"keyword":food}

    headers = {
    'x-rapidapi-key': "c9ecceb08dmsh4a5a0e04940bf9dp1224bdjsn479fb7205f2b",
    'x-rapidapi-host': "food-calorie-data-search.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = response.json()
    print(json.dumps(json_data,indent=4))
    cal=[]
    for i in json_data:
        print(i.keys())
        cal.append(i.get('energ_kcal'))
        maxi = str(max(cal))
        #print(type(maxi))
        mini = str(min(cal))
        #print(cal)
    print("you chossen food minimum calorie is {0} and Maximum Calorie is {1}".format(mini,maxi))
    return maxi, mini

    
print(Calorie('Guava')[0])