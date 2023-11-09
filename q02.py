print("----------------------------")
print("        員工薪資輸入        ")
print("    若姓名處未輸入則代表結束")
print("----------------------------")

recordList=[]
totolSalary=0
avgSalary=0

while True:
    name=input("請輸入姓名:")
    if(name==""):
        print("----------------------------")
        break
    salary=int(input("請輸入薪資:"))
    print()
    recordList.append(dict(eName=name,eSalary=salary))

for staff in recordList:
    print(f"員工{staff['eName']:<6}的薪資為 {staff['eSalary']:,}")
    totolSalary+=int(staff['eSalary'])

if(recordList):
    avgSalary=totolSalary/len(recordList)
print("----------------------------")
print(f"合計薪資：{totolSalary:>15,}")
print(f"平均薪資：{avgSalary:>18.2f}")
print("============================")
