from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from model import PARENTDIARY, PROFILE, CHILDDIARY
import databaseConfig, model
from sqlalchemy.sql import extract

# mysql database 연결 #
engine = create_engine(databaseConfig.getURI(), encoding="utf-8")
model.init_db(engine)

# mysql database와 데이터를 주고받을 통신 연결 #
Session = sessionmaker(engine)
session = Session()
session.commit()
print("-----session commit complete -----")


# ----- Database에서 데이터 통신 -----#

# example
profile1 = session.query(PROFILE).first()
print(profile1.ID)


# -- Get(DB에서 값을 불러오는) 함수 --#


# 특정 일자 부모 일기 가져오기
# 홈 화면, 소통하기 화면, 통계 일일 리포트에서 제공
def get_parent_diary(pid, date):
    parDiary = (
        session.query(PARENTDIARY)
        .filter(and_(PARENTDIARY.id_profile == pid, PARENTDIARY.pd_date == date))
        .first()
    )
    return parDiary


# 특정 일자 아이 일기 가져오기
# 홈 화면, 소통하기 화면, 통계 일일 리포트에서 제공
def get_child_diary(pid, date):
    chiDiary = (
        session.query(CHILDDIARY)
        .filter(and_(CHILDDIARY.id_profile == pid, PARENTDIARY.pd_date == date))
        .first()
    )
    return chiDiary


# 한달 기준 일기 작성된 일자 불러오기
# 홈 화면에서 제공
def get_date(pid, date):
    month = date.month
    date_list = (
        session.query(PARENTDIARY.pd_date)
        .filter(extract("month", PARENTDIARY.pd_date) == month)
        .all()
    )
    return date_list


# 사용자 정보 불러오기
# 설정 화면에서 제공
def get_profile(pid):
    user_profile = session.query(PROFILE).filter(PROFILE.id_profile == pid).first()
    return user_profile


# 최근 7개 부모 일기 통계 불러오기
# 통계 최근 7개 리포트에서 제공
def get_recent7_parent_diary():
    return


# 최근 7개 아이 일기 통계 불러오기
# 통계 최근 7개 리포트에서 제공
def get_recent7_child_diary():
    return


# 최근 30개 부모 일기 통계 불러오기
# 통계 최근 30개 리포트에서 제공
def recent30_parent_diary():
    return


# 최근 30개 아이 일기 통계 불러오기
# 통계 최근 30개 리포트에서 제공
def recent30_child_diary():
    return


# -- Set(DB에 값을 집어넣는) 함수 --#


# 사용자 정보 저장
def set_profile(
    pid, id, pw, pname, page, pcountry, pgender, pnumber, cname, cage, cgender
):
    profile = PROFILE(
        id_profile=pid,
        ID=id,
        Password=pw,
        pName=pname,
        pAge=page,
        pCountry=pcountry,
        pGender=pgender,
        pNumber=pnumber,
        cName=cname,
        cAge=cage,
        cgender=cgender,
    )
    session.add(profile)
    session.commit()


# 부모 다이어리 저장
def set_parent_diary(
    pid,
    date,
    text,
    corrected_text,
    translated_text,
    image,
    char_image,
    langRatio,
    correct_ratio,
):
    pDiary = PARENTDIARY(
        id_profile=pid,
        pd_date=date,
        pd_text=text,
        pd_corrected=corrected_text,
        pd_translated=translated_text,
        pd_imageURL=image,
        pd_charURL=char_image,
        pd_langRatio=langRatio,
        pd_correctRatio=correct_ratio,
    )
    session.add(pDiary)
    session.commit()


# 아이 다이어리 저장
def set_child_diary(
    pid,
    date,
    corrected_text,
    translated_text,
    image,
    char_image,
    correct_ratio,
    mood_ratio,
):
    cDiary = CHILDDIARY(
        id_profile=pid,
        dc_date=date,
        cd_corrected=corrected_text,
        cd_translated=translated_text,
        cd_imgURL=image,
        cd_charURL=char_image,
        cd_correctRatio=correct_ratio,
        cd_mood=mood_ratio,
    )
    session.add(cDiary)
    session.commit()
