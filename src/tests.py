import db

def add_test(aine, aihe, vuosi, koe, user_id):
    sql = "INSERT INTO tests (aine, aihe, vuosi, koe, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [aine, aihe, vuosi, koe, user_id])


def get_tests():
    sql = "SELECT id, aine, aihe, vuosi, user_id FROM tests ORDER BY aine"

    return db.query(sql)

def get_test(test_id):
    sql = """SELECT users.username,
                    tests.aine,
                    tests.aihe,
                    tests.vuosi,
                    tests.koe
            FROM users, tests
            WHERE tests.user_id = users.id AND
                tests.id = ?"""
    
    return db.query(sql, [test_id])[0]