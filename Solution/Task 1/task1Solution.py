import dataFrameLoader as dfLoader


# Show dataframe as table.
def print_dataframe(data_frame_url):
    data_frame = dfLoader.load_data_frame(data_frame_url)

    print(data_frame)


print_dataframe('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv')



