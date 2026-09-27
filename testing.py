import json

with open("company-data-apr26.json",'r', encoding="utf-8") as file:
	companyData = json.load(file)

with open("prod-data-apr26.json",'r', encoding="utf-8") as file:
	prodData = json.load(file)



print(f"C: {prodData["C"]}")
print("===========")
print(f"HCP: {prodData["HCP"]}")
print(f"MAI: {prodData["MAI"]}")
print(f"GRN: {prodData["GRN"]}")
print("===========")
print(f"MTP: {prodData["MTP"]}")
print(f"RSI: {prodData["RSI"]}")
print(f"BAC: {prodData["BAC"]}")
print(f"AIR: {prodData["AIR"]}")
print("============")
print(f"FOD: {prodData["FOD"]}")
print(f"RAT: {prodData["RAT"]}")
print("============")
print(f"GIN: {prodData["GIN"]}")
print(f"ALE: {prodData["ALE"]}")












# print(f"GRN: {prodData["GRN"]}")
# print(f"RAT: {prodData["RAT"]}")
# print(f"C: {prodData["C"]}")
# print(f"GIN: {prodData["GIN"]}")
# print(f"ALE: {prodData["ALE"]}")


# print(f"AL: {prodData["AL"]}")
# print(f"ALO: {prodData["ALO"]}")
# print(f"BE: {prodData["BE"]}")

# print(f"FE: {prodData["FE"]}")
# print(f"FEO: {prodData["FEO"]}")
# print(f"TA: {prodData["TA"]}")

# print(f"RE: {prodData["RE"]}")
# print(f"REO: {prodData["REO"]}")
