import base64

def encrypt(password, guid):
    text = password+guid
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def decrypt(password):
    decoded_bytes = base64.b64decode(password.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text