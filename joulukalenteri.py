import random,json

osallistujat = ['Teemu','Juha','Anna','Markku','Sari','Alex']
jaot = dict((o,[]) for o in osallistujat)

paivia_henkilolle = 24 / len(osallistujat)

for x in xrange(0,24):
	osallistuja = random.choice(osallistujat)
	jaot[osallistuja].append(x+1)

	if len(jaot[osallistuja]) >= paivia_henkilolle:
		osallistujat.remove(osallistuja)

print(json.dumps(jaot, sort_keys=True, indent=2))