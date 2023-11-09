from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE ='Scripting_3th_Homework/menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'Scripting_3th_Homework/output.json'   # 輸出檔案名稱

food={
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
}

data=read_json(MENU_FILE)
print_json(data)

data["categories"][1]["items"].append(food)

discountVal=float(input("請輸入折扣率(0.0 ~ 1.0):"))
process_data(data,discountVal)

write_json(data,OUTPUT_FILE)
print_json(data)





