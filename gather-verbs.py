import wn, json
from pathlib import Path

def main():
    en = wn.Wordnet('oewn:2023')

    words = en.words()
    verb_d = {}
    for word in words:
        if word.pos == 'v':
            lemma = word.lemma()
            d = {'lemma': lemma, 'senses': {}}
            senses = word.senses()
            for sense in senses:
                sense_id = sense.id
                synset = sense.synset()
                synset_id = synset.id
                synset_senses = [sense.id for sense in synset.senses()]
                words = synset.words()
                type_t = synset.lexfile()
                frames = sense.frames()
                frame_d = {}
                for frame in frames:
                    frame_d[frame] = {}
                examples = synset.examples()
                definition = synset.definition()
                d['senses'][sense_id] = {'synset': {'id': synset_id, 'senses': synset_senses}, 'frames': frame_d, 'type': type_t, 'examples': examples, 'definition': definition}
            verb_d[word.id] = d

    verb_file = Path('verbs.json')
    with verb_file.open('w') as f:
        json.dump(verb_d, f, indent=2)

if __name__ == '__main__':
    main()