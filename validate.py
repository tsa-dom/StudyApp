def username(username):
    if len(username) >= 4:
        return True
    else:
        return False

def password(password):
    if len(password) >= 8:
        return True
    else:
        return False

def equal(object_1, object_2):
    if object_1 == object_2:
        return True
    else:
        return False