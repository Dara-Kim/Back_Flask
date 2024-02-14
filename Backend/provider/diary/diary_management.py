from flask import jsonify
from datetime import datetime


class DiaryService:
    def __init__(self, date, pid):
        self.date = date
        self.pid = pid

    def get_complete_list(self, date, pid):
        # db check
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

    def get_parent_diary_preview(self, date, pid):
        # db check
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

    def get_child_diary_preview(self, date, pid):
        # db check
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


def writing_parent_diary(pid, text, image):
    # imageUrl = f'http://yourserver.com/{filename}'
    root = "./Backend/provider/diary/tmp_s3/"
    imageUrl = root + image.filename
    image.save(imageUrl)

    # diary correcting api
    correctedText = "correctedText"

    # diary translating api
    translatedText = "translatedText"

    return correctedText, translatedText, imageUrl


def writing_child_diary(pid, image):
    # imageUrl = f'http://yourserver.com/{filename}'
    root = "./Backend/provider/diary/tmp_s3/"
    imageUrl = root + image.filename
    image.save(imageUrl)

    # diary correcting api
    correctedText = "correctedText"

    # diary translating api
    translatedText = "translatedText"

    return correctedText, translatedText, imageUrl


def choosing_parent_diary(date, pdid):
    # db check
    correctedText = f"correctedText/{date}/{pdid}"

    # db check
    translatedText = f"translatedText/{date}/{pdid}"

    # db check
    imageUrl = f"http://yourserver.com/imageUrl/{date}/{pdid}"

    # db check
    characterUrl_parent = f"http://yourserver.com/characterUrl_parent/{date}/{pdid}"

    # db check
    characterUrl_child = f"http://yourserver.com/characterUrl_child/{date}/{pdid}"

    return (
        correctedText,
        translatedText,
        imageUrl,
        characterUrl_parent,
        characterUrl_child,
    )


def choosing_child_diary(date, cdid):
    # db check
    correctedText = f"correctedText/{date}/{cdid}"

    # db check
    translatedText = f"translatedText/{date}/{cdid}"

    # db check
    imageUrl = f"http://yourserver.com/imageUrl/{date}/{cdid}"

    # db check
    characterUrl_parent = f"http://yourserver.com/characterUrl_parent/{date}/{cdid}"

    # db check
    characterUrl_child = f"http://yourserver.com/characterUrl_child/{date}/{cdid}"

    return (
        correctedText,
        translatedText,
        imageUrl,
        characterUrl_parent,
        characterUrl_child,
    )
