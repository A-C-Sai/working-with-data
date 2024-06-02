import numpy as np
import matplotlib.pyplot as plt
import time

class KMeans:

    def __init__(self,n_clusters=3,n_init=10,max_iter=10,init='random'):
        '''
            n_clusters: The number of clusters
            
            n_init: Number of times the k-means algorithm is run with different centroid seeds to 
                    prevent local minimum problem.

            max_iter: Maximum number of iterations of the k-means algorithm for a single run.

            init: Method for centroids initialization
                  {‘k-means++’, ‘random’}
            
        '''
        self.init=init
        self.n_clusters=n_clusters
        self.n_init=n_init   
        self.max_iter=max_iter
        

    def __calculate_distance(self,centroids,data):

        # Calculate the distances b/w the training data points and the centroids
        # using matrix broadcasting
                                                                  
        c = centroids[np.newaxis,:] 
        
                                                                 
        d = data[:,np.newaxis] 
        
        d_matrix = np.sqrt(np.sum(np.square(c - d),axis=2)) # shape= no. of data points X number of centroids

        '''
            c_1 c_2 ... c_n
        p1  [             ]
        p2  [             ]
        p3  [             ]
        p4  [             ]
                    .
                    .
        pn  [             ]
        '''
        
        return d_matrix


    def __generate_colors(self):

        # generate unique color for each cluster
        return np.random.rand(self.n_clusters,3)
        

    # visualize training data and clusters color-coded for 2-d data
    def __plot_cluster(self,data,cluster,centroids,colors):
        plt.figure(figsize=(5,5))
        color=[colors[a] for a in cluster]
        plt.scatter(data[:,0],data[:,1],s=30,c=color,alpha=0.5)
        plt.scatter(centroids[:,0],centroids[:,1],s=500,c='white')
        plt.scatter(centroids[:,0],centroids[:,1],s=250,c='black')
        plt.scatter(centroids[:,0],centroids[:,1],s=80,c='yellow')
        plt.show()


    # generate initial centroids using k-means++ algorithm
    def __kmeanspp(self,data):

        xp=data.copy() # centroid candidates
        N=data.shape[0] # the number of data points
        centroids=[]
        density=np.ones(xp.shape[0])/N # uniform distribution is used as initial probability distribution

        for c in range(self.n_clusters):

            # (1) choose an initial centroid c(1) uniformly at random from X
            # (2) choose the next centroi c(i), selecting c(i) = x' E X with the probability density function

            idx=np.random.choice(np.arange(xp.shape[0]),p=density)
            centroids.append(xp[idx])
            xp=np.delete(xp,idx,axis=0)

            # Create a distance matrix b/w data points xp and the centroids.
            dist=self.__calculate_distance(np.array(centroids),xp)

            # find the centroid closest to each data point
            assign = np.argmin(dist,axis=1)

            # calculate D(x)
            # let D(x) denote the shortest distance from a data point x to the closest centroid we have already chosen
            Dx=np.sum(np.square(xp-np.array(centroids)[assign]),axis=1)

            # create a probability density function to select the next centroid
            density=Dx/np.sum(Dx)


        return np.array(centroids)
        
            
        
       


    def fit(self,data):
        
        self.f_error=[99999999999999999] # final error history
        self.f_centroids=None # final centroids
    
        
        if self.n_init==1:
            cluster_colors= self.__generate_colors()

        if self.init=='random':
            N=data.shape[0] # the number of data points

        for _ in range(self.n_init): # Repeat n_init times, changing the initial
                                     # positions of centroids
            
            # Initialize the centroids.
            if self.init=='random':
                # Randomly select n_clusters data points and use them as initial centroids.
                idx=np.random.choice(np.arange(N),self.n_clusters)
                centroids=data[idx]
            else:
                centroids=self.__kmeanspp(data)
            
            error=[] # error histor for current run of algorithm

            for _ in range(self.max_iter):

                dist=self.__calculate_distance(centroids,data)

                # assign each data point to the nearest centroid
                assign=np.argmin(dist,axis=1) # shape = np. of data points


                # update centroids
                new_cent=[]
                err=0
                for c in range(self.n_clusters):
                    # Find the data points assigned to centroid c
                    idx=np.where(assign==c)
                    data_idx=data[idx]

                    # the error is measured as the sum of the squares of the 
                    # distances b/w data points and their centroids
                    err+= np.sum(np.sum(np.square(data_idx-centroids[c]),axis=1))

                    # compute the average coordinates of the data points assigned to this centroid
                    # use this as new centroid
                    new_cent.append(np.mean(data_idx,axis=0))

                error.append(err) # tracking error history as centroids shift

                # To observe centroids moving set n_init=1
                if self.n_init==1:
                    self.__plot_cluster(data,assign,centroids,cluster_colors)
                    time.sleep(1)

                # update centroids
                centroids=np.array(new_cent)

            # Among the n_init number of iterations, the one with the smallest error
            # is selected as the final result
            # in case init is set to 'k-means++' n_init will be 1.
            if error[-1]<self.f_error[-1]:
                self.f_error=np.copy(error)
                self.f_centroids=np.copy(centroids)


    def predict(self,data):

        # Calculate the distances b/w the data points and the final centroids 
        dist=self.__calculate_distance(self.f_centroids,data)
        
        # assign each data point to the nearest centroid
        assign=np.argmin(dist,axis=1) # shape = np. of data points   

        return assign
                
                
                
            
            
        