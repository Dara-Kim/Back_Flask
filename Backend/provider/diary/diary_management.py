from flask import jsonify
from datetime import datetime
from model.model import PARENTDIARY, PROFILE, CHILDDIARY
import model.__init__ as db


class DiaryService:
    def __init__(self, date, pid):
        self.date = date
        self.pid = pid

    # /home
    # 한달 기준 일기 작성된 일자 불러오기
    # 제공 화면: 홈 화면
    def get_complete_list(self, date, pid):
        trans_date = datetime.strptime(date, "%Y-%m-%d")
        completeList = db.get_date(pid, trans_date)
        return completeList  # list(datetime)

    # /home/conversation
    # 특정 일자 부모 일기 가져오기
    # 제공 화면: 소통 화면(부모 일기 보기)
    def choosing_parent_diary(self, date, pid):
        parent_diary = db.get_parent_diary(pid, date)
        correctedText = parent_diary.pd_corrected
        translatedText = parent_diary.pd_translated
        imageUrl = parent_diary.pd_imageURL
        characterUrl_parent = parent_diary.pd_charURL

        return (
            correctedText,  # string
            translatedText,  # string
            imageUrl,  # string
            characterUrl_parent,  # string
        )

    # /home/conversation
    # 특정 일자 아이 일기 가져오기
    # 제공 화면: 소통 화면(아이 일기 보기)
    def choosing_child_diary(date, pid):
        child_diary = db.get_child_diary(pid, date)
        correctedText = child_diary.cd_corrected
        translatedText = child_diary.cd_translated
        imageUrl = child_diary.cd_imageURL
        characterUrl_child = child_diary.cd_charURL

        return (
            correctedText,  # string
            translatedText,  # string
            imageUrl,  # string
            characterUrl_child,  # string
        )

    # /home
    # 특정 일자 아이 일기 미리보기 가져오기
    # 제공 화면: 홈 화면(아이 일기 보기)
    # def get_parent_diary_preview(self, date, pid):
    #     # pdid = "1111111"
    #     # correctedText = "티비를 봤다. 베트남 이야기가 나와서 그리웠다."
    #     # translatedText = "~~~vietnamese~~~"
    #     # imageUrl = "https://s3.us-west-2.amazonaws.com/BUCKET1/.picturejpg"

    #     return {
    #         "pdid": pid,
    #         "correctedText": correctedText,
    #         "translatedText": translatedText,
    #         "imageUrl": imageUrl,
    #     }

    # # @가경 db check
    # def get_child_diary_preview(self, date, pid):
    #     # cdid = 1
    #     # correctedText = "동시를 했다. 동시를 조금 외웠다. 재밌었다."
    #     # translatedText = "~~~vietnamese~~~"
    #     # imageUrl = "https://s3.us-west-2.amazonaws.com/BUCKET1/picture1.jpg"

    #     return {
    #         "cdid": cdid,
    #         "correctedText": correctedText,
    #         "translatedText": translatedText,
    #         "imageUrl": imageUrl,
    #     }

    # def result_code(self):
    #     isSuccess =
    #     code =
    #     message =


# @가경 db Create
def writing_parent_diary(pid, today, text, image):
    # imageUrl = f'http://yourserver.com/{filename}'
    root = "./Backend/provider/diary/tmp_s3/"
    imageUrl = root + image.filename
    image.save(imageUrl)

    # @ 무너 api
    correctedText = "correctedText"
    translatedText = "translatedText"

    return correctedText, translatedText, imageUrl


# @가경 db Create
def writing_child_diary(pid, today, image):
    # imageUrl = f'http://yourserver.com/{filename}'
    root = "./Backend/provider/diary/tmp_s3/"
    imageUrl = root + image.filename
    image.save(imageUrl)

    # @ 무너 api
    correctedText = "correctedText"
    translatedText = "translatedText"

    return correctedText, translatedText, imageUrl


s
