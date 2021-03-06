import json
import random
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

with open('emoji_map.json', 'r') as f:
    emoji_dict = json.load(f)
    emoji_aliases = dict()
    for emoji in emoji_dict.keys():
        for alias in emoji_dict[emoji]:
            emoji_aliases[alias] = emoji


@app.route('/')
@app.route('/<path:emojicode>')
def show_emoji(emojicode='trophy'):
    if emojicode == 'random':
        emojicode = random.choice(list(emoji_aliases.keys()))
    emojistack = emojicode.split('/')
    if len(emojistack) == 1:
        emojistack.append('octopus')
    for i, emoji in enumerate(emojistack):
        emojistack[i] = emoji_aliases.get(emoji, 'u1f3c6')
    return render_template('index.html', stack=emojistack)


@app.route('/emoji/<filename>')
def emoji_src(filename):
    return send_from_directory('emoji', filename)


if __name__ == '__main__':
    app.debug = True
    app.run()
