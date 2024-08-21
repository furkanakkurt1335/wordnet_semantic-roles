import argparse, json
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser(description='Extrapolate roles on verbs')
    parser.add_argument('-v', '--verbs', type=str, help='Input file of verbs', required=True)
    parser.add_argument('-a', '--annotations', type=str, help='Input file of annotations', required=True)
    return parser.parse_args()

def get_verb_id(sense_id, verbs):
    for verb_id in verbs:
        verb = verbs[verb_id]
        if sense_id in verb['senses']:
            return verb_id
    return None

def main():
    args = get_args()
    verb_file = Path(args.verbs)
    annotation_file = Path(args.annotations)
    with verb_file.open() as f:
        verbs = json.load(f)
    with annotation_file.open() as f:
        annotations = json.load(f)
    
    sense_stack = list(annotations.keys())
    while sense_stack:
        sense_id = sense_stack.pop()
        sense_annotations = annotations[sense_id]
        sense_frames = sense_annotations['frames']
        verb_id = get_verb_id(sense_id, verbs)
        verb = verbs[verb_id]
        sense = verb['senses'][sense_id]
        synset_senses = sense['synset']['senses']
        synset_senses.remove(sense_id)
        for synset_sense in synset_senses:
            sense_stack.append(synset_sense)
        print(f'Processing sense {sense_id} of verb {verb_id}')
        for frame_string, value in sense_frames.items():
            if frame_string in verb['senses'][sense_id]['frames'] and not verb['senses'][sense_id]['frames'][frame_string]:
                verbs[verb_id]['senses'][sense_id]['frames'][frame_string] = value
                for synset_sense in synset_senses:
                    if synset_sense not in annotations:
                        annotations[synset_sense] = {'frames': {}}
                    else:
                        annotations[synset_sense]['frames'][frame_string] = value

    with verb_file.open('w') as f:
        json.dump(verbs, f, indent=4)

if __name__ == '__main__':
    main()