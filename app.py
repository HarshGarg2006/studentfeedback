from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []


@app.route("/", methods=["GET", "POST"])
def home():

    error = ""

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()
        feedback = request.form.get("feedback", "").strip()

        # Check email domain
        if not email.lower().endswith("@niet.co.in"):
            error = "Invalid Email! Please use @niet.co.in email."

            return render_template(
                "index.html",
                feedbacks=feedbacks,
                error=error
            )

        # Save feedback including EMAIL
        feedbacks.append({
            "name": name,
            "email": email,
            "course": course,
            "feedback": feedback
        })

    return render_template(
        "index.html",
        feedbacks=feedbacks,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)