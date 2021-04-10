class MaterialDao:
    
    def __init__(self, db):
        self.db = db

    def material_content(self, owner_id=None):
        if owner_id == None:
            sql = "SELECT id, name, description FROM materials;"
            content = self.db.session.execute(sql)
            return content
        else:
            sql = "SELECT id, name, description FROM materials WHERE owner_id=:owner_id;"
            content = self.db.session.execute(sql, {"owner_id": owner_id})
            return content

    def create_material(self, name, description, contents, owner_id, category):
        try:
            sql = "INSERT INTO materials (name, description, content_raw, owner_id, category_name) VALUES (:name, :description, :contents, :owner_id, :category_name);"
            self.db.session.execute(sql, {"name": name, "description": description, "contents": contents, "owner_id": owner_id, "category_name": category})
            self.db.session.commit()
            return True
        except:
            return False

    def user_material(self, user_id, material_id):
        sql = "SELECT * FROM materials WHERE owner_id=:user_id AND id=:material_id;"
        content = self.db.session.execute(sql, {"user_id": user_id, "material_id": material_id})
        material = content.fetchone()
        return material

    def material_by_id(self, material_id):
        sql = "SELECT * FROM materials WHERE id=:material_id;"
        content = self.db.session.execute(sql, {"material_id": material_id})
        material = content.fetchone()
        return material

    def update_contents(self, material_id, contents):
        try:
            sql = "UPDATE materials SET content_raw=:contents WHERE id=:material_id;"
            self.db.session.execute(sql, {'material_id': material_id, 'contents': contents})
            self.db.session.commit()
            return True
        except:
            return False