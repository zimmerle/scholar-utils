#!env python


from scholarly import scholarly
import fileinput
import sys


for a in fileinput.input():
    if a == "":
        continue

    try:
        search_query = scholarly.search_author(a)
        aa = next(search_query).fill()
        print(a.rstrip(), end='')
        print("," + str(aa.hindex), end='')
        print("," + str(aa.i10index), end='')
        print("," + '; '.join(aa.interests))
    except:
        print(" --- Unexpected error (" + a + "): ", sys.exc_info()[0])
        pass

