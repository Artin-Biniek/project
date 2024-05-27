import json
"""
1)Identify all attributes,all types,all domains


"""
"""

1)Pass in JSON
2)Iterate over elements of JSON
3)Check if elements belong to one of the valid attributes and check if its a dictionary
4)If dictionary pass it once again as the new JSON
5)Keep going until you find that its no longer a dictionary value
6)It will automatically stop at that value and continue on with the next elem in the list when
those child elements are done it will move to the next parent elements and so on.
"""
#Checking valid attributes
def test(X):
    for elem in X:
        if elem in attributes and isinstance(X[elem],dict):
            print(elem)
            #Obtaining child attributes
            print(X[elem])
            test(X[elem])
        elif elem in attributes and not isinstance(X[elem],dict):
            print(elem)
            print(X[elem])
        else:
            print("invalid")
            exit()



#Domain checking


#Example
json_string= '''
{
    "@context":{
        "@id":{
            "@id":"temp",
            "@id2":{
                "@id2":"temp2"
            }
        },

        "@id2":{
            "@id":"temp3",
            "@id2":"temp4"
        }
    }
}

'''

attributes=["@context","@id","@id2"]

data=json.loads(json_string)
test(data)

