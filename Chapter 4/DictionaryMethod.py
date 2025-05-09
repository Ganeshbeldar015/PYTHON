        
dict ={
    "name" : "Ganesh",
    "collge" : "NMIET",
    "cgpa" : "8.64",
    
}

print(dict.keys()) #return all keys
print(list(dict.keys())) #return all keys in list form

print(dict.values()) #return all values
print(list(dict.values())) #return all values in list form

print(dict.items()) #return all (key,val) pairs as tuples
print(list(dict.items())) #return all (key,val) pairs as tuples in the form of list

print(dict.get("name")) #returns the key  according to value
print(list(dict.get("name"))) #returns the key  according to value in list form

# new ={"city":"pune"}
# dict.update(new)
# print(dict)
dict.update({"city":"pune"})
print(dict)
