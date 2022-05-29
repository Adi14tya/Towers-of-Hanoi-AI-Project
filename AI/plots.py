from data_processing import *

# Ploting a plot for sales
def plot(df,col):
    convert_dtype(df)
    createDMY(df)
    change_idx(df)
    plt.figure(figsize=(16,5))        
    plt.plot(df.index,col,label ="Sales")
    plt.legend(loc='best')
    plt.show()

# Auto-correlation function plot
def acf_plot(col):
    plot_acf(col)
    plt.show()