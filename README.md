# fraud_detection

Dataset: real world 14,337 cases of credit card usage information (about 9% is fraud cases)

Each transaction has a description about the product/service on 'description' colum.

After data cleaning, I used the LDA and LSA topic modeling. Based on the vector values, I put it into a random forest model and tried to predict if it's fraud or not. 

Future work: Use XGBoost to improve the model and utilize other features as well. 

