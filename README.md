![pedro-lastra-Nyvq2juw4_o-unsplash (1)](https://user-images.githubusercontent.com/75818628/129616561-9e4b9e88-1bce-499f-89b1-88dc448d0dcc.jpg)
# Chicago Traffic Accidents  
Classification Models  
<br>**Project Partners: Jojo de Leon and Harrison Gu**

## Project objective: 
Our aim is to investigate the factors of reported accidents in the city of Chicago to ascertain which features are more likely to lead to an accident that involves injury in order to aid the city of Chicago in allocating their limited ambulatory services.

## Data
Our Chicago Traffic Accidents datasets came from the city of Chicago’s data portal. We combined two datasets, one that was referenced by the vehicle while the other regarded the person(s) involved in the accident. The information contained is derived from all reported accidents from 2015 to present day. 

https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3  
https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d  

## Methodology  
1. The Crash Record ID, which was present in both datasets, was used to combine the two datasets. Initially, there were over 1.6 million accidents with 79 features for each accident to explore. We chose to concentrate on accidents in which at least one vehicle was a car.  As such, records pertaining to cyclists and pedestrians were eliminated. Furthermore, for the features we identified as relevant, any unknown or missing entry for a relevant feature within a record disqualified that record for use. Our models are based on 17 features of roughly 162 thousand accident records. 
2. In order to establish the two best models to use for our data, we ran baseline, aka vanilla, models of the following types: Logistic Regression, K-Nearest Neighbors, Decision Tree, Bagged Tree, Random Forest, Ada Boost, Gradient Boost, and XGBoost. 
3. After examination of the confusion matrix and classification report for each model, it was determined that the optimal models to hone and delve deeper would be an XGBoost model and a Random Forest model.
4. For each of these two models, we dove deeper and tried to optimize results by using GridSearch to find the best parameters, as well as SMOTE, to deal with class imbalances and Type II errors.

## Analysis of Models
### Random Forest:   
* After using GridSearch, we found that the most optimal parameters were 'criterion' = 'gini', 'max_depth' = None, 'min_samples_leaf' = 3, and 'min_samples_split' = 10. This improved our accuracy score for training and testing data.  
* SMOTE helped remove some of the Type II errors, but it also created an overfitting issue, as training accuracy increased while testing accuracy decreased.    
### XGBoost:  
* After using GridSearch, we found that the most optimal parameters were learning_rate = 0.2, max_depth = 7, min_child_weight = 2, n_estimators = 100, subsample = 0.7.
* 

## Findings
### Random Forest:  
Our final model showed that the features with the highest impact were:  
* AGE_TWENTIES (injury prone)  
* DRIVER_FAULT (injury prone)  
* AGE_EIGHTIES (no injury)   
### XGBoost:  
Our final model showed that the features with the highest impact were:  
* AGE_EIGHTY OR OLDER
* DRIVER_FAULT
* CRASH_MONTH_2 - February

## Recommendations  


## Future Work
Explore other ways to improve injury classification, as the Precision, Recall, and F1 scores for injury in the testing group were substantially lower than those of no injury.











