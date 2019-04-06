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
@dev main function that does everything
'''
def operate():
    to=input("address to\n")
    frm=input("address from\n")
    dist =distance(to,frm)
    dist=toKilometers(dist)
    requiredCo2=getrequireCO2(dist)
    metric=tometricTonne(requiredCo2)
    print("C02 required in metric tonne: ",metric)
operate()