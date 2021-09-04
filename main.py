import requests
import json
import sys
from datetime import datetime



def main():
  print ("Welcome to Travel Planner!")
  UserEmail=input("Enter your email address:" )
  cityObj=getCity()
  arrivalDate=getArrivalDate()
  departureDate=getDepartureDate()
  #flightChoice= getFlightOptions(cityObj["airport_code"],arrivalDate,departureDate)
  interests=getInterests()
  activities= getActivties(interests,cityObj["city"])
  weather=getWeather(cityObj["city"],cityObj["state"])
  email=sendEmail(cityObj,arrivalDate,departureDate,interests,activities,weather,UserEmail)
''' --- Core Functions ---'''
def getCity():
  InputCity=(input("Where are you looking to go?\n"))
  checkAirportCodeResult = checkAirportCode(InputCity)
  if (checkAirportCodeResult != ""):
    print ("Ok, "+ InputCity + " it is!")
  else:
    print ("Sorry, this is invalid, please try again.")
    getCity() 
  return checkAirportCodeResult
  return InputCity


def getArrivalDate():
  InputArrival= (input("What day are you arriving? (YYYY-MM-DD)\n"))
  return InputArrival

def getDepartureDate(): 
  InputDeparture= (input("What day are you leaving? (YYYY-MM-DD)\n"))
  return InputDeparture

'''
def getFlightOptions(city,arrivalDate,departureDate):
  listOfFlights = []
  url=('http://api.aviationstack.com/v1/flights?access_key=808ca8d914a14efbe67cbf7630d0d9cc')
  api_result = requests.get(url)
  resultjson=(api_result.json())
  data=(resultjson["data"])
  x=0 
  print ("Please select your flight\n")
  while x<3:
    print ("-")
    flightinfo={}
    individualflight=(data[x])

    departureTime = datetime.strptime(individualflight["departure"]["scheduled"][:-6],"%Y-%m-%dT%H:%M:%S")
    prettyDepartureTime =departureTime.strftime('%H:%M')
    arrivalTime = datetime.strptime(individualflight["arrival"]["scheduled"][:-6],"%Y-%m-%dT%H:%M:%S")
    prettyArrivalTime =arrivalTime.strftime('%H:%M')

    flightinfo["Flight Date"]=(individualflight["flight_date"])
    flightinfo["Departure Time"]=prettyDepartureTime
    flightinfo["Arrival Time"]=prettyArrivalTime
    flightinfo["Airline"]=(individualflight["airline"]["name"])
    flightinfo["Flight"]=(individualflight["flight"]["iata"])
    listOfFlights.append(flightinfo)
    
    y=x+1
    print ("Flight "+str(y)+"\n Airline: "+flightinfo["Airline"]+"\n Flight: "+flightinfo["Flight"]+"\n Flight Date: "+flightinfo["Flight Date"]+"\n Departure Time: "+flightinfo["Departure Time"]+"\n Arrival Time: "+flightinfo["Arrival Time"])
    x=x+1

  InputFlightChoice= int(input("\n Select a flight: "))
  FlightChoice = listOfFlights[InputFlightChoice-1]
  print ("\nYou selected: "+ "Flight "+str(InputFlightChoice)+"\n Airline: "+FlightChoice["Airline"]+"\n Flight: "+FlightChoice["Flight"]+"\n Flight Date: "+FlightChoice["Flight Date"]+"\n Departure Time: "+FlightChoice["Departure Time"]+"\n Arrival Time: "+FlightChoice["Arrival Time"])
  return FlightChoice
'''
def getInterests():
  listOfInterests= []
  print ("\n What 3 activites do you want to do? \n (Museums, Architecture, Amusement Parks, etc.)")
  firstInterest = input("1. ")
  secondInterest = input("2. ")
  thirdInterest = input("3. ")
  listOfInterests.append(firstInterest)
  listOfInterests.append(secondInterest)
  listOfInterests.append(thirdInterest)
  return listOfInterests

def getActivties(interests,userCity):
  listOfActivities=[]
  x=0
  while x<3:
    z=0
    listOfInterestOptions=[]
    response = requests.get(
      'https://api.yelp.com/v3/businesses/search',
      params={'term': interests[x],'location':userCity,'limit':3},
      headers={'Authorization': 'Bearer HjwdPu3StGxFiQzXBCokNDyoe7T0I-KfIR7IQ2Td97DSF8sANoFkWZOR5I77mI5zCGRUU6_z-1tSCHmqfAghaJiay-qWgHgM0hDhCQFLPbAidWMLBvtpLwyd2XTOYHYx'})
    resultjson=(response.json())
    businesses = (resultjson["businesses"])
    print ("-")
    print ("Activity: "+interests[x])
    while z<3:
      
      activityInfo={}
      individualActivity = (businesses[z])
      activityInfo["Name"]=(individualActivity["name"])
      activityInfo["Address"]=(individualActivity["location"]["address1"])
      activityInfo["City"]=(individualActivity["location"]["city"])
      activityInfo["State"]=(individualActivity["location"]["state"])
      activityInfo["PhoneNum"]=(individualActivity["display_phone"])
      activityInfo["Rating"]=str(individualActivity["rating"])
      y=z+1 
      
      print ("Location "+ str(y)+": "+activityInfo["Name"]+"\n Address: "+ activityInfo["Address"]+", "+activityInfo["City"]+", "+activityInfo["State"]+"\n Phone Number: "+activityInfo["PhoneNum"]+"\n Rating: "+ activityInfo["Rating"])
      listOfInterestOptions.append(activityInfo)
      z=z+1  
    InputActivityChoice=(int(input("Which location would you like to go to? \n")))
    listOfActivities.append(listOfInterestOptions[InputActivityChoice-1])
    x=x+1
  return listOfActivities

def getWeather(city, state):
  
  response = requests.get('https://api.openweathermap.org/data/2.5/weather',
  params={'q':city+","+state,'units':"imperial",'appid':"4495c9670d86351a36efd13d93dc8a32"})
  resultjson=(response.json())
  temp=(resultjson["main"]["temp"])
  description=(resultjson["weather"][0]["main"])
  weatherInfo={'temp': temp,'description':description}
  return weatherInfo 

def sendEmail(cityObj,arrivalDate,departureDate,interests, activities,weather,email): 
  success = False

  emailContent={"city1":"San Francisco","city2":cityObj["city"],"state1":"CA","state2":cityObj["state"][3:],"airportCode1":"SFO","airportCode2":cityObj["airport_code"],"departureDate":departureDate, "arrivalDate":arrivalDate,"interest1":interests[0],"interest2":interests[1],"interest3":interests[2],"activity1":activities[0],"activity2":activities[1],"activity3":activities[2],"temp1":"60","description1":"Cloudy","weather":weather}
  response = requests.post(
      "https://api.sendgrid.com/v3/mail/send",
      json={'from':{"email":"arhumk2430@gmail.com"},"personalizations":[{"to":[{"email":email}],"dynamic_template_data":emailContent,}],"template_id":"d-a02cfd7df0fb46308c9da18d59693541"},
      headers={'Authorization': 'Bearer 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','Content-Type':'application/json'})
  return success

''' ---- Helper Functions ---'''
def checkAirportCode(inputCity):
  # Opening JSON file
  f = open('airportData.json')
  # returns JSON object as 
  # a dictionary
  data = json.load(f)
  cityFound = False 
  cityObject = {}
  # Iterating through the json
  # list
  for i in data:
    if(i["iata_code"] == inputCity):
      cityFound = True
      cityObject["airport_code"] = i["iata_code"]
      cityObject["city"] = i["municipality"]
      cityObject["state"]= i["iso_region"]
  # Closing file
  f.close()
  if (cityFound):
    return cityObject
  else:
    return ""

main()

''''
-format and email report/ text messages
-fix email format
-add current weather/current location
-mispelled activities
-location not found yelp
''' 