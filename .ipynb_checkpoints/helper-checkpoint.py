def create_encoding(column,subset,dataframe,target):
    """
    Input a feature from a categorical data frame to encode numerically
    """
    column_dict={}
    dummy_df = dataframe[[f'{column}',f'{target}']].groupby([f'{column}'], 
    as_index = False).mean().sort_values(by = f'{target}', ascending = False)
    for i in range(len(dummy_df)):
        column_dict[dummy_df.iloc[i][0]]=(dummy_df.iloc[i][1])
    subset[column] = dataframe[column].map(lambda x: column_dict[x])
    return subset