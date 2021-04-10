class UserDao:
    
    def __init__(self, db):
        self.db = db

    def user_in_db(self, username):
        sql = "SELECT * FROM users WHERE username=:username;"
        result = self.db.session.execute(sql, {"username": username})
        user = result.fetchone()
        return user

    def create_user(self, username, password_hash):
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username, :password);"
            self.db.session.execute(sql, {"username": username, "password": password_hash})
            self.db.session.commit()
            return True
        except:
            return False

    def get_user_id(self, username):
        sql = "SELECT id FROM users WHERE username=:username;"
        result = self.db.session.execute(sql, {"username": username})
        user_id = result.fetchone()
        return user_id