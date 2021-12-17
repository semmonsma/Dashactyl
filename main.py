import requests
from requests.structures import CaseInsensitiveDict

Var1 = input("What api you want to use? Coins, setresources, createcoupon")
url = "your dashactyl url"
#wait for user input
if Var1 == "coins":
    url2 = url + "/api/coins"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer (put code here)"
    headers["Content-Type"] = "application/json"
    data = '{"id": "331433556867940353", "coins": 1000}'
    resp = requests.post(url2, headers=headers, data=data)
    print(resp.status_code)
elif Var1 == "setresources":
    url2 = url + "/api/setresources"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer (put code here)"
    headers["Content-Type"] = "application/json"
    data = '{"id": "331433556867940353", "resources": 1000}'
    resp = requests.post(url2, headers=headers, data=data)
    print(resp.status_code)
elif Var1 == "createcoupon":
    url2 = url + "/api/createcoupon"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer (put code here)"
    headers["Content-Type"] = "application/json"
    data = '{"id": "331433556867940353", "coupon": "test"}'
    resp = requests.post(url2, headers=headers, data=data)
    print(resp.status_code)
    #print the coupon
    print(resp.json()["coupon"])
else:
    print("You didn't enter a valid api")
print(resp.status_code)
