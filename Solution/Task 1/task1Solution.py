import dataFrameLoader as dfLoader

data_frame_url = 'https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv'
data_frame = dfLoader.load_data_frame(data_frame_url)

print(data_frame)
