import etherscan
import requests
from datetime import datetime

'''
@dev given to address extracts the last 10 characters from them and converts them to
hex then calculates the distance in meters between the 2
@param to destination address
@param frm source address
<return>returns absolute distance between the to and from address</return>
'''
def distance(to,frm):
    if len(to) != 42 and len(frm) != 42:#@dev ensure that we have the correct lenght of an address
        return
    to=to[-10:]
    frm=frm[-10:]
    return abs(int(to,16)-int(frm,16))

'''
@dev return the the given distance in meters to kilometers (rounded off)
@param meters distance to be converted to kilometers
<return>converted distance in kilomters </return>
'''
def toKilometers(meters):
    return round(meters/1000)
'''
@dev returns the amount of co2 required based on the Kilometers passed in to the function
@param Km kilomoters
<return> returns the total amount of Co2 required </return>
'''
def getrequireCO2(km):
    return km*100

'''
@dev converts grams to metric tonnes
@param grams total number of grams to be converted
<return> returns the rounded off grams in metric tonnes </return>
'''    
def tometricTonne(grams):
    return round(grams/(1*10**6))
'''
@dev calculates requierd co2 using the given paramaters
@param to ethereum address the kitty is coming from
@param frm ethereum address is being sent to
'''
def calculateCO2(to,frm):
    dist =distance(to,frm)
    dist=toKilometers(dist)
    requiredCo2=getrequireCO2(dist)
    metric=tometricTonne(requiredCo2)
    #print("C02 required in metric tonne: ",metric)
    return metric
'''
@dev main function that does everything outputs file (Co2Required.txt) with all calculated c02 required for transfering kitties
'''
def process():
        address="0x06012c8cf97BEaD5deAe237070F9587f8E7A266d"
        url= "https://api.etherscan.io/api?module=account&action=txlist&address="+address+"&startblock=0&endblock=99999999&page=1&offset=1000000&sort=desc&apikey=YourApiKeyToken"
        response=requests.get(url)
        content=response.json()
        results=content.get("result")
        file=open("output.json","w")
        co2=open("Co2Required.txt","w")
        file.write(str(results))
        for n,transaction in enumerate(results):
            to=transaction.get("to")
            frm=transaction.get("from")
            timestamp=int(transaction.get("timeStamp"))
            co2Required=calculateCO2(to,frm)
            convertedTimestamp = datetime.fromtimestamp(timestamp)
            #print("to",to,"from",frm,"date",convertedTimestamp)
            line="address to: "+to+" address from: "+frm+" C02 Required in metric tonne: "+str(co2Required)+" Date: "+str(convertedTimestamp)
            co2.write(line)
            co2.write("\n")
        co2.close()

process()