import os
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from pandas.tools.plotting import table


'''
This function gets the probabilities per outcome based on the input data from the user.
It then puts those probabilities into a table and saves the table as a png file into the
graphs directory.
'''
def calculate_illnesses(age,
        gender,
        product_category,
        symptoms_list):

    figure_filepath = get_graphs_filepath('prob_table_df.png')

    prediction_array = to_array(age,
        gender,
        product_category,
        symptoms_list)


    # use the 4 args to calculate results into dictionary as below
    # initialize illnesses
    possible_illnesses = {
        'death': 0.,
        'life_threatening': 0.,
        'serious_injuries_illness': 0.,
        'disability': 0.,
        'other_serious__important_medical_events_': 0.,
        'congenital_anomaly': 0.,
        'req_intervention_to_prvnt_perm_imprmnt': 0.,
        'hospitalization': 0.,
        'visited_an_er': 0.,
        'visited_a_health_care_provider': 0.
    }

    with open(get_pickle_filepath('forest_tuned_lowbias_fitted.pkl'), 'rb') as picklefile:
        forest_tuned_lowbias_fitted = pickle.load(picklefile)

        # calculate illnesses
        illness_probabilities = forest_tuned_lowbias_fitted.predict_proba(prediction_array)
        illnesses_list = list(possible_illnesses.keys())
        illness_probabilities_list = list(illness_probabilities[0])
        illness_probabilities_series = pd.Series(illness_probabilities_list)
        illness_probabilities_series = illness_probabilities_series*100
        possible_illnesses_table = pd.DataFrame({'Possible Outcome': illnesses_list, 'Probability': illness_probabilities_series})

        ax = plt.subplot(111, frame_on=False)  # no visible frame
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis

        table(ax, possible_illnesses_table, loc='center')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        plt.savefig(figure_filepath)

    return figure_filepath


'''This function creates a numpy array out of the user inputs so that 
probability predictions could be generated. '''

def to_array(age,
        gender,
        product_category,
        symptoms_list):

    symptoms_dict = {
        'diarrhea':0,
        'mood_swing':0,
        'renal_function':0,
        'upper_respiratory_tract_infection':0,
        'prothrombin_time':0,
        'bleeding':0,
        'nasal_congestion':0,
        'drug_overdose':0,
        'angina':0,
        'dysbiosis':0,
        'overactive_bladder':0,
        'suicide_terminology':0,
        'epileptic_seizure':0,
        'nephrotoxicity':0
    }

    for input_feature in symptoms_list:
        symptoms_dict[input_feature] += 1


    prediction_list = [product_category]

    for value in symptoms_dict.values():
        prediction_list.append(value)

    prediction_list.append(age)
    prediction_list.append(gender)

    return np.array(prediction_list).reshape(1,-1)


def get_pickle_filepath(filename):
    return os.path.join(os.path.dirname(__file__), '../scripts', filename)


def get_graphs_filepath(filename):
    return os.path.join(os.path.dirname(__file__), '../static/graphs', filename)


if __name__ == '__main__':
    calculate_illnesses(34, 0, 2, ['', ''])
