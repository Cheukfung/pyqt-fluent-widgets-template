import base64

from Crypto.Cipher import AES

from common.my_logger import my_logger as logger


def pkcs7padding(plaintext, block_size=16):
    text_length = len(plaintext)
    bytes_length = len(plaintext.encode('utf-8'))
    len_plaintext = text_length if (bytes_length == text_length) else bytes_length
    return plaintext + chr(block_size - len_plaintext % block_size) * (block_size - len_plaintext % block_size)


def aes_encrypt(content, key='j2EmvU6yHw8LzKxN', iv='yA3tGqWbVr9nLcPz'):
    padded_data = pkcs7padding(content)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    encrypt_bytes = cipher.encrypt(padded_data.encode('utf-8'))  # 加密
    return str(base64.b64encode(encrypt_bytes), encoding='utf-8')  # 重新编码


def aes_decrypt(content, key='j2EmvU6yHw8LzKxN', iv='yA3tGqWbVr9nLcPz'):
    if content == '':
        return ''
    try:
        cipher = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
        decrypt_bytes = base64.b64decode(content)
        msg = cipher.decrypt(decrypt_bytes)
        return msg[0:-ord(msg[-1:])].decode('utf-8')
    except Exception as e:
        logger.warning('aes解密失败 ' + str(e))
        return ''
