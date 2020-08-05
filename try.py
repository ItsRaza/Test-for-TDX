from geopy.geocoders import Nominatim
from geopy.distance import great_circle


geolocator = Nominatim(user_agent="Saffona")
location1 = geolocator.geocode("87/B Alamgir Society Malir Karachi")
print('\n')
pointA = location1.address
print("point A=", pointA)
A = (location1.latitude, location1.longitude)
print(A)
print('\n')

location2 = geolocator.geocode("175 5th Avenue NYC")

print('\n')

pointB = location2.address
print("point B=", pointB)
B = (location2.latitude, location2.longitude)
print(B)

# calculating distance

print("Distance =", great_circle(A, B).kilometers, "km")
