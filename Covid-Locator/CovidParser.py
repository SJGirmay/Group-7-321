import pip._vendor.requests
import json

StateAbv= ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
"KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NE","NH","NJ","NM","NY","NC",
"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

StatesLower = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut",
"delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana",
"maine","maryland","massachusetts","michigan","minnesota","mississippi","missouri","montana","nebraska",
"nevada","new hampshire","new jersey","new mexico","new york","north carolina","north dakota","ohio",
"oklahoma","oregon","pennsylvania","rhode island","south carolina","south dakota","tennessee","texas",
"utah","vermont","virginia","washington","west virginia","wisconsin","wyoming"]

States = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
"Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana",
"Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska",
"Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
"Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas",
"Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

#Add DC later

def CovidParser(resp):
  resp1 = resp.lower()
  resp2 = resp.upper()
  if(resp1 in StatesLower):
    return(States[StatesLower.index(resp1)])
  elif(resp2 in StateAbv):
    return(States[StateAbv.index(resp2)])
  elif(resp1 == 'q' or resp1 == 'quit'):
    quit()
  else:
    resp = input('Invalid Input. Please Enter valid State or State Abreviation. ')
    CovidParser(resp)
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

resp = input('Please enter a valid state or state Abreviation. To quit, enter q or quit. ')
baseUrl = "https://corona.lmao.ninja/v2/states/"
inputVar = CovidParser(resp) 
EndVar = "?yesterday="
result = (baseUrl + inputVar + EndVar)
response = pip._vendor.requests.get(result)
jprint(response.json())
