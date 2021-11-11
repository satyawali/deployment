import pickle

loaded_model = pickle.load(open('dib_78.pkl', 'rb'))
 
print(loaded_model.predict([[10,20,30,40,50,60,70,80]]))
