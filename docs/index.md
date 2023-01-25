# Welcome to Rome Bridge



Rome Bridge is an adapter between Feature Stores and Data Science Models. A common interface for feading features to machine learning models helps expidite developement, allow interchangability and reduces the risk involved with accidently feending features into models the wrong way. 


## Supported Feature Stores 


|	Product	|	Open Source	|	Link	|
|	------	|	------	|	-------------------------------------	|
|	AWS Sagemaker Feature Store	|	No	|	[link](https://aws.amazon.com/sagemaker/feature-store/)	|
|	Tecton	|	No	|	[link](http://tecton.ai)	|
|	Databrick Feature Store	|	No	|	[link](https://docs.databricks.com/applications/machine-learning/feature-store/index.html)	|
|	Feature Form	|	No	|	[link](https://www.featureform.com/)	|
|	Feast	|	Yes	|	[link](https://feast.dev/)	|
|	Vertex AI	|	No	|	[link](https://cloud.google.com/vertex-ai/docs/featurestore)	|
|	Hopswork	|	Yes	|	[link](https://www.hopsworks.ai/feature-store)	|
|	feathr	|	Yes	|	[link](https://engineering.linkedin.com/blog/2022/open-sourcing-feathr---linkedin-s-feature-store-for-productive-m)	|
|	Rasgo	|	No	|	[link](https://www.rasgoml.com/)	|
|	Butterfree	|	Yes	|	[link](https://github.com/quintoandar/butterfree)	|
|	Bytehub	|	Yes	|	[link](https://docs.bytehub.ai/)	|
|	Kaskada	|	No	|	[link](https://kaskada.com/)	|
|	ScribbleData	|	No	|	[link](https://www.scribbledata.io/product)	|


## Supported Data Science Models

| Model | flavor | Link |
| ------ | -------- | -------------------|
| Rulefit Regressor | sklearn.ensemble.GradientBoostingRegressor  | [Link](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html) |
| ExtraTrees Regressor | sklearn.ensemble.ExtraTreesRegressor | [Link](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html) |
| Random Forest | sklearn.ensemble.RandomForestRegressor | [Link](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) |
| Average Blender | sklearn.linear_model.LogisticRegression | [Link](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) |
| eXtreme Gradient Boosted Trees Regressor | sklearn.ensemble.GradientBoostingRegressor or xgboost | [Link](https://github.com/tqchen/xgboost) [Link](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)
| Light Gradient Boosted Trees Regressor | lightgbm.ESLGBMTR | [Link](https://github.com/Microsoft/LightGBM) |
| Decision Tree Regressor | sklearn.tree.DecisionTreeRegressor | [Link](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html) |
| Support Vector Machines | libsvm | [Link](https://github.com/cjlin1/libsvm) |
| Elastic Net Regressor or Ridge Regressor| lightning's CDRegressor | [Link](https://contrib.scikit-learn.org/lightning/) |
| Auto tune kNN Regressor | sklearn.neighbors.KNeighborsRegressor | [Link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html) |
|  Breiman and Cutler Random Forest Regressor | R | [Link](http://math.furman.edu/~dcs/courses/math47/R/library/randomForest/html/00Index.html) |
| online gradient descent variant | vowpal wabbit Regressor | [Link](https://github.com/VowpalWabbit/vowpal_wabbit/wiki) |
| Neural Network Regressor | TensorFlow | [Link](https://github.com/tensorflow/tensorflow) |
| Generalized Additive Model | LinearGAM | [Link](https://pygam.readthedocs.io/en/latest/) |
| Linear Regression | sklearn.linear_model.LinearRegression |  [Link](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) | 

