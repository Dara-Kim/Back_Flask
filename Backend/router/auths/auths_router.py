from flask import Blueprint, request, jsonify
from provider.auths.login import login  # login �Լ� ����Ʈ

auths_router = Blueprint('auths', __name__)

@auths_router.route('/logIn', methods=['POST'])
def handle_login():
    # ��û���� ���̵�� ��й�ȣ ����
    username = request.json.get('username')
    password = request.json.get('password')
    
    # �α��� �Լ� ȣ��
    success, message = login(username, password)
    
    # ���� ��ȯ
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"message": message}), 401
