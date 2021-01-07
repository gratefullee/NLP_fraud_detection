# fraud_detection

Dataset: 14,337 of real-world credit card transactions (about 9% of them are fraud cases)

Each transaction has a description about the product/service on 'description' colum as well as other features.

After data cleaning, I used the LDA and LSA topic modeling. Based on the vector values, I put it into a random forest model and tried to predict if it's fraud or not. 

Future work: 1) Use XGBoost to improve the model. 2) Utilize other features as well. 

