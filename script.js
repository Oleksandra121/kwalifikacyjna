async function translateTerm() {
    const term = document.getElementById('termInput').value.toLowerCase();
    const languageSelect = document.getElementById('languageSelect').value;
    const response = await fetch('dictionary.json');
    const dictionary = await response.json();

    let translation;
    if (languageSelect === 'uk-pl') {
        translation = dictionary[term];
    } else if (languageSelect === 'pl-uk') {
        translation = Object.keys(dictionary).find(key => dictionary[key].toLowerCase() === term);
    }

    const translationElement = document.getElementById('translation');
    if (translation) {
        translationElement.innerHTML = languageSelect === 'uk-pl'
            ? `${translation}`
            : `${translation}`;
    } else {
        translationElement.textContent = 'Переклад не знайдено';
    }
}

/*? `Польський переклад: <span class="highlight">${translation}</span>`
            : `Український переклад: <span class="highlight">${translation}</span>`;*/