import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")
dataset = pd.concat([train.drop(["SalePrice"], axis=1), test])
dataset = pd.DataFrame(dataset)
d = pd.DataFrame(dataset.isnull().sum())
print("Total no. of rows: 2919 \nCount of missing values: \n")
for i in range(len(d)):
    if d.iloc[i,0]>5:
        print(d.index[i], " ", d.iloc[i,0])
#MSZoning
dataset["MSZoning"].fillna("RL", inplace=True)
#Utilities
dataset["Utilities"].fillna(dataset["Utilities"].mode, inplace=True)
#Exterior1st and Exterior2nd
dataset["Exterior1st"].fillna(dataset["Exterior1st"].mode, inplace=True)
dataset["Exterior2nd"].fillna(dataset["Exterior2nd"].mode, inplace=True)
#Electrical
dataset["Electrical"].fillna(dataset["Electrical"].mode, inplace=True)
#BsmtFullBath and BsmtHalfBath
dataset["BsmtFullBath"].fillna(dataset["BsmtFullBath"].mode, inplace=True)
dataset["BsmtHalfBath"].fillna(dataset["BsmtHalfBath"].mode, inplace=True)
#KitchenQual
dataset["KitchenQual"].fillna(dataset["KitchenQual"].mode, inplace=True)
#Functional
dataset["Functional"].fillna(dataset["Functional"].mode, inplace=True)
#GarageCars
dataset["GarageCars"].fillna(dataset["GarageCars"].mode, inplace=True)
#SaleType
dataset["SaleType"].fillna(dataset["SaleType"].mode, inplace=True)
#BsmtUnfSF and TotalBsmtSF
dataset["BsmtUnfSF"].fillna(dataset["BsmtUnfSF"].mean(),inplace=True)
dataset["TotalBsmtSF"].fillna(dataset["TotalBsmtSF"].mean(),inplace=True)

#BsmtFinSF1 and BsmtFinSF2
dataset["BsmtFinSF1"].fillna(0, inplace=True)
dataset["BsmtFinSF2"].fillna(0, inplace=True)
#GarageArea
dataset["GarageArea"].fillna(419.49, inplace=True) #replacing it with the mean of detached garage area
#MasVnrType
dataset.MasVnrType.fillna("None", inplace=True)
#MasVnrArea
dataset.MasVnrArea.fillna(0, inplace=True)
#BsmtQual
dataset.BsmtQual.fillna("NA", inplace=True)
#BsmtCond
dataset.BsmtCond.fillna("NA", inplace=True)

# For the properties without basement, we will set the value to no basement, and for others, to no exposure
#BsmtExposure
dataset.BsmtExposure.fillna(dataset.BsmtUnfSF, inplace=True)
dataset.BsmtExposure.replace({0.0:"NA",936.0:"No", 1595.0:"No", 560.7721041809458:"No", 725.0:"No" }, inplace=True)

#BsmtFinType1
dataset.BsmtFinType1.loc[660]=dataset.BsmtFinType1.mode()
dataset.BsmtFinType1.fillna("NA",inplace=True)

#BsmtFinType2
dataset.BsmtFinType2.loc[332]=dataset.BsmtFinType2.mode()
dataset.BsmtFinType2.fillna("NA",inplace=True)

#GarageType
dataset.GarageType.fillna("NA", inplace=True)

#2127,2577 - Garages' Id present
#Garages can be expected to be built around the same time other garages were built in the same neighbourhood
#dataset[["Neighborhood","GarageType"]].iloc[[2127,2577]]

dataset[((dataset.Neighborhood=="OldTown") | (dataset.Neighborhood== "IDOTRR")) & (dataset.GarageType== "Detchd")]

#GarageYrBlt
dataset.GarageYrBlt.loc[2127] = 1950
dataset.GarageYrBlt.loc[2577] = 1946
dataset.GarageYrBlt.fillna(0, inplace=True)

#GarageFinish
dataset.GarageFinish.loc[2127] = "Unf"
dataset.GarageFinish.loc[2577] = "Unf"
dataset.GarageFinish.fillna("NA", inplace=True)

#GarageQual
dataset.GarageQual.loc[2127] = "TA"
dataset.GarageQual.loc[2577] = "TA"
dataset.GarageQual.fillna("NA", inplace=True)

#GarageCond
dataset.GarageCond.loc[2127] = "TA"
dataset.GarageCond.loc[2577] = "TA"
dataset.GarageCond.fillna("NA", inplace=True)

#LotFrontage
dataset.LotFrontage.fillna(0,inplace=True)

#FireplaceQu
dataset.FireplaceQu.fillna("NA",inplace=True)

#PoolQC
dataset.PoolQC.fillna("NA",inplace=True)

#Fence
dataset.Fence.fillna("NA",inplace=True)

#Alley
dataset.Alley.fillna("NA",inplace=True)

#MiscFeature
dataset.MiscFeature.fillna("NA",inplace=True)
d=pd.DataFrame(dataset.isnull().sum())

print("Total no. of rows: 2919 \nCount of missing values: \n")

for i in range(len(d)):
    if d.iloc[i,0]>0:
        print(d.index[i], " ", d.iloc[i,0])









