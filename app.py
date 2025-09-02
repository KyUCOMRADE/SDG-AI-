from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv
import os
import requests
from openai import OpenAI

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Paystack Keys
PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")

# OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Routes
@app.route("/")
def home():
    return render_template("index.html", paystack_key=PAYSTACK_PUBLIC_KEY)

# AI Suggestion Route
@app.route("/get_suggestion", methods=["POST"])
def get_suggestion():
    try:
        user_prompt = request.json.get("prompt")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI assistant that gives real-world solutions."},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150
        )

        return jsonify({"suggestion": response.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"error": str(e)})

# Payment Initialization
@app.route("/initiate_payment", methods=["POST"])
def initiate_payment():
    email = request.form.get("email")
    amount = int(request.form.get("amount")) * 100  # Convert to kobo (Paystack requirement)

    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "amount": amount,
        "currency": "KES"  # Use "KES" for Kenyan Shillings
    }

    response = requests.post("https://api.paystack.co/transaction/initialize", headers=headers, json=data)
    res_json = response.json()

    if res_json.get("status"):
        return redirect(res_json["data"]["authorization_url"])
    else:
        return jsonify({"error": res_json.get("message")})

if __name__ == "__main__":
    app.run(debug=True)
