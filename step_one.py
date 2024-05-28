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
            #print(elem)
            #print(X[elem])
            test2(X[elem])
        else:
            print("invalid")
            exit()


"""
context:
is a valid url that first elem is https://www.w3.org/ns/credentials/v2
the next 1...n elements is any existing url https:// || http:// (a string type)

Id(as a parent):
an existing url http://(a string type)

Id(as a child of credential subject)
did:sometext:sometext(a string type)

Type(parent,can be a child of Vc object,verifiable presentation object,credentialStatus object,termsOfUse object,Evidence object):
[someName,....,SomeNameN](string type) or Absolute Url [https://www.something.com...](string)

Names:
Can be a string "SomeName" or language value object

language value object
contains @value(a string value),@language(language tag),and may contain @direction(base direction string).




"""
#Type checking
def test2(elem):
    print("temp")
    if elem in values:
        print(type(elem))
    else:
        print("invalid")
        exit()


#Example
json_string= '''
{
    "@context":{
        "@type":{
            "aud":"@id",
            "@protected": 100

        }
    }
}

'''
def get_keys(data):
    keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            keys.append(key)
            keys += get_keys(value)
    elif isinstance(data, list):
        for value in data:
            keys += get_keys(value)
    return keys

def get_values(data):
    values = []
    if isinstance(data, dict):
        for value in data.values():
            values += get_values(value)
    elif isinstance(data, list):
        for item in data:
            values += get_values(item)
    else:
        values.append(data)
    return values


with open('op.txt', 'r') as file:
    data = json.load(file)


attributes=set(get_keys(data))

values=set(get_values(data))

#attributes=["@context","@id","@id2"]
data=json.loads(json_string)
test(data)

