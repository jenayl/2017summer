#!/usr/bin/python
"""
    Clean away the 10% of points that have the largest
    residual errors (difference between the prediction
    and the actual net worth).

    Return a list of tuples named cleaned_data where
    each tuple is of the form (age, net_worth, error).
"""

def outlierCleaner(predictions, ages, net_worths):
    # predictions = reg.predict(ages_train)
    cleaned_data = []

    errors = (net_worths - predictions)**2
    cleaned_data = zip(ages, net_worths, errors) # zip( )
    cleaned_data = sorted(cleaned_data, key=lambda x:x[2][0], reverse=True)
    #sorted(); sorting method
    ## parameter key ==> what to sort by?
    ## key = lambda x: x[2][0] ==> for each element x, sort by x[2][0]
    limit = int(len(net_worths)*0.1)
    return cleaned_data[limit:]

