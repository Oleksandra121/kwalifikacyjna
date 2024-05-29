from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

import json
from collections import ChainMap

with open('translations.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

with open('translations_pol.json', 'r', encoding='utf-8') as f:
    pol_translations = json.load(f)

with open('translations_ukr.json', 'r', encoding='utf-8') as f:
    ukr_translations = json.load(f)

combined_translations = dict(ChainMap(translations, pol_translations, ukr_translations))

@app.route('/translate', methods=['POST'])
def translate():
    term = request.form['term'].lower()
    source_lang = request.form['source_lang']
    
    target_term = combined_translations.get(term, "Переклад не знайдено")
    
    return jsonify({'target_term': target_term})

@app.route('/translate', methods=['POST'])
def translate():
    polish_term = request.form['polish_term'].lower()
    ukrainian_term = translations.get(polish_term, "Переклад не знайдено")
    return jsonify({'ukrainian_term': ukrainian_term})

if __name__ == '__main__':
    app.run(debug=True)