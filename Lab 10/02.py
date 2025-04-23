import csv
myfile=open("text.csv",'r')
sw=csv.DictReader(myfile)
sum1=0
for i in sw :
   print(i)
   sum1=sum1+int(i['marks'])
print(sum1)   
myfile.close()