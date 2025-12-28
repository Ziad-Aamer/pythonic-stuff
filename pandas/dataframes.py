import pandas as pd

def init_dataframe():
    data = {
        'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C'],
        'Column3': [4.5, 5.5, 6.5]
    }

    return pd.DataFrame(data)


def test_loc_iloc(df: pd.DataFrame):
    # df.loc[Rows, Columns] ; iloc uses only index values
    # get rows with index 1
    result = df.loc[1]
    print('result: ', result)

    print('--------------------')

    # get row with index 1 to 2, and only show the second column. Full slicing is enabled
    result = df.loc[1:2, 'Column2']
    print('result: ', result)



if __name__  == '__main__':
    df = init_dataframe()
    test_loc_iloc(df)