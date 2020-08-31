Lists =[["xbox",4],["Gta V",1],
          ["pirates",2],["Naruto",3]]
dict1 = dict(Lists)
print(dict1)
for items in dict1:
    print(items)
# for item, Gaming_time in dict1.items():
#     print( item,"and gaming is majedar gaming",Gaming_time)

items = [int , float , "laksh", 2,4,6,556,74,890,246,64]

for item in items:
    if str(item).isnumeric() and item >=6:
        print(item)
