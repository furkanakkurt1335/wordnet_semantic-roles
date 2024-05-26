import wn

def main():
    en = wn.Wordnet('oewn:2023')

    synsets = en.synsets()
    senses_seen = []
    for synset in synsets:
        senses = synset.senses()
        for sense in senses:
            sense_id = sense.id
            if sense_id in senses_seen:
                print(f'Already seen: {sense_id}') # never printed
            else:
                senses_seen.append(sense_id)

if __name__ == '__main__':
    main()