import JishoAPI from 'unofficial-jisho-api';

const jisho = new JishoAPI();

function searchForPhrase(phrase) {
    var result = jisho.searchForPhrase(phrase);
    console.log(result);
    if (result.meta.status != 200) {
        console.log("Error: " + result.meta.status);
    }

    let phraseResults = result.data;

    for (var i=0;i<phraseResults.length;i++) {
        var phrase = phraseResults[i];
        if (phrase.slug === word) {
            var exactMatch = True;
        }
    }

    if (exactMatch) {

    }

    if (phraseResults[0].slug === word) {
        console.log("Phrase found!");
    } else if (phraseResults[0].slug in word) {
        console.log("Word found!");
    } else {
        console.log("No results found.");
    }
};

function searchForKanji(kanji) {
    kanji = jisho.searchForKanji(kanji);
    return kanji;
};

let word = "日本語";
let japanese = searchForKanji(word)
let english = searchForPhrase("日本に行く")