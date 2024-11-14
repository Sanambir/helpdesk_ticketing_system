# app/app.py
#
from flask import Flask, request, render_template, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for tickets (for simplicity)
tickets = []

# Home route - Show all tickets
@app.route("/")
def index():
    return render_template("index.html", tickets=tickets)
##
# Route to create a new ticket
@app.route("/create_ticket", methods=["POST"])
def create_ticket():
    ticket = {
        "id": len(tickets) + 1,
        "title": request.form["title"],
        "description": request.form["description"],
        "status": "Open",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tickets.append(ticket)
    return redirect(url_for("index"))
# fixed something #
# Route to update a ticket's status
@app.route("/update_ticket/<int:ticket_id>", methods=["POST"])
def update_ticket(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = request.form["status"]
            break
    return redirect(url_for("index"))
#
if __name__ == "__main__":
    app.run(debug=True)
