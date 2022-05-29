from data_processing import *
from tests import *
from plots import *

data = dataframe("FOE.csv")

Sales_On_Particular_Period(data,"Year","Volume")

Sales_On_Particular_Period(data,"Month","Volume")

Sales_On_Particular_Period(data,"Day","Volume")

# Function to get sales on particular month and a year
Monthly_Sales_MY(data,3,1980)

# Function to get on a particular month of all years
Monthly_Sales_M(data,3)

# Function to get sales on a particular year
Yearly_Sales(data,1980)

# Function to get sales on a particular date
Day_Sales_Date(data,17,3,1980)

# Function to get sales on a particular day
Day_Sales_day(data,17)

# Getting the Dimensions of the dataframe
#get_dimen(data)

plot(data,data['Volume'])

adf_test(data["Volume"])

kpss_test(data["Volume"])

# Auto-correlation function plot
#acf_plot(data['Volume'])

# Function to add some noise to the data
random_df = random_noise(data)
print(random_df[0:5])

# Function for lag features
df = lag_features(data, [30, 91, 98, 105, 112, 119, 126, 182, 273, 364, 546, 728, 912, 1095],"High","Low","Volume")
print(df.head(31))

# Function for roll mean features
df =roll_mean_features(data,[91, 182, 273, 365, 546, 728],"High","Low","Volume")
print(df.head())

# Function for ewm features(Exponentially weighted moving averages)
alphas = [0.99, 0.95, 0.9, 0.85, 0.8, 0.7, 0.6, 0.5]
lags = [30, 91, 98, 105, 112, 119, 126, 182, 273, 364, 546, 728, 912, 1095]
df = ewm_features(data, alphas,lags,"High","Low","Volume")
print(df.head(50))

