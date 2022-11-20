import pandas


# Returns data frame from url.
def load_data_frame(url=''):
    return pandas.read_csv(url)


data_frame_url = 'https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv'
print(load_data_frame(data_frame_url))
