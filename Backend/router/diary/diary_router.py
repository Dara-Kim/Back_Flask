from flask import Blueprint, request, jsonify
from provider.diary.diary_management import writing_parent_diary, choosing_parent_diary
from provider.diary.diary_management import writing_child_diary, choosing_child_diary

diary_router = Blueprint("/home", __name__)


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


@diary_router.route(f"/home/parent/<int:pdid>", methods=["GET"])
def handle_choosing_parent_diary(pdid):
    date = request.json.get("date")

    (
        correctedText,
        translatedText,
        imageUrl,
        characterUrl_parent,
        characterUrl_child,
    ) = choosing_parent_diary(date, pdid)
    return jsonify(
        {
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
            "characterUrl_parent": characterUrl_parent,
            "characterUrl_child": characterUrl_child,
        }
    )


@diary_router.route(f"/home/child/<int:cdid>", methods=["GET"])
def handle_choosing_child_diary(cdid):
    date = request.json.get("date")

    (
        correctedText,
        translatedText,
        imageUrl,
        characterUrl_parent,
        characterUrl_child,
    ) = choosing_child_diary(date, cdid)
    return jsonify(
        {
            "correctedText": correctedText,
            "translatedText": translatedText,
            "imageUrl": imageUrl,
            "characterUrl_parent": characterUrl_parent,
            "characterUrl_child": characterUrl_child,
        }
    )
