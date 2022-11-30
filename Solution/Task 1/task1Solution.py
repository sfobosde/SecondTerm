import dataFrameLoader as dfLoader


# Show dataframe as table.
data_frame_url = 'https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv'
data_frame = dfLoader.load_data_frame(data_frame_url)
print(data_frame)
print(data_frame.Fare.dtype)
print(data_frame.dtypes)

for name, value in data_frame.items():
    print(f'{name}:', len(data_frame.index[data_frame[name] != 0].tolist()))



