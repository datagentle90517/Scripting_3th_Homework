import json

def triangle_zhonxin(a:int, b:int, c:int):
    '''
    計算三角形重心
    '''
    x=round((int(a[0])+int(b[0])+int(c[0]))/3)
    y=round((int(a[1])+int(b[1])+int(c[1]))/3)
    return (x,y)

def read_json(file_name: str):
    '''
    將 json 檔案轉為字典後回傳
    '''
    with open(file_name, 'r', encoding='UTF-8') as f:
        # json.load() 讀取 JSON 檔案，轉換為 Python 的 dict
        pyJson = json.load(f)
    return pyJson

def print_json(data: dict):
    '''
    將字典轉爲 json 字串後輸出到螢幕
    '''
    result=json.dumps(data,ensure_ascii=False,indent=4)
    print(result)

def write_json(data: dict, file_name: str):
    '''
    將字典轉為檔案
    '''
    with open(file_name, 'w', encoding="utf-8") as f:
        # json.dump() 將 dict 轉成 JSON 格式，寫入 JSON 檔案
        json.dump(data, f, ensure_ascii=False, indent=4)

def process_data(data: dict, discount: float):
    '''
    將字典中每個菜品的價格打discount 折數
    '''
    for food in data["categories"][0]["items"]:
        food["price"]=round(food["price"]*discount)
    for food in data["categories"][1]["items"]:
        food["price"]=round(food["price"]*discount)