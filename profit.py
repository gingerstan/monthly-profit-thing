# PrUn Daily Profit from Extractables Calculator

# company-data-apr26.json:
# Section 1: Totals -> for each company lists their total volume, profit, and respective ranks
# Section 2: Individuals -> breakdown of which items each company produced, along with the volume,
#							profit, quantity produced, and overall rank




import json

with open("company-data-apr26.json",'r', encoding="utf-8") as file:
	companyData = json.load(file)

with open("prod-data-apr26.json",'r', encoding="utf-8") as file:
	prodData = json.load(file)


#################################################
# Unit Extraction Cost Stuff

raws = ["ALO","AMM","AR","AUO","BER","BOR","BRM","BTS","CLI","CUO","F","FEO","GAL","H",
		"H2O","HAL","HE","HE3","HEX","KR","LES","LIO","LST","MAG","MGS","N","NE","O",
		"REO","SCR","SIO","TAI","TCO","TIO","TS","ZIR"]

pbu = ["DW","RAT" ,"OVE","COF","PWO"]

# key = matID, value = list of unit extraction costs from each player
plrExtCosts = {} 
for mat in raws:
	plrExtCosts[mat] = []

# key = matID, value = lists the price of pbu mats for each player
pbuMatCosts = {}
for mat in pbu:
	pbuMatCosts[mat] = []


indiv = companyData["individual"]


print("Unit Extraction Cost")
# fills the plrExtCosts dict with the cost to
# extract the corresponding raw material
# for each player
for playerID in indiv:
	for mat, value in indiv[playerID].items():
		if mat not in raws:
			continue

		volume = value["volume"]
		profit = value["profit"]
		amount = value["amount"]

		unitCost = (volume - profit) / amount

		plrExtCosts[mat].append(unitCost)

# for each raw material, determines the
# average price to extract one unit
unitExtCosts = {}
for mat, ranks in plrExtCosts.items():

	sum = 0
	for x in ranks:
		sum += x

	average = sum / len(ranks)

	unitExtCosts[mat] = average

for mat, cost in unitExtCosts.items():
	print(f"{mat} : {cost}")


print("=========================================\nAverage PIO Consumable Prices")

# fills the pbuMatCosts dict with the ask 
# price of the corresponding PBU material
# for each player
for playerID in indiv:
	for mat, value in indiv[playerID].items():
		if mat not in pbu:
			continue

		volume = value["volume"]
		amount = value["amount"]

		unitCost = volume / amount

		pbuMatCosts[mat].append(unitCost)

# for each PBU material, determines the
# average ask price of one unit
pbuUnitCosts = {}
for mat, ranks in pbuMatCosts.items():

	sum = 0
	for x in ranks:
		sum += x

	average = sum / len(ranks)

	pbuUnitCosts[mat] = average


for mat, cost in pbuUnitCosts.items():
	print(f"{mat} : {cost}")


print("=========================================\nPBU Consumable Prices")

pbuCosts = {}
amounts = [40,40,5,5,2]

yes = 0
for mat, cost in pbuUnitCosts.items():
	pbuCosts[mat] = cost * amounts[yes]
	yes += 1

totalCost = 0
for mat, cost in pbuCosts.items():
	print(f"{mat}: {cost}")
	totalCost += cost
print(f"PBU Cost: {totalCost}")

print("=========================================\nPBU Consumable Price Ratios")

costRatios = {}
for mat, cost in pbuCosts.items():
	costRatios[mat] = cost / totalCost

total = 0
for mat, ratio in costRatios.items():
	print(f"{mat}: {ratio}")
	total += ratio
print(f"total ratio: {total}")

print("=========================================\nRaw Mat Unit Consumable Cost")

rawMatsConsumablePrices = {}

for mat in raws:
	matUnitPrice = unitExtCosts[mat]

	idkyet = {}
	for cons in pbu:
		idkyet[cons] = round(matUnitPrice * costRatios[cons], 2)

	rawMatsConsumablePrices[mat] = idkyet


for mat, prices in rawMatsConsumablePrices.items():
	print(f"{mat}: ")
	for cons, priceRatio in prices.items():
		print(f"{cons} cost = {priceRatio},",end=" ")
	print("")


with open("rawMatsConsumablePrices.json", "w") as file:
    json.dump(rawMatsConsumablePrices, file, indent=4)


print("=========================================\nMultiple Input Ratios")

############################################################
# Multiple-Recipe Stuff

# matches itemID to the preferred recipes usage ratio
multiRecipeRatios = {}

multiRecipeRatios["AHP"] = {"preferred" : 0.75, "alternate" : 0.25}
multiRecipeRatios["AL"] = {"preferred" : 0.558, "alternate" : 0.442}
multiRecipeRatios["BBH"] = {"preferred" : 0.6, "alternate" : 0.4}
multiRecipeRatios["BDE"] = {"preferred" : 0.7, "alternate" : 0.3}
multiRecipeRatios["BEA"] = {"preferred" : 0.9, "alternate" : 0.1}
multiRecipeRatios["BHP"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["BLE"] = {"preferred" : 0.9, "alternate" : 0.1}
multiRecipeRatios["BSE"] = {"preferred" : 0.6, "alternate" : 0.4}
multiRecipeRatios["BTA"] = {"preferred" : 0.7, "alternate" : 0.3}
multiRecipeRatios["C"] = {"preferred" : 0.7, "alternate" : 0.3} #
multiRecipeRatios["DRF"] = {"preferred" : 0.95, "alternate" : 0.05} 
multiRecipeRatios["DW"] = {"preferred" : 0.3, "alternate" : 0.7}
multiRecipeRatios["EXO"] = {"preferred" : 0.4, "alternate" : 0.6} #
multiRecipeRatios["FE"] = {"preferred" : 0.672, "alternate" : 0.328}
multiRecipeRatios["GL"] = {"preferred" : 0.45, "alternate" : 0.55} #
multiRecipeRatios["GRA"] = {"preferred" : 0.9, "alternate" : 0.1}
multiRecipeRatios["GRN"] = {"preferred" : 0.9, "alternate" : 0.1}
multiRecipeRatios["HCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["HHP"] = {"preferred" : 0.7, "alternate" : 0.3}
multiRecipeRatios["HOP"] = {"preferred" : 0.85, "alternate" : 0.15}
multiRecipeRatios["LCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["MAI"] = {"preferred" : 0.8, "alternate" : 0.2}
multiRecipeRatios["LCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["MCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["MUS"] = {"preferred" : 0.8, "alternate" : 0.2}
multiRecipeRatios["MCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["OVE"] = {"preferred" : 0.8, "alternate" : 0.2}
multiRecipeRatios["PIB"] = {"preferred" : 0.8, "alternate" : 0.2}
multiRecipeRatios["PPA"] = {"preferred" : 0.6, "alternate" : 0.4} #
multiRecipeRatios["PT"] = {"preferred" : 0.6, "alternate" : 0.4} #
multiRecipeRatios["RAT"] = {"preferred" : 0.2, "alternate" : 0.8} #
multiRecipeRatios["RCO"] = {"preferred" : 0.7, "alternate" : 0.3}
multiRecipeRatios["RE"] = {"preferred" : 0.88, "alternate" : 0.12}
multiRecipeRatios["RG"] = {"preferred" : 0.65, "alternate" : 0.35}
multiRecipeRatios["RHP"] = {"preferred" : 0.95, "alternate" : 0.05}
multiRecipeRatios["SCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["SF"] = {"preferred" : 0.8, "alternate" : 0.2}
multiRecipeRatios["SI"] = {"preferred" : 0.6, "alternate" : 0.4} # 
multiRecipeRatios["SIO"] = {"preferred" : 0, "alternate" : 1} # extractable
multiRecipeRatios["TA"] = {"preferred" : 0.5, "alternate" : 0.5}
multiRecipeRatios["TCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["TI"] = {"preferred" : 0.5, "alternate" : 0.5}
multiRecipeRatios["VCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["VEG"] = {"preferred" : 0.7, "alternate" : 0.3}
multiRecipeRatios["VSC"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["WCB"] = {"preferred" : 1, "alternate" : 0}
multiRecipeRatios["ZR"] = {"preferred" : 0.5, "alternate" : 0.2}

multiRecipeRatiosV2 = {}
for key, ratios in multiRecipeRatios.items():
	multiRecipeRatiosV2[key] = [ratios["preferred"], ratios["alternate"]]


with open("multiRecipeRatios.json", "w") as file:
    json.dump(multiRecipeRatios, file, indent=4)

with open("multiRecipeRatiosV2.json", "w") as file:
    json.dump(multiRecipeRatiosV2, file, indent=4)