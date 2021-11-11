import joblib

loaded_model = joblib.load('dib_78.pkl')

print(loaded_model.predict([[10,20,30,40,50,60,70,80]]))
