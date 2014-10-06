resto_ratings = {}

f = open("scores.txt")
for line in f:
    line = line.rstrip()
    entries = line.split(":")
    restaurant = entries[0]
    ratings = int(entries[1])

    #resto_ratings.setdefault(entries[0], entries[1])
    resto_ratings[restaurant] = ratings + resto_ratings.get(restaurant, 0)
    #.get assigns a value when the key doesn't exist, you can set the default to 0 if 
    #you need to use a value
    

for key in sorted(resto_ratings.keys()):
    print "Restaurant %s is rated at %d" % (key, resto_ratings.get(key))


#for key, value in sorted(set(resto_ratings.iteritems())): #you can't sort dictionary but can sort sets/lists
 #   print "Restaurant %s is rated at %d" % (key, value)


