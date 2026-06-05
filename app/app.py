from flask import Flask, request, escape
import sqlite3
import os
import yaml
import subprocess
app = Flask(__name__)
@app.route("/")
def home():
 return "Payment Review API - Assessment Lab"
@app.route("/payment")
def get_payment():
 username = request.args.get("user")
 conn = sqlite3.connect("payments.db")
 cursor = conn.cursor()
 query = "SELECT * FROM payments WHERE username = ?"
 cursor.execute(query, (username,))
 result = cursor.fetchall()
 conn.close()
 return str(result)
@app.route("/admin/run")
def admin_run():
action = request.args.get("cmd", "")
allowed_commands = {
  "list_dir": ["ls"],
 "show_user": ["whoami"],
 "show_date": ["date"]
 }
 if action not in allowed_commands:
  return "Invalid command", 400
 return subprocess.check_output(allowed_commands[action], text=True)

@app.route("/account")
def account():
 account_id = request.args.get("id")
 accounts = {
 "1": "Alice Account Balance: 5000",
 "2": "Bob Account Balance: 7500",
 "3": "Admin Account Balance: 99999"
 }
 return accounts.get(account_id, "Account not found")
@app.route("/config/load", methods=["POST"])
def load_config():
 data = request.data.decode("utf-8")
 parsed = yaml.safe_load(data)
 return escape(str(parsed)) 
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000, debug=False)