import sys

from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomDataset, PredictPipeline
from src.exception import CustomException
from src.logging import logging


app = Flask(__name__)
#app = application

try:
    @app.route('/', methods=['GET'])
    def predict_datapoint():
        if request.method == 'GET':
            return render_template('form.html')
        
except Exception as e:
    logging.info("An exception has occured in home route.")
    raise CustomException(e, sys)

try:
    @app.route('/prediction', methods=['POST'])
    def prediction():
        data = CustomDataset()
        data_frame = data.get_data_as_dataframe(LIMIT_BAL=float(request.form.get('LIMIT_BAL')),
                                                SEX=int(request.form.get('SEX')),
                                                EDUCATION=int(request.form.get('EDUCATION')),
                                                MARRIAGE=int(request.form.get('MARRIAGE')),
                                                AGE=int(request.form.get('AGE')),
                                                PAY_0=int(request.form.get('PAY_0')),
                                                PAY_2=int(request.form.get('PAY_2')),
                                                PAY_3=int(request.form.get('PAY_3')),
                                                PAY_4=int(request.form.get('PAY_4')),
                                                PAY_5=int(request.form.get('PAY_5')),
                                                PAY_6=int(request.form.get('PAY_6')),
                                                BILL_AMT1=float(request.form.get('BILL_AMT1')),
                                                BILL_AMT2=float(request.form.get('BILL_AMT2')),
                                                BILL_AMT3=float(request.form.get('BILL_AMT3')),
                                                BILL_AMT4=float(request.form.get('BILL_AMT4')),
                                                BILL_AMT5=float(request.form.get('BILL_AMT5')),
                                                BILL_AMT6=float(request.form.get('BILL_AMT6')),
                                                PAY_AMT1=float(request.form.get('PAY_AMT1')),
                                                PAY_AMT2=float(request.form.get('PAY_AMT2')),
                                                PAY_AMT3=float(request.form.get('PAY_AMT3')),
                                                PAY_AMT4=float(request.form.get('PAY_AMT4')),
                                                PAY_AMT5=float(request.form.get('PAY_AMT5')),
                                                PAY_AMT6=float(request.form.get('PAY_AMT6')))

        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(data_frame)

        result = prediction.tolist()
        if result[0] == 1:
            string = "This person will not pay credit next month"
        else:
            string = "This person will pay credit next month"

        print(string)

        return render_template('result.html', final_result=string)
    
except Exception as e:
    logging.info("An exception has occured in prediction route.")
    raise CustomException(e, sys)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
