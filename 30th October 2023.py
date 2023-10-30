# Program1
"""Find the maximum and minimum elements in a tuple."""
my_tuple=(15,8,25,36,42,10)
print(max(my_tuple))
print(min(my_tuple))

# Program2
"""Find the intersection and Union of two sets."""
#-----INTERSECTION------
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.intersection(set2))

#-----OR-------
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set3=set1.intersection(set2)
print(set3)

#------UNION_____
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.union(set2))
#-----OR-----
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set3=set1.union(set2)
print(set3)

# Program3:
"""Remove duplicates elements from a list:"""
my_list=[1,2,2,3,4,4,5]
my_list=list(dict.fromkeys(my_list))
print(my_list)

#Program4
"""Remove a key-value pair from the dictionary"""
student={"name":"John","age":20,"class":"xii"}
student.pop("class")
print(student)

#Program5
"""Convert to Dict JSON
Response and Print and Booking Id And checkin and checkout Data"""
import json
passenger={
    "bookingid":2384,
    "booking":{
        "firstname":"Pramod",
        "lastname":"Dutta",
        "totalprice":432,
        "depositepaid":False,
        "bookingdates":{
            "checkin":"2022-01-01",
            "checkout":"2022-01-01"
        },
        "additionalneeds":"Lunch"
    }
}

print(passenger)
print("Bookingid:",passenger["bookingid"])
print("Checkin:",passenger["booking"]["bookingdates"]["checkin"])
print("Checkin:",passenger["booking"]["bookingdates"]["checkout"])