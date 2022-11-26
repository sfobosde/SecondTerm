import pandas


# Returns data frame from url.
def load_data_frame(url=''):
    return pandas.read_csv(url)