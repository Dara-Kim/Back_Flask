from flask import Blueprint, request, jsonify
from datetime import datetime
from provider.diary.diary_management import (
    DiaryService,
    writing_parent_diary,
    choosing_parent_diary,
    writing_child_diary,
    choosing_child_diary,
)

diary_router = Blueprint("/home", __name__)


# 홈 화면
@diary_router.route("/home", methods=["GET"])
def DiaryService_displaying_home():
    pid = request.form.get("pid")
    date = datetime.now().date()
    Diary = DiaryService(date, pid)
    completeList = Diary.get_complete_list(date, pid)
    parentDto = Diary.get_parent_diary_preview(date, pid)
    childDto = Diary.get_child_diary_preview(date, pid)

    # print(type(completeList))
    # print(type(parentDto))
    # print(type(childDto))

    return jsonify(
        {
            "completeList": completeList,
            "get_parent_diary_preview": parentDto,
            "get_child_diary_preview": childDto,
        }
    )


# 부모 일기 작성 화면
@diary_router.route("/home/parent", methods=["POST"])
def handle_writing_parent_diary():
    # Extracting pId, text and image from request
    pid = request.form.get("pid")
    text = request.form.get("text")
    image = request.files["image"]

    # Calling function "writing_parent_diary"
    correctedText, translatedText, imageUrl = writing_parent_diary(pid, text, image)
    return jsonify(
        {
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
        }
    )


# 아이 일기 작성 화면
@diary_router.route("/home/child", methods=["POST"])
def handle_writing_child_diary():
    # Extracting pId, text and image from request
    pid = request.form.get("pid")
    image = request.files["image"]

    # Calling function "writing_child_diary"
    correctedText, translatedText, imageUrl = writing_child_diary(pid, image)
    return jsonify(
        {
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
        }
    )


# 소통하기 화면
@diary_router.route(f"/home/conversation", methods=["GET"])
def handle_choosing_parent_diary():
    pid = request.form.get("pid")
    date = request.form.get("date")

    date = datetime.strptime(date, "%Y-%m-%d")
    parent_diary = choosing_parent_diary(date, pid)
    child_diary = choosing_child_diary(date, pid)

    return jsonify(
        {
            "hi": "hi"
            # "parent_diary": parent_diary,
            # "child_diary": child_diary
        }
    )


# 통합중
# @diary_router.route(f"/home/child/<int:cdid>", methods=["GET"])
# def handle_choosing_child_diary(cdid):
#     date = request.json.get("date")

#     (
#         correctedText,
#         translatedText,
#         imageUrl,
#         characterUrl_parent,
#         characterUrl_child,
#     ) = choosing_child_diary(date, cdid)
#     return jsonify(
#         {
#             "correctedText": correctedText,
#             "translatedText": translatedText,
#             "imageUrl": imageUrl,
#             "characterUrl_parent": characterUrl_parent,
#             "characterUrl_child": characterUrl_child,
#         }
#     )
