import json
import requests

start = 1
end = 1

token = '52474170756e6f62383467634f6f58'
r = requests.get('http://openapi.seoul.go.kr:8088/'+token+'/json/ListCulturalAssetsInfo/'+str(start)+'/'+str(end)+'/')
result = r.json()

status = result["ListCulturalAssetsInfo"]["RESULT"]["CODE"]
cnt = result["ListCulturalAssetsInfo"]["list_total_count"]

if(status == "INFO-000"):
    pivot = int(cnt/1000)+2
    for i in range(1, pivot):
        if(i == pivot): # 범위 넘어가는 경우
            end = pivot
        else:
            end = i*1000
        start = end-999
        r = requests.get('http://openapi.seoul.go.kr:8088/'+token+'/json/ListCulturalAssetsInfo/'+str(start)+'/'+str(end)+'/')
        result = r.json()
        print(result)
        rows = result["ListCulturalAssetsInfo"]["row"]

        for row in rows:
            name = row["NAME_KOR"]
            addr = row["STAND_ADDR"]
            board = row["BOARD_KOR"]

            print(name)
            print(addr)
            print(board)

            # region_id, category_id, lang_id
else:
    print(status)
