from flask import Flask, render_template, Response, send_file, jsonify
import csv

app = Flask(__name__)

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        # print(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data
file_path = r"C:\Users\PXR0OGF\OneDrive - NEE\Mock Data CSV.csv"

@app.route("/")
def home():
    site_info = read_csv(file_path)  # Specify the path to your CSV file
    return render_template('index.html', site_info = site_info)

@app.route('/<site>')
def post(site):
    site_info= read_csv(file_path)  # Update with your CSV file path
    site_data = next((item for item in site_info if item['site'] == site), None)
    # print(site_data)
    return render_template('specSite.html', site=site_data)

# @app.route('/post/<site>')
# def post(site):
#     site_info = read_csv('path_to_your_csv_file.csv')  # Update with your CSV file path
#     site_data = next((item for item in site_info if item['site'] == site), None)
#     return render_template('specSite.html', site=site_data)





if __name__ == '__main__':
    app.run(debug=True)


