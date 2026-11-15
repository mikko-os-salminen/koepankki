import db

def add_test(aine, aihe, vuosi, koe, user_id):
    sql = "INSERT INTO tests (aine, aihe, vuosi, koe, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [aine, aihe, vuosi, koe, user_id])


def get_tests():
    sql = "SELECT id, aine, aihe, vuosi, user_id FROM tests ORDER BY aine"

    return db.query(sql)

def get_test(test_id):
    sql = """SELECT users.username,
                    users.id user_id,
                    tests.id,
                    tests.aine,
                    tests.aihe,
                    tests.vuosi,
                    tests.koe
            FROM users, tests
            WHERE tests.user_id = users.id AND
                tests.id = ?"""

    return db.query(sql, [test_id])[0]

def update_test(test_id, aine, aihe, vuosi, koe):
    sql = """UPDATE tests SET aine = ?,
                              aihe = ?,
                              vuosi = ?,
                              koe = ?
                          WHERE id = ?"""
    db.execute(sql, [aine, aihe, vuosi, koe, test_id])

def remove_test(test_id):
    sql = "DELETE FROM tests WHERE id = ?"
    db.execute(sql, [test_id])
