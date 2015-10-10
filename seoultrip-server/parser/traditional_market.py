import json
import requests

start = 1
end = 1

token = '52474170756e6f62383467634f6f58'
r = requests.get('http://openapi.seoul.go.kr:8088/'+token+'/json/ListTraditionalMarket/'+str(start)+'/'+str(end))
result = r.json()

status = result["ListTraditionalMarket"]["RESULT"]["CODE"]
cnt = result["ListTraditionalMarket"]["list_total_count"]

if(status == "INFO-000"):
    pivot = int(cnt/1000)+2
    for i in range(1, pivot):
        if(i == pivot): # 범위 넘어가는 경우
            end = pivot
        else:
            end = i*1000
        start = end-999
        r = requests.get('http://openapi.seoul.go.kr:8088/'+token+'/json/ListTraditionalMarket/'+str(start)+'/'+str(end))
        result = r.json()
        print(result)
        rows = result["ListTraditionalMarket"]["row"]

        for row in rows:
            name = row["M_NAME"]
            addr = row["M_ADDR"]
            phone = row["M_TEL"]
            lat = row["LAT"]
            lng = row["LNG"]
            
            # TODO: region_id, category_id, lang_id

            print(name)
            print(addr)
            print(phone)
            print(lat)
            print(lng)

else:
    print(status)
