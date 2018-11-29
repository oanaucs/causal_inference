import numpy as np

def load_model(index, n_obs=10000):

    if index == 1:
        X = np.random.randn(n_obs, 4)
        X[:,2] += X[:,1]
        X[:,3] += X[:,2]

        true = np.zeros((4, 4), dtype='int')
        true[1,2] = 1
        true[2,3] = 1
        return X, true

    if index == 2:
        X = np.random.randn(n_obs, 4)
        X[:,1] += X[:,2]
        X[:,3] += X[:,2]

        true = np.zeros((4, 4), dtype='int')
        true[2,1] = 1
        true[2,3] = 1
        return X, true

    if index == 3:
        X = np.random.randn(n_obs, 4)
        X[:,2] += X[:,1] + X[:,3]

        true = np.zeros((4, 4), dtype='int')
        true[1,2] = 1
        true[3,2] = 1
        return X, true

    if index == 4:
        X = np.random.randn(n_obs, 4)
        X[:,1] += X[:,0]
        X[:,2] += X[:,0]
        X[:,3] += X[:,1] + X[:,2] 

        true = np.zeros((4, 4), dtype='int')
        true[0,1] = 1
        true[0,2] = 1
        true[1,3] = 1
        true[2,3] = 1

        return X, true

    if index == 5:
        X = np.random.randn(n_obs, 4)
        X[:,3] += X[:,1] + X[:,2]
        X[:,0] += X[:,1] + X[:,2] 

        true = np.zeros((4, 4), dtype='int')
        true[1,3] = 1
        true[1,0] = 1
        true[2,3] = 1
        true[2,0] = 1

        return X, true

    if index == 6:
        X = np.random.randn(n_obs, 5)
        X[:,4] += X[:,2] + X[:,3]
        X[:,1] += X[:,2] + X[:,3] 
        X[:,0] += X[:,1] + X[:,4] 
        
        true = np.zeros((5, 5), dtype='int')
        true[3,4] = 1
        true[2,4] = 1
        true[2,1] = 1
        true[3,1] = 1
        true[1,0] = 1
        true[4,0] = 1

        return X, true


    if index == 7:
        X = np.random.randn(n_obs, 4)
        X[:,1] += X[:,0]
        X[:,3] += X[:,0]
        X[:,2] += 0.5*X[:,0] + 0.5*X[:,1] + 0.5*X[:,3] 

        true = np.zeros((4, 4), dtype='int')
        true[0,1] = 1
        true[0,2] = 1
        true[0,3] = 1
        true[3,2] = 1
        true[1,2] = 1

        return X, true

    if index == 8:
        X = np.random.randn(n_obs, 5)
        X[:,4] += 0.5*X[:,2] + 0.4*X[:,3]
        X[:,1] += 0.5*X[:,2] + 0.4*X[:,3] 
        X[:,0] += 0.5*X[:,1] + 0.6*X[:,4] 
        X[:,3] += 2.*X[:,2] #+ X[:,4] 

        true = np.zeros((5, 5), dtype='int')
        true[3,4] = 1
        true[2,4] = 1
        true[2,1] = 1
        true[3,1] = 1
        true[1,0] = 1
        true[4,0] = 1
        true[2,3] = 1

        return X, true

    if index == 9:
        X = np.random.randn(n_obs, 15)
        X[:,4] += 0.5*X[:,2] + 0.4*X[:,3]
        X[:,1] += 0.5*X[:,2] + 0.4*X[:,3] 
        X[:,0] += 0.5*X[:,1] + 0.6*X[:,4] 

        true = np.zeros((15, 15), dtype='int')
        true[3,4] = 1
        true[2,4] = 1
        true[2,1] = 1
        true[3,1] = 1
        true[1,0] = 1
        true[4,0] = 1

        return X, true

def get_adj(graph):
    N = len(graph)
    return dict([(j, list(np.where(graph[:,j] != 0)[0])) for j in range(N)])