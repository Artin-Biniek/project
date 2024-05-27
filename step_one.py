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
valid_attributes=dict2[X]
print(child_attributes)

#If child attributes do exist do the following 
if isinstance(child_attributes, dict):
    #Iterate over the valid child attributes    
    for key in child_attributes:
        for child in valid_attributes:
            if(child==key):
                #If valid we dont need to check this attribute anymore
                valid_attributes.pop(0)
                print(key)
                print(child)
                break
            else:
                print(key)
                print(child)
                print("Invalid JSON")
                exit()

#Next we check all domains

#To check for valid values see if it matches the conditions for a value

