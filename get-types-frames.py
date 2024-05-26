import json, argparse, random
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser(description='Print types of verbs')
    parser.add_argument('-v', '--verbs', type=str, help='Input file of verbs', required=True)
    parser.add_argument('-c', '--count', type=int, help='Number of verbs to print', default=10)
    return parser.parse_args()

def main():
    args = get_args()
    verb_file = Path(args.verbs)
    with verb_file.open() as f:
        verb_d = json.load(f)

    verb_keys = list(verb_d.keys())
    random.shuffle(verb_keys)
    types = {}
    frames = {}
    for key in verb_keys:
        d = verb_d[key]
        senses = d['senses']
        for sense in senses.values():
            type_t = sense['type']
            if type_t not in types:
                types[type_t] = {'examples': [], 'count': 0}
            if d['lemma'] not in types[type_t]['examples'] and len(types[type_t]['examples']) < args.count:
                types[type_t]['examples'].append(d['lemma'])
            types[type_t]['count'] += 1
            for frame in sense['frames']:
                if frame not in frames:
                    frames[frame] = {'count': 0}
                frames[frame]['count'] += 1

    types = {k: v for k, v in sorted(types.items(), key=lambda item: item[1]['count'], reverse=True)}
    type_file = Path('types.json')
    with type_file.open('w') as f:
        json.dump(types, f, indent=2)

    frames = {k: v for k, v in sorted(frames.items(), key=lambda item: item[1]['count'], reverse=True)}
    frame_file = Path('frames.json')
    with frame_file.open('w') as f:
        json.dump(frames, f, indent=2)

if __name__ == '__main__':
    main()