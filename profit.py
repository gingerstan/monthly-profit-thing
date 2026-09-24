# PrUn Daily Profit from Extractables Calculator

# company-data-apr26.json:
# Section 1: Totals -> for each company lists their total volume, profit, and respective ranks
# Section 2: Individuals -> breakdown of which items each company produced, along with the volume,
#							profit, quantity produced, and overall rank


# TODO:
# Need to link companyIDs here to players
# account for inflation?
#



import json

with open("company-data-apr26.json",'r', encoding="utf-8") as file:
	companyData = json.load(file)

with open("prod-data-apr26.json",'r', encoding="utf-8") as file:
	prodData = json.load(file)


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