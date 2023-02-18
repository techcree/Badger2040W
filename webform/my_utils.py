#TechCree - ssk start mainscript with webserver and webform
def decode_url(url):
    url = url.replace("+", " ")
    parts = url.split("%")
    decoded = parts[0]
    for part in parts[1:]:
        try:
            code = int(part[:2], 16)
            decoded += chr(code) + part[2:]
        except ValueError:
            decoded += "%" + part
    return decoded
