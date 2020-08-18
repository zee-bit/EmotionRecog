from sklearn.model_selection import train_test_split

# To see number of training data point available for each label
def balance_class(Y):
    num_class = set(Y)
    count_class = {}
    for i in range(len(num_class)):
        count_class[i] = sum([1 for y in Y if y == i])
    return count_class

def give_train_test_splits(X, Y, test_size=0.1, random_state):
    # Split in  training set : validation set :  testing set in 80:10:10
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=random_state)
    y_train = (np.arange(num_class) == y_train[:, None]).astype(np.float32)
    y_test = (np.arange(num_class) == y_test[:, None]).astype(np.float32)
    return X_train, X_test, y_train, y_test

def give_convolution_layer(filters, kernel_size=(3,3), padding='same', use_bn=True, dropout_percentage=None, pool_size=None):
    sequential_model.add(Conv2D(filters, kernel_size, padding='same', activation='relu'))
    if use_bn:
        model.add(BatchNormalization())
    if pool_size is not None: 
        model.add(MaxPooling2D(pool_size=pool_size))
    if dropout_percentage is not None:
        model.add(Dropout(dropout))
    return sequential_model