<h1> Airline Satisfaction </h1>

<h2> Scope </h2>

The purpose of this project is to treat it as a practical case, trying to solve a real world company problem with the data provided. The objective is create value to this 
hypothetical company by analyzing the data.

The dataset used for the project is from Kaggle: Airline Passanger Satisfaction. Uploaded by TJ Klein, link right below:

https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

This dataset has been chosen because in Kaggle it has a great usability (9.41) which eases a lot working on it, and because it was directly related to an industry, which 
helps elaborating conclussions from a business point of view.

In this practical case my company has provided me the results of a recent poll run on passengers after having flown with this airline and I'm being asked what services 
evaluated are more valuable to the customers, in order to invest in upgrading one or another.

<h2> Input </h2>

The data provided is divided in 2 datasets: a train and a test one. They have the same amount of features and target, which is wether the customer is satisfied overall or 
neutral/dissatisfied. The split is 20%, which means that the train dataset holds 80% of the customers and the test one, used for prediction purposes holds the rest.

Each passenger has assigned 22 features, amongst which there is information about their trip (distance, type of travel...), personal information (age, gender) and the poll 
results over the different services, ranked from 0 to 5. Thus, most of the features can be considered as categorical and the modeling problem is a binary classification since 
each customer is overall satisfied or neutral/dissatisfied with the airline.

<h2> Technologies Used </h2>

OS: Windows 10

Programming Language: Python 3.10.5 

IDE: VSCode (jupyter notebook extension)

Command Prompt: Windows Terminal

Python package management: pip

<h2> Index of the project </h2>

**NOTE**: All the project is commented throughout the main notebook airline_satisfaction.ipynb  

  - Import Libraries  
  - Exploratory Data Analysis  
  - Data Preparation  
  - Modeling  
  - Model Optimization  
  - Test dataset
  
<h2> Conclusion </h2>

In the EDA there were some features that showed a strong trend towards the overall satisfaction of the customer, such as the inflight wifi service. These features that have
very radicalized results have far more influence than the ones that have "the expected" distribution, and this hypothesis was confirmed after analyzing the weight of the 
features used for the model.

Thus, the airline should invest specially in these features, focusing on services such as the wifi service and online services. Also if they want to segmentate in marketing,
they could focus on business travellers to establish themselves as the airline for business trips.

