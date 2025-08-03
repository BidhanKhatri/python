# Dictionary methods 

# items(), keys(), values(), update(), get(), clear(), copy(), pop(), popitem()

bidhan_info = {
    "name": "Bidhan",
    "from": "Nepal",
    "marks": [40,68,77,99],
} 

# items() method
print(bidhan_info.items()) # return key and value pairs [('name', 'Bidhan'), ('from', 'Nepal'), ('marks', [40, 68, 77, 99])]

#keys() method

print(bidhan_info.keys()) # return list of keys ['name', 'from', 'marks']
print(bidhan_info.values()) # return list of values ['Bidhan', 'Nepal', [40, 68, 77, 99]]

#update() method
bidhan_info.update({"from" : "China", "address":"Cheu Chang" })
print(bidhan_info)

#clear() method
print("Clear data: ", bidhan_info.clear())

#get() method
# print(bidhan_info.get("agghhauogh")) # return (None) 
# print(bidhan_info["gasufha"]) # return (error)

#copy() method
copied_data = bidhan_info.copy()
print("copied data", copied_data)

#pop() method
popped_data = bidhan_info.pop("marks")
print("popped data: ", popped_data)




