from flask import Flask, request, jsonify

app = Flask(__name__)


def check_attendance(att):
    if att <= 80:
        print("Not allowed to sit in exam")
    print("Allowed")

@app.route("/")
def home():
    return "Student Attendance System"


@app.route("/check-attendance", methods=["POST"])
def check_attendance_balance():
    data = request.get_json()

    att = data["att"]
    

    if check_attendance(att):
        return jsonify({
            "message": "Allowed"
        }), 200

    return jsonify({
        "message": "Insufficient"
    }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)