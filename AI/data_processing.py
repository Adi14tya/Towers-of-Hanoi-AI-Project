import pandas as pd
import numpy as np
from datetime import datetime
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf

warnings.filterwarnings("ignore")

#reading data
def dataframe(filename):
    return pd.read_csv(filename)

# Converting column type into Date Type
def convert_dtype(df):
    df['Date'] = pd.to_datetime(df['Date'])

# Finding the number of unique values in particular column
def unique_val(df):
    print(len(df.unique()))


# Creating new columns named "Day", "Month" and "Year" from "Date" column
def createDMY(df):
    df["Day"]=df["Date"].dt.day
    df["Month"]=df["Date"].dt.month
    df["Year"]=df["Date"].dt.year


Mon_li=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# Function to get Sales("Volume") in a specific period
def Sales_On_Particular_Period(df,col1,col2):
    convert_dtype(df)
    createDMY(df)
    print(df.groupby([col1])[[col2]].sum().reset_index())


# Function to get sales on particular month and a year
def Monthly_Sales_MY(df,mon,year):
    convert_dtype(df)
    createDMY(df)
    total=0
    df1=df[(df["Month"]==mon)&(df["Year"]==year)]
    total=df1["Volume"].sum()
    print("The total sales on",Mon_li[mon-1],"in the year",year,"is",total)

# Function to get on a particular month of all years
def Monthly_Sales_M(df,mon):
    convert_dtype(df)
    createDMY(df)
    total=0
    df1=df[(df["Month"]==mon)]
    total=df1["Volume"].sum()
    print("The total sales on",Mon_li[mon-1],"is",total)

# Function to get sales on a particular year
def Yearly_Sales(df,year):
    convert_dtype(df)
    createDMY(df)
    total=0
    df1=df[df["Year"]==year]
    total=df1["Volume"].sum()
    print("The total sales on in the year",year,"is",total)

# Function to get sales on a particular date
def Day_Sales_Date(df,day,mon,year):
    convert_dtype(df)
    createDMY(df)
    total=0
    df1=df[(df["Day"]==day)&(df["Month"]==mon)&(df["Year"]==year)]
    total=df1["Volume"].sum()
    print("The total sales on "+str(day)+"-"+str(Mon_li[mon-1])+"-"+str(year)+" is "+str(total))

# Function to get sales on a particular day
def Day_Sales_day(df,day):
    convert_dtype(df)
    createDMY(df)
    total=0
    df1=df[df["Day"]==day]
    total=df1["Volume"].sum()
    print("The total sales on tha date",day,"is",total)

# Getting the datatype of each column of dataframe
def get_dtypes(df):
    print(df.dtypes)

# Getting the Dimensions of the dataframe
def get_dimen(df):
    convert_dtype(df)
    createDMY(df)
    df.shape
    print("Dataset has {} records and {} columns".format(df.shape[0], df.shape[1]))

# Changing the index of Dataframe to the Date column with set_index() method
def change_idx(df):
    convert_dtype(df)
    createDMY(df)
    return df.set_index("Date")

# Function to add some noise to the data
def random_noise(df):
    return np.random.normal(scale=1.6,size=(len(df)))

# Function for lag features
def lag_features(df, lags,col1,col2,col3):
    for lag in lags:
        df['Vol_lag_' + str(lag)] = df.groupby([col1,col2])[col3].transform(lambda x: x.shift(lag))+ random_noise(df)
    return df

# Function for roll mean features
def roll_mean_features(df,windows,col1,col2,col3):
    for window in windows:
        df['Vol_roll_mean_' + str(window)] = df.groupby([col1,col2])[col3].transform(lambda x: x.shift(1).rolling(window=window, min_periods=10, win_type="triang").mean()) + random_noise(df)
    return df

# Function for ewm features(Exponentially weighted moving averages)
def ewm_features(df,alphas,lags,col1,col2,col3):
    for alpha in alphas:
        for lag in lags:
            df['Volume_ewm_alpha_'+str(alpha).replace(".", "")+"_lag_" + str(lag)] = df.groupby([col1,col2])[col3].transform(lambda x: x.shift(lag).ewm(alpha=alpha).mean())
    return df






