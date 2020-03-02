import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def distribution(df,variable,name_of_variable):
    explode1=[]
    explode1.append(0)
    for i in range(df[variable].nunique()-1):
        explode1.append(0.05)
    sns.set()
    f,ax=plt.subplots(1,2,figsize=(18,8))
    df[variable].value_counts().plot.pie(explode=explode1,autopct='%1.1f%%',ax=ax[0],shadow=True)
    ax[0].set_title('Rate of Heart Disease by ' + name_of_variable)
    ax[0].set_ylabel('Count')
    sns.countplot(variable,data=df,ax=ax[1],order=df[variable].value_counts().index)
    ax[1].set_title('Rate of Heart Disease by '+ name_of_variable)
    plt.show()

def ratio(df,variable,main_variable,name_of_variable):
    Gender = pd.crosstab(df[variable],df[main_variable])
    Gender.div(Gender.sum(1).astype(float), axis = 0).plot(kind="bar", stacked=True, figsize=(4,4)).legend(loc=4)
    plt.xlabel(name_of_variable)
    p = plt.ylabel('Percentage')
    print(pd.crosstab(df[variable],df[main_variable], normalize='index'))

def huge_ratio(df,variable,main_variable,name_of_variable):
    Gender = pd.crosstab(df[variable],df[main_variable])
    Gender.div(Gender.sum(1).astype(float), axis = 0).plot(kind="bar", stacked=True, figsize=(8,8)).legend(loc=4)
    plt.xlabel(name_of_variable)
    p = plt.ylabel('Percentage')
    print(pd.crosstab(df[variable],df[main_variable], normalize='index'))