import csv
import pandas as pd
import dash as ds

df =pd.read_csv('daily_sales_data_0.csv', header= 0)
df1 =pd.read_csv('daily_sales_data_1.csv', header =0)
df2 =pd.read_csv('daily_sales_data_2.csv', header =0)


def sales(df, df1, df2):
    for dataframe in [df, df1, df2]:
        dataframe['price']= dataframe['price'].replace({r"\$": '', r"," :""}, regex = True).astype(float)
        dataframe['sales'] = dataframe['price'] * dataframe['quantity']
    combined_df =pd.concat([df, df1, df2], ignore_index = True)
    
    pink_morsel_df =combined_df[combined_df['product'].str.strip().str.lower() == "pink morsel"]
    
    formatted_df = pink_morsel_df[['sales', 'date', 'region']]
    
    formatted_df.to_csv('pink_morsel_sales.csv', index=False)
    
    return pink_morsel_df[['sales', 'date', 'region']]


    

print(sales(df, df1, df2))







