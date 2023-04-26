# nested dictionary
family={
    'father':{'age':45,'name':'hari','hobby':'cooking'},
    'mother':{'age':42,'name':'laxmi','hobby':'traveling'},
    'brother':{'age':18,'name':'bishal','hobby':'farming'}
}
print(family['father'])
print(family['mother'])
print(family['brother'])

for m,n in family.items():
    print(m,n)