import JishoAPI from 'unofficial-jisho-api';

const jisho = new JishoAPI();

function searchForPhrase(phrase) {
    return jisho.searchForPhrase(phrase);
}

function searchForKanji(kanji) {
    let kanji = jisho.searchForKanji(kanji);
    return kanji;
}

let kanjis = [];

for (kanji in kanjis) {
    kanji = searchForKanji(kanji);
    console.log(kanji);
}