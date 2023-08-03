# Driver Distraction Detection
## Introduction
This project is helps in detecting driver distraction and drowsiness using a model trained on movinet.
This project will be further extended to detect driver distraction during the nighttime while at the same time improving the accuracy and the speed of the model and published as a paper soon.

# BlackSpot Detection
## Introduction
This project is helps in detecting blackspots on the road to prevent drivers from taking accident prone routes 
using a model trained on logistic regression.

Currently, for a small scale project this model only takes 5 attributes into consideration to predict the blackspots.
namely latitude, longitude, weather, time and day of the week.

This part of the project is still under development and will be updated soon to predict the alternate routes.

Currently due to the unavailability of a proper free api for maps this is not market ready.

At the moment the model is trained on a dataset given by San francisco city, as no other Indian city had released its recent public dataset.
This model can scale to any city with the help of the dataset provided by the city, this also takes into account the weather conditions in to the respect while predicting the blackspots.


