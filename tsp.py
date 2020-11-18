import city 
import random

class TSP():

	def __init__(self,n):  				#n is the number of cities to be generated
		self.initial_cities = []
		self.countries = []
		i = 0
		while i < n:
			newCity = city.City(i)
			self.initial_cities.append(newCity)
			i+=1

	def makeCountries(self, n): 
		i = 0
		cities = self.initial_cities[:]
		while i < n:
			newCountry = city.Country(self.initial_cities)
			newCountry.shuffleCities()
			self.countries.append(newCountry)
			i += 1
		return(self.countries)

	def bestSolution(self):    #determines best solution and returns the country(agent) with the best solution
		min = 0
		min_agent = city.Country(self.initial_cities) 
		for country in self.countries:
			current = country.costOfRoute()
			if current < min:
				min = current 
				min_agent = country
		return (min_agent)


if __name__=="__main__":
	main()

	