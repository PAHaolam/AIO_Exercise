import numpy as np


def create_train_data():
    train_data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
                  ['Sunny', 'Hot', 'High', 'Strong', 'no'],
                  ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
                  ['Rain', 'Mild,', 'High', 'Weak', 'yes'],
                  ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
                  ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
                  ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
                  ['Overcast', 'Mild', 'High', 'Weak', 'no'],
                  ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
                  ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(train_data)


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.array(
        [(train_data[:, 4] == y).mean() for y in y_unique])
    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []
    for i in range(train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        conditional_probability.append(
            np.array([[(train_data[train_data[:, -1] == y, i] == x).mean() for x in x_unique] for y in y_unique]))
    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    p0 = 0
    p1 = 0

    p0 = np.prod([conditional_probability[i][0, get_index_from_value(
        X[i], list_x_name[i])] for i in range(len(X))])*prior_probability[0]
    p1 = np.prod([conditional_probability[i][1, get_index_from_value(
        X[i], list_x_name[i])] for i in range(len(X))])*prior_probability[1]

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
