#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random,json

def main():
  osallistujat = ['Teemu','Juha','Anna','Markku','Sari','Alex']
  PAIVIA_PER_HENKILO = 24 / len(osallistujat)

  def jako(osallistujat=[]):
    jaot = dict((o,[]) for o in osallistujat)
    for paiva in xrange(1,24+1):
      osallistuja = random.choice(osallistujat)
      jaot[osallistuja].append(paiva)
      if len(jaot[osallistuja]) >= PAIVIA_PER_HENKILO:
        osallistujat.remove(osallistuja)
    return jaot

  def loyda_nostaja(nostot, paiva):
    henkilo = random.choice(nostot.keys())
    if paiva in jaot.get(henkilo):
      return loyda_nostaja(nostot, paiva)
    else:
      if len(nostot.get(henkilo)) >= PAIVIA_PER_HENKILO:
        return loyda_nostaja(nostot, paiva) 
      return henkilo

  def nostot(jaot):
    osallistujat=jaot.keys()
    nos = dict((o,[]) for o in osallistujat)
    for paiva in xrange(1,24+1):
      nos.get(loyda_nostaja(nos, paiva)).append(paiva)
    return nos

  jaot=jako(osallistujat)
  nosset = nostot(jaot)
  
  print("Kukin henkilö täyttää pussit näiltä päiviltä:")
  print(json.dumps(jaot, sort_keys=True, indent=2))
  print("Kukin henkilö avaa luukun näiltä päiviltä:")
  print(json.dumps(nosset, sort_keys=True, indent=2))

if __name__ == '__main__':
  try:
    main()
  except RuntimeError as re:
    print("Jako epäonnistui.. rekursio pälli päivien jakaminen epäonnistui")
