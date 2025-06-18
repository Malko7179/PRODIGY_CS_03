from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    length_ok = len(password) >= 8
    lower_ok = bool(re.search(r"[a-z]", password))
    upper_ok = bool(re.search(r"[A-Z]", password))
    digit_ok = bool(re.search(r"\d", password))
    special_ok = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    score = sum([length_ok, lower_ok, upper_ok, digit_ok, special_ok])
    verdict = {5:"Very Strong",4:"Strong",3:"Medium",2:"Weak"}.get(score, "Very Weak")
    
    suggestions = []
    if not length_ok: suggestions.append("Use at least 8 characters")
    if not lower_ok: suggestions.append("Add lowercase letters")
    if not upper_ok: suggestions.append("Add uppercase letters")
    if not digit_ok: suggestions.append("Include numbers")
    if not special_ok: suggestions.append("Use special characters like !@#$%")
    
    return {"score": score, "verdict": verdict, "suggestions": suggestions}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    result = check_password_strength(data.get("password", ""))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
