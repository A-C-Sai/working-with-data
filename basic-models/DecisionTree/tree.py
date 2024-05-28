import numpy as np


class DTreeClassifier:

    def __init__(self, max_depth=None):

        self.max_depth=max_depth 
        self.classes=None # classes present in y_train
        self.x_train=None 
        self.y_train=None 
        self.tree=dict() # tree structure
        '''
            tree 
            ----
            {
                'fid':
                'split_point':
                'gini': **
                'samples': **
                'values': **
                'class': **
                'left_child': value / {'fid': , 'split_point': , ...}
                'right_child': value / {'fid': , 'split_point': , ...}
            }
        '''


    # Calculate Gini Index of a node
    def __gini_index(self, node): 
        '''
            node: contains the id's of the data points present in the node
        '''
        n=node.shape[0] # number of data points in the node
        gini=1.0
        for c in self.classes:
            pcl=(self.y_train[node]==c).sum()
            gini-=(pcl/n)**2
            
        return gini

    # Split a node into left and right children
    # Aim: Find the best split point with highest Information Gain
    def __node_split(self, data_ids):
        '''
            data_ids: contains the id's of the data points present in the node
        '''
        n=data_ids.shape[0]

        # Gini Index of the parent node (before splitting)
        p_gini=self.__gini_index(data_ids)

        # Split the node into all candidates for all features and
        # Find the best feature and the best split point with the
        # highest information gain
        max_ig = -9999999
        for fid in range(self.x_train.shape[1]):

            # feature data to be split
            feature_data = self.x_train[data_ids, fid].copy()

            # remove duplicates of feature_data and sort in ascending order
            unique_feature_data = np.unique(feature_data)

            # list all the candidates, ehich are the midpoints of adjacent data
            candidate_split_points = [np.mean(unique_feature_data[[i,i+1]]) \
                                      for i in range(len(unique_feature_data)-1)]
            
                                      
            '''
               len(candidate_split_points) > 1:
                   Calculate the IG for all candidates, and find the candidate with the largest IG.
               len(candidate_split_points) < 1:
                   Skip the for-loop. feature_data either has only one data point or all have the same value. 
                   No need to split.
            '''

            for c in candidate_split_points:
                #split feature_data into left and right nodes
                left=data_ids[np.where(feature_data<=c)[0]]
                right=data_ids[np.where(feature_data>c)[0]]

                # Calculate Gini Index after splitting
                l_gini=self.__gini_index(left)
                r_gini=self.__gini_index(right)

                # Calculate IG
                ig=p_gini - (l_gini * left.shape[0]/n) - (r_gini * right.shape[0]/n)

                # find where the IG is greatest
                if ig > max_ig:
                    max_ig=ig
                    b_fid=fid # best feature id
                    b_point=c # best split point
                    l_node=left # data ids in left node
                    r_node=right # data ids in right node
                    values=np.bincount(self.y_train[data_ids]) # number of data points belonging to each class
            
        if max_ig > 0.: # split
            return dict([('fid',b_fid),('split_point',b_point),\
                         ('gini',p_gini),('samples',n),('values',list(values)), \
                         ('class',values.argmax()),('left_child',l_node),('right_child',l_node)])
        else:
            return None # No split



    # Create a binary tree using recursion
    def __recursive_split(self, node, curr_depth):
        left=node['left_child']
        right=node['right_child']

        # exit recursion
        if self.max_depth!=None and curr_depth==self.max_depth:
            return

        # recursion
        s=self.__node_split(left)
        if isinstance(s, dict): # split to the left, done.
            node['left_child']=s
            self.__recursive_split(node['left_child'], curr_depth+1)
            

        s=self.__node_split(right)
        if isinstance(s, dict): # split to the right, done.
            node['right_child']=s
            self.__recursive_split(node['right_child'], curr_depth+1)

        

    # Create a tree using training data, and return the result of the tree
    def fit(self, x_train, y_train):
        self.x_train=x_train
        self.y_train=y_train
        self.classes=np.unique(self.y_train)


        # Initially, the root node holds all the data indices.
        root=self.__node_split(np.arange(self.x_train.shape[0]))
        if isinstance(root, dict):
            self.__recursive_split(root, curr_depth=1)


        self.tree=root



    # Estimate the target class of a test data
    def __x_predict(self,tree,x):
        if x[self.tree['fid']] <= self.tree['split_point']:
            if isinstance(self.tree['left_child'], dict): # recursion if not leaf
                return self.x_predict(tree['left_child'], x) # recursion
            else:
                return tree['class']
        else:
            if isinstance(self.tree['right_child'], dict): # recursion if not leaf
                return self.x_predict(tree['right_child'], x) # recursion
            else:
                return tree['class']


    # Estimate the target class of x_test
    def predict(self, x_test):
        tree=self.tree # predictor
        y_pred=[self.x_predict(tree, x) for x in x_test]
        return np.array(y_pred)

    
                
        
        
            
            
        
        
            
        
         
       
        
        