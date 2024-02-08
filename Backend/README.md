# DASORI
Project Dasori: SKT FLY AI 4기 Ziller DaSori 서비스 프로젝트의 Backend Repository입니다.

Backend: 김다은, 문정현, 이가경


---
## 폴더 구조

app: 어플리케이션 구동 폴더
config: 환경 변수 설정이니까 배포할 때 다시 생각해보기
manage.py: 호스팅 서버 주소, 완료된 app을 불러옴
model: 각 DB 별 ORM 관리 폴더 
provider: API 작성 파일 폴더
router: 각 API 별 blueprint 관리 폴더

.
├── README.md
├── app
│   └── __init__.py
├── config
│   ├── __init__.py 
│   └── flask_config.py
├── manage.py
├── model
│   ├── __init__.py
│   └── member_model.py
│   └── parent_model.py
│   └── child_model.py
├── provider
│   ├── __init__.py
│   ├── common_provider.py
│   ├── auths
│   │   ├── __init__.py
│   │   └── signup.py
│   │   └── login.py
│   │   └── find_account.py
│   ├── diary
│   │   ├── __init__.py
│   │   └── diary_management.py
│   └── stats
│       ├── __init__.py
│       ├── parent_stats.py
│       └── child_stats.py
├── requirements.txt
└── router
    ├── __init__.py
    ├── auths
    │   ├── __init__.py
    │   └── auths_router.py
    ├── diary
    │   ├── __init__.py
    │   └── diary_router.py
    └── stats
        ├── __init__.py
        └── stats_router.py