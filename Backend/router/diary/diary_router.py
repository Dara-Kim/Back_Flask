# from flask import Blueprint, request, jsonify
# from provider.diary.diary_management import writing_parent_diary

# diary_router = Blueprint('/home', __name__)


# @diary_router.route('/home/parent', methods=['POST'])
# def handle_writing_parent_diary():
#     # Extracting pId, text and image from request
#     pid = request.json.get('pid')
#     text = request.json.get('text')
#     image = request.files.get('image')
#     # Calling function "writing_parent_diary"
#     correctedText, translatedText, imageUrl = \
#         writing_parent_diary(pid, text, image)
#     return jsonify({
#         "correctedText": correctedText,
#         "translatedText": translatedText,
#         "imageUrl": imageUrl
#         })
