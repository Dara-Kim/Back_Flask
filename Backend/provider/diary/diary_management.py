from flask import jsonify
from datetime import datetime


class DiaryService:
    def __init__(self, date, pid):
        self.date = date
        self.pid = pid

    # @가경 db check
    def get_complete_list(self, date, pid):
        completeListStr = [
            "2024-01-01",
            "2024-01-05",
            "2024-01-10",
            "2024-01-20",
            "2024-01-24",
        ]
        completeList = [
            datetime.strptime(date_str, "%Y-%m-%d") for date_str in completeListStr
        ]

        return completeList

    # @가경 db check
    def get_parent_diary_preview(self, date, pid):
        pdid = "1111111"
        correctedText = "티비를 봤다. 베트남 이야기가 나와서 그리웠다."
        translatedText = "~~~vietnamese~~~"
        imageUrl = "https://s3.us-west-2.amazonaws.com/BUCKET1/.picturejpg"

        return {
            "pdid": pdid,
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
        }

    # @가경 db check
    def get_child_diary_preview(self, date, pid):
        cdid = 1
        correctedText = "동시를 했다. 동시를 조금 외웠다. 재밌었다."
        translatedText = "~~~vietnamese~~~"
        imageUrl = "https://s3.us-west-2.amazonaws.com/BUCKET1/picture1.jpg"

        return {
            "cdid": cdid,
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
        }

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


# @가경 db check
def choosing_parent_diary(date, pdid):
    correctedText = f"correctedText/{date}/{pdid}"
    translatedText = f"translatedText/{date}/{pdid}"
    imageUrl = f"http://yourserver.com/imageUrl/{date}/{pdid}"
    characterUrl_parent = f"http://yourserver.com/characterUrl_parent/{date}/{pdid}"
    characterUrl_child = f"http://yourserver.com/characterUrl_child/{date}/{pdid}"

    return (
        correctedText,
        translatedText,
        imageUrl,
        characterUrl_parent,
        characterUrl_child,
    )


# @가경 db check
def choosing_child_diary(date, cdid):
    correctedText = f"correctedText/{date}/{cdid}"
    translatedText = f"translatedText/{date}/{cdid}"
    imageUrl = f"http://yourserver.com/imageUrl/{date}/{cdid}"
    characterUrl_parent = f"http://yourserver.com/characterUrl_parent/{date}/{cdid}"
    characterUrl_child = f"http://yourserver.com/characterUrl_child/{date}/{cdid}"

    return (
        correctedText,
        translatedText,
        imageUrl,
        characterUrl_parent,
        characterUrl_child,
    )
