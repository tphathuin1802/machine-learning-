import pandas as pd
import pickle

from pandas import Index

modelname="C:/Coding/Projects/DataProjects/MachineLearningProjects/HousePricePrediction/housingmodel.zip"

# Load Trained Machine Learning Model
trainedmodel=pickle.load(open(modelname, 'rb'))

features=Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population'],
      dtype='object')
# Check coeff again if you want (no need)
coeff_df = pd.DataFrame(trainedmodel.coef_,features,columns=['Coefficient'])
print(coeff_df)

print("Input 1:")
input1=[66774.995817,5.717143,7.795215,4.320000,36788.980327]
print(input1)
prediction1=trainedmodel.predict([input1])
print("Housing Price Prediction 1=",prediction1)

print("-"*50)
input2=[[66774.995817,5.717143,7.795215,4.320000,36788.980327],
        [80527.47208,8.093512681,5.0427468,4.1,47224.35984]]
print(input2)
prediction2=trainedmodel.predict(input2)
print("Housing Price Prediction 2=",prediction2)