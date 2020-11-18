import random
import math 

class City():  #each city is a node for traveling salesman problem

	def __init__(self, number):
		self.number = number 
		self.x = random.randint(0,200) # x-coordinate
		self.y = random.randint(0,200) # y-coordinate
		self.searched = False

	def getX(self):                              #get x-coordinate
		return(self.x)

	def getY(self):                              #get y-coordinate
		return(self.y)

	def getCoordinate(self):                     #return coordinates of city in a tuple (x,y)
		return((self.x,self.y))

	def setSearchStatus(self):                   #set search status to True 
		self.searched = True 

	def getSearchStatus(self):                   #return search status 
		return(self.searched)

	def distanceTo(self, city):                  #returns euclidean distance from this city to another
		xD = abs(self.getX()-city.getX())
		yD = abs(self.getY()-city.getY())
		distance = math.sqrt((xD*xD)+(yD+yD))
		return(distance)


class Country(): #a country is an object/data structure to hold all nodes(Cities) for TSP

	def __init__(self, c):                       
		self.cities = c[:]

	

	def numberOfCities(self):                    #returns the number of cities in country
		return(len(self.cities))

	def shuffleCities(self):                     #shuffles the cities and sends out a copy
		random.shuffle(self.cities)

	def getCities(self):
		return(self.cities[:])

	def printCities(self):
		i = 0
		for city in self.cities:
			print("For "+str(i)+" city: x="+str(city.x)+" y="+str(city.y))
			i+=1

	def costOfRoute(self):								#sum the distance between each city: d(c0,c1)+d(c1,c2)+...+d(cn-1,cn)+d(cn,c0)
		total = 0
		i = 0
		n = len(self.cities)
		while i < (n-1):
			total += self.cities[i].distanceTo(self.cities[i+1])
			i+=1
		total += self.cities[n-1].distanceTo(self.cities[0])
		return(total)

	def numberOfSwapsTo(self, country):          		#returns the number of swaps needed to turn countries.cities into country.cities
		toSwap = []
		total = 0
		i = 0
		temp_country = Country(country.cities[:])
		for element in self.cities:
			j = temp_country.cities.index(element)
			if j != i: 									#if the index of element is not the same in both, then a swap is needed
				toSwap.append((i,j))
				total+=1
				temp_country.swapOp([(i,j)],1)
			i+=1
		return(total-1, toSwap) 						#there will always be one less swap needed that the number of elements out of order

	def swapOp(self, toSwap, n):						#toSwap is list of tuples:(index1,index2) where n elements of the list are used to swap index1,index2
		i = 0
		while i < n:
			a,b = toSwap[i]
			temp = self.cities[a]
			self.cities[a] = self.cities[b]
			self.cities[b] = temp
			i+=1

	




	