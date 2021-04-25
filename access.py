from db import db

def user_in_db(username):
    sql = "SELECT * FROM users WHERE username=:username;"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    return user

def create_user(username, password_hash):
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password);"
        db.session.execute(sql, {"username": username, "password": password_hash})
        db.session.commit()
        return True
    except:
        return False

def get_user_id(username):
    sql = "SELECT id FROM users WHERE username=:username;"
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone()
    return user_id

def material_content(owner_id=None):
    if owner_id == None:
        sql = "SELECT DISTINCT M.*, U.username FROM (SELECT M.*, coalesce(L.likes,0) likes FROM materials M LEFT JOIN (SELECT material_id, sum(like_value) LIKES FROM likes GROUP BY material_id) L ON M.id=L.material_id) M, chapters C, users U WHERE U.id=M.owner_id AND M.id=C.material_id ORDER BY M.likes DESC;"
        content = db.session.execute(sql)
        return content
    else:
        sql = "SELECT M.*, U.username FROM (SELECT M.*, coalesce(L.likes,0) likes FROM materials M LEFT JOIN (SELECT material_id, sum(like_value) LIKES FROM likes GROUP BY material_id) L ON M.id=L.material_id) M, users U WHERE U.id=M.owner_id AND M.owner_id=:owner_id ORDER BY M.likes DESC;"
        content = db.session.execute(sql, {"owner_id": owner_id})
        return content

def materials_by_name(name):
    sql = "SELECT DISTINCT M.*, U.username FROM (SELECT M.*, coalesce(L.likes,0) likes FROM materials M LEFT JOIN (SELECT material_id, sum(like_value) LIKES FROM likes GROUP BY material_id) L ON M.id=L.material_id) M, chapters C, users U WHERE U.id=M.owner_id AND M.id=C.material_id AND M.name LIKE :name ORDER BY M.likes DESC;"
    content = db.session.execute(sql, {"name": "%" + name + "%"})
    materials = content.fetchall()
    return materials

def materials_by_author(author):
    sql = "SELECT DISTINCT M.*, U.username FROM (SELECT M.*, coalesce(L.likes,0) likes FROM materials M LEFT JOIN (SELECT material_id, sum(like_value) LIKES FROM likes GROUP BY material_id) L ON M.id=L.material_id) M, chapters C, users U WHERE U.id=M.owner_id AND U.username=:author AND M.id=C.material_id ORDER BY M.likes DESC;"
    content = db.session.execute(sql, {"author": author})
    materials = content.fetchall()
    return materials

def materials_by_category(category):
    sql = "SELECT DISTINCT M.*, U.username FROM (SELECT M.*, coalesce(L.likes,0) likes FROM materials M LEFT JOIN (SELECT material_id, sum(like_value) LIKES FROM likes GROUP BY material_id) L ON M.id=L.material_id) M, chapters C, users U WHERE U.id=M.owner_id AND M.id=C.material_id AND M.category_name=:category ORDER BY M.likes DESC;"
    content = db.session.execute(sql, {"category": category})
    materials = content.fetchall()
    return materials

def create_material(name, description, contents, owner_id, category):
    try:
        sql = "INSERT INTO materials (name, description, content_raw, owner_id, category_name) VALUES (:name, :description, :contents, :owner_id, :category_name);"
        db.session.execute(sql, {"name": name, "description": description, "contents": contents, "owner_id": owner_id, "category_name": category})
        db.session.commit()
        return True
    except:
        return False

def user_material(user_id, material_id):
    sql = "SELECT * FROM materials WHERE owner_id=:user_id AND id=:material_id;"
    content = db.session.execute(sql, {"user_id": user_id, "material_id": material_id})
    material = content.fetchone()
    return material

def material_by_id(material_id):
    sql = "SELECT * FROM materials WHERE id=:material_id;"
    content = db.session.execute(sql, {"material_id": material_id})
    material = content.fetchone()
    return material

def update_contents(material_id, contents):
    try:
        sql = "UPDATE materials SET content_raw=:contents WHERE id=:material_id;"
        db.session.execute(sql, {'material_id': material_id, 'contents': contents})
        db.session.commit()
        return True
    except:
        return False

def update_material_name(material_id, name):
    try:
        sql = "UPDATE materials SET name=:name WHERE id=:material_id;"
        db.session.execute(sql, {'material_id': material_id, 'name': name})
        db.session.commit()
        return True
    except:
        return False

def chapters_by_id(material_id):
    sql = "SELECT * FROM chapters WHERE material_id=:material_id;"
    content = db.session.execute(sql, {"material_id": material_id})
    chapters = content.fetchall()
    return chapters

def create_chapter(name, material_id, content_raw):
    try:
        sql = "INSERT INTO chapters (name, material_id, content_raw) VALUES (:name, :material_id, :content_raw);"
        db.session.execute(sql, {"name": name, "material_id": material_id, "content_raw": content_raw})
        db.session.commit()
        return True
    except:
        return False

def chapter_by_id(chapter_id):
    sql = "SELECT * FROM chapters WHERE id=:chapter_id;"
    content = db.session.execute(sql, {"chapter_id": chapter_id})
    chapter = content.fetchone()
    return chapter

def chapter_contents(chapter_id, contents):
    try:
        sql = "UPDATE chapters SET content_raw=:contents WHERE id=:chapter_id;"
        db.session.execute(sql, {'chapter_id': chapter_id, 'contents': contents})
        db.session.commit()
        return True
    except:
        return False

def user_chapter(user_id, material_id, chapter_id):
    sql = "SELECT C.*, M.owner_id FROM chapters C, materials M WHERE C.material_id=M.id and C.id=:chapter_id and M.owner_id=:user_id;"
    content = db.session.execute(sql, {"chapter_id": chapter_id, "material_id": material_id, "user_id": user_id})
    chapter = content.fetchone()
    return chapter

def drop_material(material_id):
    sql = "DELETE FROM materials WHERE id=:material_id;"
    db.session.execute(sql, {"material_id": material_id})
    db.session.commit()

def add_feedback(material_id, user_id, feedback):
    sql = "INSERT INTO feedback (material_id, user_id, content_raw) VALUES (:material_id, :user_id, :feedback);"
    db.session.execute(sql, {"material_id": material_id, "user_id": user_id, "feedback": feedback})
    db.session.commit()

def get_feedback(material_id):
    sql = "SELECT F.content_raw, U.username FROM feedback F, materials M, users U WHERE F.material_id=M.id AND F.user_id=U.id AND M.id=:material_id;"
    content = db.session.execute(sql, {"material_id": material_id})
    feedback = content.fetchall()
    return feedback

def like(material_id, user_id, like_value):
    try:
        sql = "INSERT INTO likes (material_id, user_id, like_value) VALUES (:material_id, :user_id, :like_value);"
        db.session.execute(sql, {"material_id": material_id, "user_id": user_id, "like_value": like_value})
        db.session.commit()
    except:
        db.session.rollback()
        sql = "UPDATE likes SET like_value=:like_value WHERE material_id=:material_id AND user_id=:user_id;"
        db.session.execute(sql, {'material_id': material_id, 'user_id': user_id, 'like_value': like_value})
        db.session.commit()

def like_status(material_id, user_id):
    sql = "SELECT like_value FROM likes WHERE material_id=:material_id AND user_id=:user_id;"
    content = db.session.execute(sql, {"material_id": material_id, "user_id": user_id})
    likes = content.fetchone()
    return likes