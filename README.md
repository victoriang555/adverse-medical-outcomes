# Adverse Medical Outcomes Prediction

This project seeks to predict the outcome of an adverse reaction to consuming a food, drug, or cosmetic product. 


# Motivation
I wanted to address the concerns around whether someone should seek medical care when feeling ill soon after consuming something. If someone has a high probability of being hospitalized or something even more dire, I would like to inform them of that probability so that they could seek medical attention right away. And vice versa, if they have a low probability of have any major reaction that would require medical attention, I would help them prevent spending a large sum of money on medical care.


# Models/Methods
1. KNN to conduct language classification for feature engineering 
2. PCA to reduce dimensions of vectorized corpus for feature engineering
3. Random Forest ensemble for final modeling 


# Main Tools/Modules/Languages  
1. Python & HTML5
2. pandas
3. scikitlearn
4. flask
5. wikipedia
6. matplotlib


# Model Features
1. Accuracy is 17% better than the dummy model.
2. Overfits in order to have more evenly distributed recall across the targets


# Installation
```bash
pip install -r requirements.txt 
python app.py 
```

# Repo Structure
UI- Contains all flask app files 
Notebooks and Pickles - Contains all notebooks and sub-directories with corresponding pickle fles



# Credits 
1. https://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm
2. https://en.wikipedia.org/wiki/Main_Page
3. http://wikipedia.readthedocs.io/en/latest/code.html