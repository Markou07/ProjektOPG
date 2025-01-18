from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# cesta k suboru s rezervaciami
REZERVACIE_SUBOR = "rezervacie.txt"


# hlavna stranka
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        datum = request.form["datum"]
        cas = request.form["cas"]
        miesto = request.form["miesto"]
        popis = request.form["popis"]

        # ulozenie rezervacie do suboru
        with open(REZERVACIE_SUBOR, "a", encoding="utf-8") as subor:
            subor.write(f"{datum} {cas} {miesto} {popis}\n")

        return redirect(url_for("index"))
    return render_template("index.html")



