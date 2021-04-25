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
        sql = "SELECT DISTINCT M.id, M.name, M.description FROM materials M, chapters C WHERE M.id=C.material_id;"
        content = db.session.execute(sql)
        return content
    else:
        sql = "SELECT id, name, description FROM materials WHERE owner_id=:owner_id;"
        content = db.session.execute(sql, {"owner_id": owner_id})
        return content

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
    sql = "SELECT chapters.*, materials.owner_id FROM chapters, materials WHERE chapters.material_id=materials.id and chapters.id=:chapter_id and materials.owner_id=:user_id;"
    content = db.session.execute(sql, {"chapter_id": chapter_id, "material_id": material_id, "user_id": user_id})
    chapter = content.fetchone()
    return chapter

def materials_by_name(name):
    sql = "SELECT * FROM materials WHERE name LIKE :name;"
    content = db.session.execute(sql, {"name": "%" + name + "%"})
    materials = content.fetchall()
    return materials

def materials_by_author(author):
    sql = "SELECT M.* FROM users U, materials M WHERE U.username=:author and U.id=M.owner_id;"
    content = db.session.execute(sql, {"author": author})
    materials = content.fetchall()
    return materials

def materials_by_category(category):
    sql = "SELECT * FROM materials WHERE category_name=:category;"
    content = db.session.execute(sql, {"category": category})
    materials = content.fetchall()
    return materials

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