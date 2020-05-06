# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


# YOUR CODE HERE
class LatLon:
    def __init__(self,lat,lon, **kw):
        self.lat = lat
        self.lon = lon
        super().__init__(**kw)
    def description(self):    
        return f'this is the lat: {self.lat} and lon:{self.lon} of my location'



myPlace = LatLon(23,22)
print(myPlace.description())

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self,name, **kw):
        self.name = name
        super().__init__(**kw)

    def __str__(self):
        return f"<Waypoint {self.name},{self.lat},{self.lon} >"
    
    def myname(self):
        return f'My name is {self.name}'


way = Waypoint('Jose',lat=23,lon=22)

print(way)
# print(way.myname(), way.description())





# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self,difficulty,size, **kw):
        self.difficulty = difficulty
        self.size = size
        super().__init__(**kw)


    def howHard(self):
        return f'level of difficulty is {self.difficulty}, the size of is {self.size}, the lat: {self.lat}, lon is {self.lon}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

CataCombs = Geocache(lat=23,lon=33,size="huge",name="Catacombs",difficulty="Hard")
print(CataCombs.howHard())



# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
# class Animal:
#   def __init__(self, animalName):
#     print(animalName, 'is an animal.');

# Mammal inherits Animal
# class Mammal(Animal):
#   def __init__(self, mammalName):
#     print(mammalName, 'is a mammal.')
#     super().__init__(mammalName)