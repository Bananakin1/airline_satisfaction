from sklearn.metrics import balanced_accuracy_score, f1_score
import time

def test_classifiers(train_data, train_classes, test_data, test_classes, classifiers):
    """
    test_classifiers function:
    
    Fits the data split into a train and test subsets for everyone of the classifiers chosen
    and provides metrics like accuracy and f1 score for each one of them. 

    Useful to obtain the performance of different models over the same data.
    """
    res = {}

    for clf in classifiers:
        name = clf.__class__.__name__

        print("Now training {}...".format(name))

        start_time = time.time()
        clf.fit(train_data, train_classes)
        
        acc = round(balanced_accuracy_score(test_classes, clf.predict(test_data)), 3)
        f1 = round(f1_score(y_true=test_classes, y_pred = clf.predict(test_data), average='weighted'), 3)

        stop_time = time.time()

        time_to_run = round(stop_time - start_time,3)

        print("{} trained in {} with an F1 of : {} and an accuracy of: {}".format(name, time_to_run, f1, acc))

        res[name] = (acc, f1, time_to_run)

    return res