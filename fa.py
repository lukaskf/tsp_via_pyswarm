import math
import numpy as np
import tsp
import city
import intelligence
import random


class fa(intelligence.sw):
    """
    Firefly Algorithm
    """

    def __init__(self, n, sizeTSP, dimension, iteration, csi=1, psi=1,
                 alpha0=1, alpha1=0.1, norm0=0, norm1=0.1):
        """
        :param n: number of agents
        :param function: test function
        :param lb: lower limits for plot axes
        :param ub: upper limits for plot axes
        :param dimension: space dimension
        :param iteration: number of iterations
        :param csi: mutual attraction (default value is 1)
        :param psi: light absorption coefficient of the medium
        (default value is 1)
        :param alpha0: initial value of the free randomization parameter alpha
        (default value is 1)
        :param alpha1: final value of the free randomization parameter alpha
        (default value is 0.1)
        :param norm0: first parameter for a normal (Gaussian) distribution
        (default value is 0)
        :param norm1: second parameter for a normal (Gaussian) distribution
        (default value is 0.1)
        """

        super(fa, self).__init__()

        t_s_p = tsp.TSP(sizeTSP)
        t_s_p.makeCountries(n)

        self.__agents = t_s_p.countries                            #MODIFIED  #need to have normal distribution of distances somehow within this range? current TSP just has complete randomness for points(permutations of cities) 
                                                                     #this just keeps a list of all the agents, TSP.country will solve this

        Pbest = t_s_p.bestSolution()                                         #use tsp.bestSolution() to get country with best solution
                                    
        Gbest = Pbest

        for t in range(iteration):

            alpha = alpha1 + (alpha0 - alpha1) * math.exp(-t)

            for i in range(n):
                fitness = [x.costOfRoute() for x in self.__agents]                 #fitness is a list where each element in the list is the cost/solution for each agent
                for j in range(n):
                    if fitness[i] > fitness[j]:
                        self.__move(i, j, t, csi, psi, alpha, dimension,
                                    norm0, norm1, n)
                    else:
                        num_mutate = random.randint(0,sizeTSP)
                        swaps = []
                        for index in range(0,num_mutate):
                            r1 = random.randint(0,n)
                            r2 = random.randint(0,n)
                            swaps.append((r1,r2))
                        self.__agents[i].swapOp(swaps,num_mutate)
            print(t)

           # self.__agents = np.clip(self.__agents, lb, ub)
        # self._points(self.__agents)

        #     Pbest = t_s_p.bestSolution()
        #     if Pbest < Gbest:
        #         Gbest = Pbest

        # self._set_Gbest(Gbest)
        print("---FA SOLUTION---")
        print(t_s_p.bestSolution().costOfRoute())
        print("-----------------")

    def __move(self, i, j, t, csi, psi, alpha, dimension, norm0, norm1, n):
        difference, swap_ops = self.__agents[i].numberOfSwapsTo(self.__agents[j])
        r = np.linalg.norm(difference)   
        beta = csi / (1 + psi * r ** 2)

        number = math.floor(math.sqrt(self.__agents[j].costOfRoute()) + beta * (difference) + alpha * math.exp(-t) * random.randint(0,n))
        if number>len(swap_ops):
            number = len(swap_ops)
        self.__agents[i].swapOp(swap_ops,number)
