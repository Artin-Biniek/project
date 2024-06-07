import json
import validators
import re
import os
"""
1)Identify all attributes,all types,all domains
2)Future checks parameter and value relationship check
3)Parent and child checks
4)parent and child of child.... relationship checks.

"""
"""

1)Pass in JSON
2)Iterate over elements of JSON
3)Check if elements belong to oe of the valid attributes and check if its a dictionary
4)If dictionary pass it oncen again as the new JSON
5)Keep going until you find that its no longer a dictionary value
6)It will automatically stop at that value and continue on with the next elem in the list when
those child elements are done it will move to the next parent elements and so on.
"""


#Type can be a namespace, or of a specific name

#Checking what type exists so we can know what schema we are dealing with
def checkType(X,dictTemp):
    typeValues=[]
    for elem in X:
        if(elem=="type"):
            for elem2 in X[elem]:
                if(elem2 in dictTemp["@context"]):
                  typeValues.append(elem2)

    return typeValues

#Comparing the parsed JSON-ld with the schema we are dealing with


def temp(dictTemp,X,valBool):
    valBool=False
    for elem in X:
        for elem2 in dictTemp:
            if(elem==elem2 or "@"+elem==elem2):
                print(elem, "and",elem2,"are the same attribute")
                if(isinstance(X[elem],dict)) or (isinstance(X[elem],list)):
                  if len(X[elem])==0:
                    #print("Fails1")
                    return #exit()
                  for i in X[elem]:
                    if isinstance(X[elem],dict) and isinstance(dictTemp[elem2],dict) or (isinstance(X[elem],list) and isinstance(i,dict)) :
                        #print("testing")
                        if(isinstance(i,dict)):
                          if len(i)==0:
                           # print("Fails1")
                            return #exit()
                          else:
                            keys_list = [list(d.keys()) for d in X[elem]]
                            for sublist in keys_list:
                              testing=[]
                              #print("Sublist:",sublist)
                              for item in sublist:
                                  testing.append(item)
                              for f in data2[elem]:
                                if f not in testing:
                                  print("FAILED")
                                  return #exit()
                            print(i)
                            temp(dictTemp[elem2],i,valBool)
                        
                        else:
                          value=X.get(elem)
                          key_list=list(value.keys())
                          testing=[]
                          for item in key_list:
                            testing.append(item)
                          for f in data2[elem]:
                            if f not in testing:
                              print("FAILED")
                              return
                          print(X[elem])
                          temp(dictTemp[elem2],X[elem],valBool)
                #checking if value type is same
                if not isinstance(X[elem],dict):
                    if X[elem]==None:
                      print("Failed")
                      return #exit()
                    if elem=="type":
                        if isinstance(X[elem],str):
                          print("it is a string type")
                          valBool=True
                        elif all(isinstance(item, str) for item in X[elem]):
                          print("it is a list of strings")
                          valBool=True
                        elif validators.url(X[elem]):
                          print("It is a url value type")
                          valBool=True
                        else:
                          print("Fails2")
                          return
                    elif elem=="id":
                        if(re.search("^did:.+:.+$",X[elem])):
                            print("It is a DID value type")
                            valBool=True
                        elif validators.url(X[elem]):
                          print("It is a url value type")
                          valBool=True
                        else:
                          print("Failed3")
                          return #exit()

                    elif elem=="issuer":
                      if(re.search("^did:.+:.+$",X[elem])):
                          print("It is a DID value type")
                          valBool=True
                      else:
                          print("Failed3")
                          return #exit()
                    
                    elif elem=="@context":
                      for data[elem], x in enumerate(data[elem]):
                            if data[elem]==0:
                              if x=="https://www.w3.org/ns/credentials/v2" or  x=="https://www.w3.org/2018/credentials/v1":
                                print("its a url value type")
                              else:
                                print("Failed")
                                return #exit()
                            if data[elem]!=0:
                              if validators.url(x):
                                print("It is a url value type")
                                valBool=True
                              else:
                                print("Failed")
                                return #exit()

                      

    #For now keep it commented
    #if valBool==False:
    #  print("Could not find attribute",elem)
    #  exit()

    return valBool


#Example

json_string= '''
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2"
  ],
  "type": [
    "VerifiableCredential"
  ],
  "refreshService": [
    {
      "type": "https://example.org/#ExampleTestSuiteRefreshService",
      "id": "did:example:refresh/2"
    },
    {
      "type": "https://example.org/#ExampleTestSuiteRefreshService",
      "id": "did:example:refresh/3"
    }
  ],
  "issuer": "did:example:issuer",
  "credentialSubject": {
    "id": "did:example:subject"
  }
}
'''
#Required  refers to mandatory child,and parent properties

required='''
{

  "VerifiableCredential":["type","credentialSubject","issuer"],
  "VerifiablePresentation":["type"],
  "credentialStatus":["type"], 
  "credentialSchema":["type","id"],
  "termsOfUse":["type"], 
  "evidence":["type"], 
  "issuer":["id"], 
  "refreshService":["type"],
  "ProblemDetails":["title","detail"],
  "languageValueObject":["@value"]

}
'''

with open('op.txt', 'r') as file:
        dictTemp = json.load(file)

data2=json.loads(required)
data=json.loads(json_string)
typeValues=checkType(data,dictTemp)

listTemp=[]
check=False
for elem in data:
  for i in typeValues:
    if elem in data2[i]:
      listTemp.append(elem)
      if len(listTemp)==len(data2[i]):
        check=True
if not check:
  print("False")
        #exit()
dictTemp=dictTemp["@context"][typeValues[0]]["@context"]
dictTemp["@context"]="https://www.w3.org/ns/credentials/v2"
valBool=False
print(temp(dictTemp,data,valBool))





"""
dir='./tests/input/'
files=os.listdir(dir)
for f_name in files:
    print(f_name)
    with open(dir + f_name,'r') as file:
         data=json.load(file)



    with open('op.txt', 'r') as file:
        dictTemp = json.load(file)

    data2=json.loads(required)
    #data=json.loads(json_string)
    typeValues=checkType(data,dictTemp)

    try:
      listTemp=[]
      check=False
      for elem in data:
        for i in typeValues:
          if elem in data2[i]:
            listTemp.append(elem)
            if len(listTemp)==len(data2[i]):
              check=True

      if not check:
        print("False")
        #exit()


      dictTemp=dictTemp["@context"][typeValues[0]]["@context"]
      dictTemp["@context"]="https://www.w3.org/ns/credentials/v2"
      valBool=False
      print(temp(dictTemp,data,valBool))

    except Exception as e:
      print(f'validation failed for file {f_name}')
      print(e)
"""

