from flask import Blueprint, request, jsonify
from provider.auths.login import login  # login 함수 임포트

auths_router = Blueprint('auths', __name__)

@auths_router.route('/logIn', methods=['POST'])
def handle_login():
    # 요청에서 아이디와 비밀번호 추출
    username = request.json.get('username')
    password = request.json.get('password')
    
    # 로그인 함수 호출
    success, message = login(username, password)
    
    # 응답 반환
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"message": message}), 401
