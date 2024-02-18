from flask import jsonify
from datetime import datetime
from model.model import PARENTDIARY, PROFILE, CHILDDIARY
import model.__init__ as db

db.init_db()


# ----- Class 선언부 ----- #
# DiaryService - 홈 화면 관련 호출 함수
class DiaryService:
    """
    get_complete_list()
    get_parent_diary_preview()
    get_child_diary_preview()
    """

    def __init__(self, date, pid):
        self.date = date
        self.pid = pid

    # (GET) /home
    # 한달 기준 일기 작성된 일자 불러오기
    # 제공 화면: 홈 화면(달력)
    def get_complete_list(self, date, pid):
        # trans_date = date.date()
        complist = []
        completeList = db.get_date(pid, date)
        for i in completeList:
            complist.append(i.pd_date)
        return complist  # list(datetime)

    # (GET) /home
    # 특정 일자 부모 일기 미리보기 가져오기
    # 제공 화면: 홈 화면(부모 일기 미리보기 칸)
    def get_parent_diary_preview(self, date, pid):
        parent_diary = db.get_parent_diary(pid, date)
        correctedText = parent_diary.pd_corrected
        translatedText = parent_diary.pd_translated
        imageUrl = parent_diary.pd_imageURL

        return {
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
        }

    # (GET) /home
    # 특정 일자 아이 일기 미리보기 가져오기
    # 제공 화면: 홈 화면(아이 일기 미리보기 칸)
    def get_child_diary_preview(self, date, pid):
        child_diary = db.get_child_diary(pid, date)
        correctedText = child_diary.cd_corrected
        translatedText = child_diary.cd_translated
        imageUrl = child_diary.cd_imageURL

        return {
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
        }

    # def result_code(self):
    #     isSuccess =
    #     code =
    #     message =


# ----- 기타 함수 호출부 ----- #


#  1. 소통화면 관련 함수  #
# (GET) /home/conversation
# 특정 일자 부모 일기 가져오기
# 제공 화면: 소통 화면(부모 일기 보기 칸)
def choosing_parent_diary(date, pid):
    # date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    parent_diary = db.get_parent_diary(pid, date)
    correctedText = parent_diary.pd_corrected
    translatedText = parent_diary.pd_translated
    imageUrl = parent_diary.pd_imageURL
    characterUrl_parent = parent_diary.pd_charURL
    question_parent = parent_diary.pd_question

    return {
        "correctedText": correctedText,
        "translatedText": translatedText,
        "imageUrl": imageUrl,
        "characterUrl": characterUrl_parent,
        "question": question_parent,
    }


# (GET) /home/conversation
# 특정 일자 아이 일기 가져오기
# 제공 화면: 소통 화면(아이 일기 보기 칸)
def choosing_child_diary(date, pid):
    # date = datetime.strptime(date_string, "%Y-%m-%d")
    child_diary = db.get_child_diary(pid, date)
    correctedText = child_diary.cd_corrected
    translatedText = child_diary.cd_translated
    imageUrl = child_diary.cd_imageURL
    characterUrl_child = child_diary.cd_charURL
    qusetion_child = child_diary.cd_question

    return {
        "correctedText": correctedText,  # string
        "translatedText": translatedText,  # string
        "imageUrl": imageUrl,  # string
        "characterUrl": characterUrl_child,
        "question": qusetion_child,
    }


#  2. 일기 작성 관련  #
# (POST) /home/parent
# 부모 일기 작성
# 제공 화면: 부모 일기 작성 화면
def writing_parent_diary(pid, text, image):
    date = datetime.now().date()
    imageUrl = "imgurl"
    # --- 이미지 저장 부분 임시 코드 --- #
    # imageUrl = f'http://yourserver.com/{filename}'
    # root = "./Backend/provider/diary/tmp_s3/"
    # imageUrl = root + image.filename
    # image.save(imageUrl)
    # --- #

    # @ 무너 api
    correctedText = "correctedText"
    translatedText = "translatedText"
    charImgUrl = "charImgUrl"
    corretRatio = 33
    langRatio = 3
    question = "parent_qusetion"

    db.set_parent_diary(
        pid,
        date,
        text,
        correctedText,
        translatedText,
        imageUrl,
        charImgUrl,
        langRatio,
        corretRatio,
        question,
    )

    return correctedText, translatedText, imageUrl


# (POST) /home/child
# 아이 일기 작성
# 제공 화면: 부모 일기 작성 화면
def writing_child_diary(pid, image):
    date = datetime.now().date()
    imageUrl = "imgurl"
    # --- 이미지 저장 부분 임시 코드 --- #
    # imageUrl = f'http://yourserver.com/{filename}'
    # root = "./Backend/provider/diary/tmp_s3/"
    # imageUrl = root + image.filename
    # image.save(imageUrl)
    # --- #

    # @ 무너 api
    correctedText = "correctedText"
    translatedText = "translatedText"
    charImgUrl = "charImgUrl"
    corretRatio = 22
    moodRatio = 2
    question = "child_question"

    db.set_child_diary(
        pid,
        date,
        correctedText,
        translatedText,
        imageUrl,
        charImgUrl,
        corretRatio,
        moodRatio,
        question,
    )

    return correctedText, translatedText, imageUrl
