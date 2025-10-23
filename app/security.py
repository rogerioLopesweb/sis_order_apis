import bcrypt

def hash_password(password: str) -> str:
    """
    Cria um hash seguro da senha usando bcrypt
    """
    # Converte a senha para bytes e gera o salt
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    
    # Gera o hash
    hashed = bcrypt.hashpw(password_bytes, salt)
    
    # Retorna o hash como string
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha está correta
    """
    try:
        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    except Exception:
        return False