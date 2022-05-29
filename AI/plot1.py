from turtle import color, fillcolor, title
from unicodedata import name
from matplotlib import colorbar, markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import col, line
import seaborn as sns
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.express as px
import cufflinks
cufflinks.go_offline()
#cufflinks.set_config_file(world_readable=True, theme='pearl')
import plotly
import chart_studio.plotly as py
from plotly import tools

#pd.set_option('display.max_columns', 100)
data = pd.read_csv('train.csv')


def dataframe(filename):
    df = pd.read_csv(filename)
    df.drop('Id',axis=1,inplace=True)
    return df

#statistical summary for numeric data
def numeric(df):
    tab = ff.create_table(df.describe().T,index=True,index_title="Numeric Columns")
    iplot(tab)

#statistical summary for categorical or string
def categorical(df):
    tab = ff.create_table(df.describe(['O'].T),index=True,index_title="Categorical Columns")
    iplot(tab)

#histogram
def histogram(df,col):
    f = px.histogram(df,x=col,y="",title="Histogram of {0}".format(col),nbins=100,opacity=0.5,labels={col:"Sales","":"HI"})
    f.update_traces(marker_line_width = 1, marker_line_color="black")
    f.show()

#boxplot
def boxplot(df,col):
    f=px.box(df,y=col,title="Boxplot of {0}".format(col),labels={col:" "})
    f.show()

#Boxplot and histogram of house sale price grouped by with or with no air conditioning
def groupBox(df,col):
    if col=="CentralAir":
        g1 = go.Box(y=df.loc[df[col]=='Y']['SalePrice'],name="With {0}".format(col),marker=dict(color = 'rgb(214, 12, 140)'))
        g2 = go.Box(y=df.loc[df[col]=='N']['SalePrice'],name="With no {0}".format(col),marker=dict(color='blue'))
        d = [g1,g2]
        layout = go.Layout(title="Boxplot of Sale Price by {0}".format(col))
    elif col=="GarageCars":
        g0 = go.Box(y=df.loc[df[col]==0]['SalePrice'],name="No {0}".format(col),marker=dict(color = 'red'))
        g1 = go.Box(y=df.loc[df[col]==1]['SalePrice'],name="With 1 {0}".format(col),marker=dict(color = 'blue'))
        g2 = go.Box(y=df.loc[df[col]==2]['SalePrice'],name="With 2 {0}".format(col),marker=dict(color = 'yellow'))
        g3 = go.Box(y=df.loc[df[col]==3]['SalePrice'],name="With 3 {0}".format(col),marker=dict(color = 'green'))
        g4 = go.Box(y=df.loc[df[col]==4]['SalePrice'],name="With 4 {0}".format(col),marker=dict(color = 'orange'))
        d=[g0,g1,g2,g3,g4]
        layout = go.Layout(title="Boxplot of Sale Price by {0}".format(col))
    fig = go.Figure(data=d,layout=layout)
    fig.show()

def groupHis(df,col):
    if col=="CentralAir":
        g1 = go.Histogram(x=df.loc[df[col]=='Y']['SalePrice'],name="With {0}".format(col),marker=dict(color = 'red'),opacity=1)
        g2 = go.Histogram(x=df.loc[df[col]=='N']['SalePrice'],name="With no {0}".format(col),marker=dict(color='blue'),opacity=0.7)
        d = [g1,g2]
        layout = go.Layout(title="Boxplot of Sale Price by {0}".format(col),barmode='overlay')
    elif col=="GarageCars":
        g0 = go.Histogram(x=df.loc[df[col]==0]['SalePrice'],name="No {0}".format(col),marker=dict(color = 'red'),opacity=0.5)
        g1 = go.Histogram(x=df.loc[df[col]==1]['SalePrice'],name="With 1 {0}".format(col),marker=dict(color = 'blue'),opacity=0.5)
        g2 = go.Histogram(x=df.loc[df[col]==2]['SalePrice'],name="With 2 {0}".format(col),marker=dict(color = 'yellow'),opacity=0.5)
        g3 = go.Histogram(x=df.loc[df[col]==3]['SalePrice'],name="With 3 {0}".format(col),marker=dict(color = 'green'),opacity=0.5)
        g4 = go.Histogram(x=df.loc[df[col]==4]['SalePrice'],name="With 4 {0}".format(col),marker=dict(color = 'orange'),opacity=0.5)
        d=[g0,g1,g2,g3,g4]
        layout = go.Layout(title="Boxplot of Sale Price by {0}".format(col),barmode='overlay')
    fig = go.Figure(data=d,layout=layout)
    fig.update_traces(marker_line_width = 1, marker_line_color="black")
    fig.show()

#frequency Table
def frequency(df,col):
    a=df[col].value_counts()
    print(a/a.sum())

#Numeric Summaries
def Nsummaries(df,col):
    print(df[col].describe())

#scatterplot
def scatter(df,x,y):
    f = px.scatter(df,x=x,y=y,title="Scatterplot of {0} vs {1}".format(x,y),color_discrete_sequence=['darkred'])
    f.show()