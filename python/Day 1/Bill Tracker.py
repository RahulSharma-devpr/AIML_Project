rent=float(input("Enter rent of House / Flat:"))
foods=float(input("Enter Cost of foods:"))
electricity=float(input("Enter Electricity Bill:"))
maintenance=float(input("Enter Maintenance Cost:"))

total_bill= rent+foods+electricity+maintenance

print("Bill Summary")

print(rent)
print(foods)
print(electricity)
print(maintenance)
print(total_bill)

Member=int(input(" Members in Sharing\n"))
total_bill_per_Member= (rent+foods+electricity+maintenance)
print("BILL per Member",total_bill_per_Member/Member)

