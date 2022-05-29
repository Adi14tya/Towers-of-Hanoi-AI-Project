from plot1 import *

data = dataframe("train.csv")
#numeric(data)
#histogram(data,'SalePrice')
#boxplot(data,'SalePrice')
#groupHis(data,"GarageCars")
#frequency(data,"OverallQual")
scatter(data,"GrLivArea","SalePrice")

