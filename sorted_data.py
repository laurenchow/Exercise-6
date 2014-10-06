resto_ratings = {}

f = open("scores.txt")
for line in f:
    line = line.rstrip()
    entries = line.split(":")
    resto_ratings.setdefault(entries[0], entries[1])


for key, value in sorted(set(resto_ratings.iteritems())):
    print "Restaurant %r is rated at %r" % (key, value)


#for ordering in sorted(set(resto_ratings)):
#    print ordering, 

