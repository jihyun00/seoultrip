import json

with open('data/seoulhotel.json', 'r') as f:
    file = f.read()
f.close()

result = json.loads(file)

cnt = len(result["DATA"]) 
rows = result["DATA"]

for row in rows:
    name = row["HOTEL_NM"]
    addr = row["ADDR_URL"]
    grade = row["GRADE"]
    faculty = row["ADD_FACTY"]
    room = row["NOF_RM"]

    # region_id, category_id, lang_id, CGM_NM으로 뭔가 할 수 있을 듯?
    print(name)
    print(addr)
    print(grade)
    print(faculty)
    print(room)
