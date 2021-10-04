from geopy.geocoders import Nominatim

appName = "jwst-demo-panda"
geolocator = Nominatim(user_agent=appName)

fenwayLatitude = 42.34671602665354
fenwayLongitude = -71.09718561498757

location = geolocator.reverse( query=(fenwayLatitude, fenwayLongitude) )
print(location.address)

locationDataset = location.raw
address = locationDataset["address"]
if "city" in address:
    print(address["city"])
if "town" in address:
    print(address["town"])
print(address["county"])
print(address["state"])
print(address["postcode"])
print(address["country"])
print(locationDataset)

jlsLatitude = 42.416381737534806
jlsLongtitude = -71.15867815731357

location = geolocator.reverse( query=(jlsLatitude, jlsLongtitude) )
print(location.address)

locationDataset = location.raw
address = locationDataset["address"]
if "city" in address:
    print(address["city"])
if "town" in address:
    print(address["town"])
print(address["county"])
print(address["state"])
print(address["postcode"])
print(address["country"])
print(locationDataset)
