import hashlib

# 사용자 딕셔너리 정의
users = {
    'admin1': hashlib.sha256('asdfghjhgfd'.encode()).hexdigest(),
    'admin2': hashlib.sha256('erthrgeggrf'.encode()).hexdigest(),
    'admin3': hashlib.sha256('vhbijdjbdkm'.encode()).hexdigest(),
    'admin4': hashlib.sha256('lp,lfpvfebb'.encode()).hexdigest(),
    'admin5': hashlib.sha256('koinjiuhhuv'.encode()).hexdigest(),
}

def login(username, password):
    # 입력 받은 비밀번호의 해시값 계산
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # 사용자 딕셔너리에서 아이디 검증
    if username in users:
        # 비밀번호 해시값 검증
        if users[username] == password_hash:
            return True, "Login successful."
        else:
            return False, "Invalid password."
    else:
        return False, "User not found."