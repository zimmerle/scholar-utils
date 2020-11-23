#!env python

from scholarly import scholarly
from scholarly import ProxyGenerator
import fileinput
import sys

pg = ProxyGenerator()
pg.Tor_External(9050, 9051, 'password')
scholarly.use_proxy(pg)

for a in fileinput.input():
    if a == "":
        continue

    try:
        search_query = scholarly.search_pubs(a)
        aa = next(search_query).fill()
        print(a.rstrip(), end='')
        bib = aa.bib
        print("," + str(bib['gsrank']), end='')
        print("," + str(bib['cites']), end='')
        print("")
    except:
        print(" --- Unexpected error (" + a + "): ", sys.exc_info()[0])
        pass

