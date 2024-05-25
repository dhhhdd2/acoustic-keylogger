__all__ = ["audio_processing",]

from acoustic_keylogger.audio_processing import *
from acoustic_keylogger.unsupervised import *
from sklearn.preprocessing import MinMaxScaler

data = wav_read("音乐.wav")


keystrokes = detect_keystrokes(data)

X = [extract_features(x) for x in keystrokes]
X_norm = MinMaxScaler().fit_transform(X)

letters = {}
phrase = []
current_letter = ord('a')
for x in X_norm:
    if x[0] not in letters:
        letters[x[0]] = current_letter
        current_letter += 1
    phrase.append(letters[x[0]])

flag_encoded = "".join([chr(x) for x in phrase])

print(flag_encoded)

mappings = {
    'a': '4',
    'b': '9',
    'c': '5',
    'd': '3',
    'h': '8',
    'e': '7',
    'n': 'e',
    'i': 'f',
    'g': '6',
    'f': 'b',
    'j': 'c',
    'k': '2',
    'l': '1',
    'm': 'd',
}
flag_hex = "".join(mappings.get(char, '?') for char in flag_encoded)
print(flag_hex)
flag = bytes.fromhex(flag_hex).decode('utf-8')
# if flag.endswith('}') and '|' not in flag and '`' not in flag:
#     print(flag)
print(flag)
