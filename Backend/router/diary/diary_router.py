from flask import Blueprint, request, jsonify
from provider.diary.diary_management import writing_parent_diary
from provider.diary.diary_management import writing_child_diary

from werkzeug.utils import secure_filename
import os

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
