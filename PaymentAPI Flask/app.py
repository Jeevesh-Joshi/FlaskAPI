from flask import Flask, jsonify, request
from flask_api import FlaskAPI, status, exceptions
import re
# from flask_restful import Resource, Api 

from datetime import date

app = Flask(__name__) 

@app.route("/payment", methods=['POST'])
def ProcessPayment():
    try:
        if request.method == 'POST':
            try:
                data = request.form
                if re.search("^[0-9]{16}$", data['CreditCardNumber']):
                    if re.search("^([A-Za-z ]+)$", data['HolderName']):
                        if re.search("^[0-9]{2}[/-][0-9]{2}[/-][2][0][2-9]{2}$", data['ExpirationDate']):
                            if re.search("^([0-9.]+)$", data['Amount']):
                                amount = float(data['Amount'])
                                if  amount<20:
                                    # CheapPaymentGateway
                                    pass
                                elif amount<500:
                                    # ExpensivePaymentGateway
                                    pass
                                else:
                                    # PremiumPaymentGateway
                                    pass
                                return jsonify({'status': status.HTTP_200_OK})
                            else:
                                return jsonify({'status': status.HTTP_400_BAD_REQUEST})
                        else:
                            return jsonify({'status': status.HTTP_400_BAD_REQUEST})
                    else:
                        return jsonify({'status': status.HTTP_400_BAD_REQUEST})
                else:
                    return jsonify({'status': status.HTTP_400_BAD_REQUEST})
            except:
                return jsonify({'status': status.HTTP_400_BAD_REQUEST})
    except:
        return jsonify({'status': status.HTTP_500_INTERNAL_SERVER_ERROR})
        

if __name__ == '__main__': 

	app.run(debug = True) 
