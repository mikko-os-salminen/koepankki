import db

def add_test(aine, aihe, vuosi, koe, user_id):
    sql = "INSERT INTO tests (aine, aihe, vuosi, koe, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [aine, aihe, vuosi, koe, user_id])