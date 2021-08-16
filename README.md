![pedro-lastra-Nyvq2juw4_o-unsplash (1)](https://user-images.githubusercontent.com/75818628/129616561-9e4b9e88-1bce-499f-89b1-88dc448d0dcc.jpg)
# Chicago Traffic Accidents  
Classification Models  
**Project Partners: Jojo de Leon and Harrison Gu

## Project objective: 
Our aim is to investigate the factors of reported accidents in the city of Chicago to ascertain which features are more likely to lead to an accident that involves injury in order to aid the city of Chicago in allocating their limited ambulatory services.

## Data
Our Chicago Traffic Accidents datasets came from the city of Chicago’s data portal. We combined two datasets, one that was referenced by the vehicle while the other regarded the person(s) involved in the accident. The information contained is derived from all reported accidents from 2015 to present day. 

https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3  
https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d  

## Methodology  
1. The Crash Record ID, which was present in both datasets, was used to combine the two. Initially, there were over 1.6 million accidents with 79 features for each accident to explore. We chose to concentrate on accidents in which at least one vehicle was a car.  As such, records pertaining to cyclists and pedestrians were eliminated. Furthermore, for the features we identified as relevant, any unknown or missing entry for a relevant feature within a record disqualified that record for use. Our models are based on 17 features of roughly 162 thousand accident records. 
2. 














