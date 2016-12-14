from random import randint

class NetworkMock(object):
   def fit(self, X, y):
       pass

   def predict(self, X):
       return [randint(0,1)]