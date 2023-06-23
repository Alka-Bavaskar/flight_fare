from flask import Flask,jsonify,render_template,request

from project_app.utils import Flight_Fare

app = Flask(__name__)

@app.route("/")
def hello():
    print("Welcome to Flight Fare Prediction System")
    return render_template("test.html")

@app.route("/predict_price", methods = ["POST","GET"])

def get_flight_charges():
    if request.method == "GET":

        airline          = (request.args.get("airline"))
        source_city      = (request.args.get("source_city"))
        departure_time   = (request.args.get("departure_time"))
        stops            = (request.args.get("stops"))
        arrival_time     = (request.args.get("arrival_time"))
        destination_city = (request.args.get("destination_city"))
        class_           = (request.args.get("class_"))
        duration         = (request.args.get("duration"))
        days_left        = (request.args.get("days_left"))


        flight_price = Flight_Fare(airline,source_city,departure_time,stops,arrival_time,
                                   destination_city,class_,duration,days_left)
        price = flight_price.get_predicted_price()

        return render_template("test.html",prediction = price)
    
if __name__ == "__main__":
    # app.run()
    app.run(debug=True ,port=8080,use_reloader=False)
