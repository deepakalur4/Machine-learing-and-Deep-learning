import bentoml


classifier=bentoml.sklearn.get("iris_clf:latest").to_runner()
classifier.init_local()
print(classifier.predict.run([[5.9,3.0,5.1,1.8]]))