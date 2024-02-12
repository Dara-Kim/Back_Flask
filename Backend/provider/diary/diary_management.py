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
