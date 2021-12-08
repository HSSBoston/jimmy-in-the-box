from geopy.geocoders import Nominatim

appName = "panda-admirer"
geolocator = Nominatim(user_agent=appName)

searchKeywords = "Fenway Park"
location = geolocator.geocode(query=searchKeywords, addressdetails=True)
print(location.address)
locationDataset = location.raw
print("Fenway's latitude and longitude: " + locationDataset["lat"] + ", " + locationDataset["lon"])

fenwayAddress = "4 Jersey Street, Boston, MA 02215"
location = geolocator.geocode(query=fenwayAddress)
locationDataset = location.raw
print("Fenway's latitude and longitude: " + locationDataset["lat"] + ", " + locationDataset["lon"])

structuredQuery = { "street" : "4 Jersey St",
                    "city" : "Boston",
                    "state" : "MA",
                    "postalcode" : "02215",
                    "country" : "United States" }
location = geolocator.geocode(query=structuredQuery)
locationDataset = location.raw
print("Fenway's latitude and longitude: " + locationDataset["lat"] + ", " + locationDataset["lon"])

