from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/productionquality", methods=["GET", "POST"])
def calculator():
    results = None
    results2=None
    if request.method== "POST":
        if request.form.get("form_type") == "fpy":
            good_units = float(request.form["good_units"])
            total_units = float(request.form["total_units"])

            results = good_units / total_units

        if request.form.get("form_type") == "oee":
            availability = float(request.form["availability"])
            performance = float(request.form["performance"])
            quality = float(request.form["quality"])

            results2 = availability*performance*quality 
    return render_template("productionquality.html", result=results,result2=results2)

@app.route("/business",methods=["GET","POST"])
def business():
    results = None
    results2=None
    if request.method== "POST":
        if request.form.get("form_type") == "roi":
            net_profit = float(request.form["net_profit"])
            investment = float(request.form["investment"])

            results = net_profit / investment

        if request.form.get("form_type") == "rg":
            current_rev = float(request.form["current_rev"])
            previous_rev = float(request.form["previous_rev"])

            results2 = (current_rev-previous_rev) / previous_rev
    return render_template("business.html", result=results,result2=results2)

if __name__ == "__main__":
    app.run(debug=True)