import hashlib

# ����� ��ųʸ� ����
users = {
    'admin1': hashlib.sha256('asdfghjhgfd'.encode()).hexdigest(),
    'admin2': hashlib.sha256('erthrgeggrf'.encode()).hexdigest(),
    'admin3': hashlib.sha256('vhbijdjbdkm'.encode()).hexdigest(),
    'admin4': hashlib.sha256('lp,lfpvfebb'.encode()).hexdigest(),
    'admin5': hashlib.sha256('koinjiuhhuv'.encode()).hexdigest(),
}

def login(username, password):
    # �Է� ���� ��й�ȣ�� �ؽð� ���
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # ����� ��ųʸ����� ���̵� ����
    if username in users:
        # ��й�ȣ �ؽð� ����
        if users[username] == password_hash:
            return True, "Login successful."
        else:
            return False, "Invalid password."
    else:
        return False, "User not found."