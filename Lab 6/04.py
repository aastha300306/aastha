import operator 
l=[('kurkure',20),('popcorn',200),('waffer',50),('good day',40)]
print(sorted(l,key=operator.itemgetter(1)))