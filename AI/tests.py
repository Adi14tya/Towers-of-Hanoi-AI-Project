from data_processing import *

def adf_test(df):
    print ('Results of Dickey-Fuller Test:')
    dftest=adfuller(df, autolag='AIC')
    dfoutput=pd.Series(dftest[0:4],index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

def kpss_test(df):
    print('Results of KPSS Test:')
    kpsstest=kpss(df, regression='c', nlags="auto")
    kpss_output=pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','#Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print(kpss_output)