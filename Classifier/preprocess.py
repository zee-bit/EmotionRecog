from dataset import getData
from utils import balance_class, give_train_test_splits

def preprocess_data(filename='/content/drive/My Drive/fer2013.csv', image_size=(48, 48)):
    X, Y = getData(filename)
    num_class = len(set(Y))

    # balance = balance_class(Y)
    
    N, D = X.shape
    X = X.reshape(N, image_size, 1)

    return give_train_test_splits(X, Y, test_size=0.1, random_state=0), num_class