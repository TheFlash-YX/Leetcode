import numpy as np

def predict(train_data,test_data):
    train_arr=np.array(train_data,dtype=float)
    test_arr=np.array(test_data,dtype=float)

    train_x=train_arr[:,:-1]
    train_y=train_arr[:,-1]

    num_train=train_x.shape[0]
    num_test=test_arr.shape[0]


