from operator import contains

def check_email(string):
    index_at = string.find("@")
    index_dot = string.rfind(".")
    if index_dot < index_at:
        return False
    elif contains(string, " "):
        return False
    elif contains(string, "@."):
        return False
    elif contains(string, "@"):
        if index_dot > index_at:
            return True
    else:
        return False


