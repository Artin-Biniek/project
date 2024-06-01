import json
import validators
import re
"""
1)Identify all attributes,all types,all domains
2)Future checks parameter and value relationship check
3)Parent and child checks
4)parent and child of child.... relationship checks.

"""

#Building dictionary
def buildingDict(X):
   dictTemp={}
   for elem in X:
    if isinstance(X[elem],dict):
        print("test")
        dictTemp |= {elem:X[elem]}
        #print(dictTemp)
    elif isinstance(X[elem],list):
        dictTemp |= {elem:X[elem]}
    return dictTemp

#Checking to see if param:Value exist in dict like is there a way to go to that specified param and value?
def temp(dictTemp,X):
    for elem in X:
        #print(elem)
        for elem2 in dictTemp:
            #print(elem2)
            if(elem==elem2):
                print(elem, "and",elem2,"are the same attribute")
                if isinstance(X[elem],dict) and isinstance(dictTemp[elem2],dict) :
                    temp(dictTemp[elem2],X[elem])

                #checking if value type is same
                elif not isinstance(X[elem],dict) and not isinstance(dictTemp[elem2],dict) :
                    if type(X[elem])==type(dictTemp[elem2]):
                        if isinstance(X[elem],str) and isinstance(dictTemp[elem2],str):
                                if validators.url(X[elem]) and validators.url(dictTemp[elem2]):
                                    print("It is a url type")
                    else:
                        print(type(X[elem]),"and",type(dictTemp[elem2]),"have the same value type")




#Example

json_string= '''
{
    "@context":{
        "@protected":true,
        "@vocab": "https://www.w3.org/ns/credentials/issuer-dependent#",
        "kid":{
            "@type": "w3c.org"

        }
    }
}
'''


with open('op.txt', 'r') as file:
    data = json.load(file)

dictTemp={}
dictTemp=buildingDict(data)
#print(dictTemp["@context"])
#dictTemp.update({key1,val1})

"""
ValueType:{"@type":"url"}
IdType:{"@Id":"did:something:something2",url}

"""


data=json.loads(json_string)
temp(dictTemp,data)


