destinations = [
  "Paris, France",
  "Shanghai, China",
  "Los Angeles, USA",
  "Sao Paulo, Brazil",
  "Cairo, Egypt"
]
test_traveler = [
  'Erin Wilkes',
  'Shanghai, China',
  ['historical site', 'art']
]
def get_destination_index(destination):
  #for i in range(len(destinations)):
  #  if destinations[i] == destination:
  #    destination_index = i
  destination_index = destinations.index(destination)
  return destination_index
#print(get_destination_index('Los Angeles, USA'))
#print(get_destination_index('Paris, France'))
#print(get_destination_index('Hyderabad, India'))
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#print(get_traveler_location(test_traveler))

attractions = []
for destination in destinations:
  attractions.append([])
#print(attractions)
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions[destination_index].append(attraction)
  return attractions
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction('Paris, France', ['the Arc de Triomphe', ['monument']])
add_attraction('Paris, France', ['the Louvre', ['art', 'museum']])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
#  print(attractions_in_city)
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
la_arts = find_attractions('Los Angeles, USA',['art'])
#print(la_arts)
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interests_string = ["Hi ", traveler[0], ", we think you'll like these places around ", traveler_destination, ": "]
  for attraction in traveler_attractions:
    interests_string.append(attraction)
  string = ''
  for i in interests_string:
    string += i
  return string
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
