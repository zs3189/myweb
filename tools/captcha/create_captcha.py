##构建素材
import random
from os.path import join, exists
import pickle
import numpy as np
from os import makedirs

from PIL import Image
from captcha.image import ImageCaptcha
import numpy as np

VOCAB = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CAPTCHA_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)

DATA_LENGTH = 10000
DATA_PATH = 'data'


def generate_captcha(captcha_text):
    """
    get captcha text and np array
    :param captcha_text: source text
    :return: captcha image and array
    """
    image = ImageCaptcha()
    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_array = np.array(captcha_image)
    return captcha_array

##text2vec() 方法就是将真实文本转化为 One-Hot 编码，vec2text() 方法就是将 One-Hot 编码转回真实文本
def text2vec(text):
    """
    text to one-hot vector
    :param text: source text
    :return: np array
    """
    if len(text) > CAPTCHA_LENGTH:
        return False
    vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
    for i, c in enumerate(text):
        index = i * VOCAB_LENGTH + VOCAB.index(c)
        vector[index] = 1
    return vector


def vec2text(vector):
    """
    vector to captcha text
    :param vector: np array
    :return: text
    """
    if not isinstance(vector, np.ndarray):
        vector = np.asarray(vector)
    vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])
    text = ''
    for item in vector:
        text += VOCAB[np.argmax(item)]
    return text



def get_random_text():
    text = ''
    for i in range(CAPTCHA_LENGTH):
        text += random.choice(VOCAB)
    return text

def generate_data():
    print('Generating Data...')
    data_x, data_y = [], []

    # generate data x and y
    for i in range(DATA_LENGTH):
        text = get_random_text()
        # get captcha array
        captcha_array = generate_captcha(text)
        # get vector
        vector = text2vec(text)
        data_x.append(captcha_array)
        data_y.append(vector)

    # write data to pickle
    if not exists(DATA_PATH):
        makedirs(DATA_PATH)

    x = np.asarray(data_x, np.float32)
    y = np.asarray(data_y, np.float32)
    with open(join(DATA_PATH, 'data.pkl'), 'wb') as f:
        pickle.dump(x, f)
        pickle.dump(y, f)