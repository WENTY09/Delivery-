from flask import render_template, jsonify
from app import create_app, db
from app.models import User

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats_page():
    return render_template('stats.html')

@app.route('/api/stats')
def api_stats():
    total_users = User.query.count()
    total_deliveries = db.session.query(db.func.sum(User.deliveries)).scalar() or 0
    total_money = db.session.query(db.func.sum(User.money)).scalar() or 0
    return jsonify({
        "total_users": total_users,
        "total_deliveries": total_deliveries,
        "total_money": total_money
    })
