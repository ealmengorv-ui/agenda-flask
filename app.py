from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

agenda = []


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        apellido = request.form["apellido"].strip()
        fecha_nacimiento = request.form["fecha_nacimiento"]
        dia_semana = request.form["dia_semana"]

        if nombre and apellido and fecha_nacimiento and dia_semana:
            persona = {
                "nombre": nombre,
                "apellido": apellido,
                "fecha_nacimiento": fecha_nacimiento,
                "dia_semana": dia_semana
            }

            agenda.append(persona)

        return redirect(url_for("inicio"))

    return render_template("agenda.html", agenda=agenda)


if __name__ == "__main__":
    app.run(debug=True)