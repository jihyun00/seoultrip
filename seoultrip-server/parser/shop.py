import json
import requests

start = 1
end = 1

token = '52474170756e6f62383467634f6f58'
r = requests.get('http://openapi.songpa.seoul.kr:8088/'+token+'/json/SpListMall/'+str(start)+'/'+str(end))

result = r.json()

status = result["SpListMall"]["RESULT"]["CODE"]
cnt = result["SpListMall"]["list_total_count"]

if(status == "INFO-000"):
    pivot = int(cnt/1000)+2
    for i in range(1, pivot):
        if(i == pivot):
            end = pivot
        else:
            end = i*1000
        start = end-999
        r = requests.get('http://openapi.songpa.seoul.kr:8088/'+token+'/json/SpListMall/'+str(start)+'/'+str(end))
        result = r.json()
        rows = result["SpListMall"]["row"]

        for row in rows:
            name = row["TRNM_NM"]
            phone = row["TRDP_TELNO"]
            state_code = row["MNG_STATE_CODE"]
            kind = row["UPTAE_CODE"]

            if(state_code == "폐업"):
                continue

            # region_id, category_id, lang_id
            print(name)
            print(phone)
            print(state_code)
            print(kind)
else:
    print(status)
