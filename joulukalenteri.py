import random,json

def jako(osallistujat=[]):
  jaot = dict((o,[]) for o in osallistujat)

  paivia_henkilolle = 24 / len(osallistujat)

  for x in xrange(0,24):
    osallistuja = random.choice(osallistujat)
    jaot[osallistuja].append(x+1)

    if len(jaot[osallistuja]) >= paivia_henkilolle:
      osallistujat.remove(osallistuja)

  return jaot


if __name__ == '__main__':
  jaot=jako(['Teemu','Juha','Anna','Markku','Sari','Alex'])
  print(json.dumps(jaot, sort_keys=True, indent=2))