import pandas as pd

data = pd.read_csv("SalaryData.csv")

x = data['YearsExperience'].values
x = x.reshape(-1,1)

y = data['Salary']

from sklearn.linear_model import LinearRegression 
mind = LinearRegression()
model = mind.fit(x,y)
print(""" 
         Future Baba Welcomes you to the World of Prediction
         ---------------------------------------------------

         Agar apko bahar jana hai toh -1 dabaye
        
        
        """)

while(True):
    exp = input("Enter Your Years of Experirncr in ML Field: ")
    exp = float(exp)
    if exp < 0 :
        exit()
    prediction = model.predict([[exp]])
    print("\nBaccha tuje ", prediction , "Salary milegi..\n")
