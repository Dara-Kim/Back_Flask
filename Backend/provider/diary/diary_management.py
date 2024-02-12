from werkzeug.utils import secure_filename


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
