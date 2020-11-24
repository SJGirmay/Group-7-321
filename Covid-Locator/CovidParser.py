States = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut",
"delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana",
"maine","maryland","massachusetts","michigan","minnesota","mississippi","missouri","montana","nebraska",
"nevada","new hampshire","new jersey","new mexico","new york","north carolina","north dakota","ohio",
"oklahoma","oregon","pennsylvania","rhode island","south carolina","south dakota","tennessee","texas",
"utah","vermont","virginia","washington","west virginia","wisconsin","wyoming"]

StateAbv= ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
"KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NE","NH","NJ","NM","NY","NC",
"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

#,"district of columbia","DC","washington dc"
def CovidParser(resp):
  resp1 = resp.lower()
  resp2 = resp.upper()
  if(resp1 in States):
    print(StateAbv[States.index(resp1)])
  elif(resp2 in StateAbv):
    print(resp2)
  elif(resp1 == 'q' or resp1 == 'quit'):
    quit()
  else:
    resp = input('Invalid Input. Please Enter valid State or State Abreviation. ')
    CovidParser(resp)

resp = input('Please enter a valid state or state Abreviation. To quit, enter q or quit. ')
CovidParser(resp)    