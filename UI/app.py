from flask import Flask, render_template, send_from_directory, request
from scripts import plot_functions, feature_data_mapping
import numpy as np

app = Flask(__name__)


@app.route('/')
def main_page():
    product_categories = feature_data_mapping.get_product_category_mappings()
    symptoms_list = feature_data_mapping.get_symptom_list()

    return render_template('main.html',
                           product_categories=product_categories,
                           symptoms_list=symptoms_list)


@app.route('/static/<filename>')
def static_content(filename):
    return send_from_directory('static', filename=filename)


@app.route("/find_data", methods=['POST'])
def find_data():
    age = feature_data_mapping.to_number(request.form.get('age'))
    gender = feature_data_mapping.to_number(request.form.get('gender'))
    product_category = feature_data_mapping.to_number(request.form.get('prod_category'))
    symptoms_list = request.form.getlist('symptoms')

    absolute_plot_path = plot_functions.calculate_illnesses(
        age=age,
        gender=gender,
        product_category=product_category,
        symptoms_list=symptoms_list
    )
    web_plot_path = absolute_plot_path.split('..')[1]

    # nearest_racks = [divvy_stations_for_querying['nearby_stations_in_feet']==
    return render_template(
        'illness_info.html',
        illnesses_plot_path=web_plot_path
    )


def do_something_for_user(username):
    return "Hello user: {}".format(username)


if __name__ == '__main__':
    app.run()
