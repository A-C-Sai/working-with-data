import numpy as np

class KNNClassifier:
    def __init__(self,*,K=None,weights='uniform'):
        """
        Parameters
        ----------
        K : Number of neighbors to judge class of queries
        weights: {'uniform','distance'} performs vanilla or weighted KNN depend on parameter value

        Returns
        -------
        None
        """
        
        self.K = K 
        self.weights = weights

    def __calculate_distance(self,X_train,X_test):
        
        """
        Parameters
        ----------
        X_train : NxM matrix
        X_test : PxM matrix
    
        Returns
        -------
        d_matrix : Distance matrix containing distance of each point P_i 
        in X_test with each point N_i in X_train.
        
        [[P1_N1 P1_N2 P1_N3 ... P1_Nn]
         [P2_N1 P2_N2 P2_N3 ... P2_Nn]
         [P3_N1 P3_N2 P3_N3 ... P3_Nn]
                     .
                     .
         [Pn_N1 Pn_N2 Pn_N3 ... Pn_Nn]]
    
        """
                                                                   #  (d0,d1,d2)
        train_data = X_train[np.newaxis,:] # expand d0 axis (N, M) -> (1, N, M)
        
                                                                  # (d0,d1,d2)
        test_data = X_test[:,np.newaxis] # expand d1 axis (P, M) -> (P, 1, M)
        
        d_matrix = np.sqrt(np.sum(np.square(train_data - test_data),axis=2)) # PxN matrix
        
        return d_matrix


    def predict(self,X_train,X_test,y_train):

        """
        Parameters
        ----------
        X_train : NxM matrix
        X_test : PxM matrix
        y_train : Nx1 matrix 
        
        Returns
        -------
        y_pred : predicted class of each test query
    
        """
        if self.K == None:
            self.K = int(np.sqrt(X_train.shape[0]))
        
        self.classes = np.unique(y_train)
        
        # Calculate distance between test and train datapoints
        distance_matrix = self.__calculate_distance(X_train, X_test)
        distance_matrix += 1e-8 # Prevents distance from becoming zero
        
        # Find "K" nearest neighbors
        nearest_neighbors = np.argsort(distance_matrix,axis=1)[:, :self.K]
        
        # Find class of "K" nearest neighbors
        class_nearest_neighbors = y_train[nearest_neighbors]

        if self.weights == 'uniform':
            # Majority Voting
            y_pred = np.array([np.bincount(neighbors).argmax() for neighbors in class_nearest_neighbors])
        else:
            # inverse weighted distance
            w_dist = np.sort(distance_matrix,axis=1)[:, :self.K]
            w_inv = 1.0 / w_dist

            # Estimate the class of test data using inverse weight
            y_pred = []
            for i, weights in enumerate(w_inv):
                sum_of_weights = weights.sum()
                iw_distance = np.array([ weights[class_nearest_neighbors[i]==c].sum()/sum_of_weights for c in self.classes ])
                y_pred.append(self.classes[iw_distance.argmax()])
        
        
        return y_pred


class KNNRegressor:
    def __init__(self,*,K=20,weights='uniform'):
        """
        Parameters
        ----------
        K : Number of neighbors to judge class of queries
        weights: {'uniform','distance'} performs vanilla or weighted KNN depend on parameter value

        Returns
        -------
        None
        """
        
        self.K = K 
        self.weights = weights

    def __calculate_distance(self,X_train,X_test):
        
        """
        Parameters
        ----------
        X_train : NxM matrix
        X_test : PxM matrix
    
        Returns
        -------
        d_matrix : Distance matrix containing distance of each point P_i 
        in X_test with each point N_i in X_train.
        
        [[P1_N1 P1_N2 P1_N3 ... P1_Nn]
         [P2_N1 P2_N2 P2_N3 ... P2_Nn]
         [P3_N1 P3_N2 P3_N3 ... P3_Nn]
                     .
                     .
         [Pn_N1 Pn_N2 Pn_N3 ... Pn_Nn]]
    
        """
                                                                   #  (d0,d1,d2)
        train_data = X_train[np.newaxis,:] # expand d0 axis (N, M) -> (1, N, M)
        
                                                                  # (d0,d1,d2)
        test_data = X_test[:,np.newaxis] # expand d1 axis (P, M) -> (P, 1, M)
        
        d_matrix = np.sqrt(np.sum(np.square(train_data - test_data),axis=2)) # PxN matrix
        
        return d_matrix


    def predict(self,X_train,X_test,y_train):

        """
        Parameters
        ----------
        X_train : NxM matrix
        X_test : PxM matrix
        y_train : Nx1 matrix 
        
        Returns
        -------
        y_pred : predicted value of each test query
    
        """

        
        # Calculate distance between test and train datapoints
        distance_matrix = self.__calculate_distance(X_train, X_test)
        distance_matrix += 1e-8 # Prevents distance from becoming zero
        
        # Find "K" nearest neighbors
        nearest_neighbors = np.argsort(distance_matrix,axis=1)[:, :self.K]
        
        # Find value of "K" nearest neighbors
        nearest_neighbors_value = y_train[nearest_neighbors]

        if self.weights == 'uniform':
            # Average
            y_pred = np.mean(nearest_neighbors_value, axis=1)
        else:
            # inverse weighted distance
            w_dist = np.sort(distance_matrix,axis=1)[:, :self.K]
            w_inv = 1.0 / w_dist

            # Estimate value of test data using inverse weight
            y_pred = []
            for i, weights in enumerate(w_inv):
                sum_of_weights = weights.sum()
                y_pred.append(np.sum(weights*nearest_neighbors_value[i])/sum_of_weights)
        
        
        return np.array(y_pred)