def create_response(sentence, name):
    msg = {}
    if name != "Lunar Bot":
        if "no" in sentence:
            msg = "no u"
    return msg
