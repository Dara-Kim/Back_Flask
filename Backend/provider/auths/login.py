from flask import jsonify
import hashlib

# Defining Dictionary
users = {
    "admin1": hashlib.sha256("asdfghjhgfd".encode()).hexdigest(),
    "admin2": hashlib.sha256("erthrgeggrf".encode()).hexdigest(),
    "admin3": hashlib.sha256("vhbijdjbdkm".encode()).hexdigest(),
    "admin4": hashlib.sha256("lp,lfpvfebb".encode()).hexdigest(),
    "admin5": hashlib.sha256("koinjiuhhuv".encode()).hexdigest(),
}


def login(username, password):
    # Verifying Input
    if not username or not password:
        return False, jsonify({"error": "Bad Request"}), 400
    # Verifying User
    if username not in users:
        return False, jsonify({"error": "Not Found"}), 404
    # Verifying Password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if users[username] == password_hash:
        return True, jsonify({"message": "OK"}), 200
    else:
        return False, jsonify({"error": "Forbidden"}), 403
