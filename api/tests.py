


givendata = [ ]
required_data =  [('Kyc_Document',), ('Account_details',), ('PAN',)]
b = []
for data in required_data:
  a = True
  for x in givendata:
    if x[0].upper() == data[0].upper():
        a = False
        break
  if a :
      b.append(data[0])

print(b)