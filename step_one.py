import json
"""
1)Identify all attributes,all types,all domains


"""

#Example
json_string= '''
{
    "@context":{
        "@id":"https://www.w3.org/ns/credentials/v2",
        "@type": "https://www.w3.org/2001/XMLSchema#nonNegativeInteger"
    
    }
}

'''

parent_attributes=["@context"]
#Concerned about child attributes
dict2={
    "@context":["@id","@type"]
    
    
    
    }
#Concerned about values of child attributes or of parent attributes
dict3={


}



X="tempString"

#1)Automatically identify the parent_attributes for a given JSON
data=json.loads(json_string)
for attribute in data:
    #Check to see if attribute is a valid attribute
    if(attribute in parent_attributes):
        X=attribute
        print(attribute)
    else:
        print("Invalid Json")
        exit()


#2)Automatically identify the child attributes


#Obtain the child attributes
child_attributes=data.get(X)
print(child_attributes)

print(dict2[X])
if isinstance(child_attributes, dict):
    for key in child_attributes:
        if(key in dict2[X]):
            print("True")
        else:
            print("Invalid Json")
            exit()

print("It passed")
#Next we check all domains

#To check for valid values see if it matches the conditions for a value

