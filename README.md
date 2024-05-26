# WordNet for Semantic Roles

## Steps to run the code

- Install pipenv:

    ```bash
    pip install --user pipenv
    ```

- Install dependencies:

    ```bash
    pipenv install
    ```

- Activate the virtual environment:

    ```bash
    pipenv shell
    ```

- Install WordNet from `nltk`:

    ```python
    import nltk
    nltk.download('wordnet')
    ```

- If you are using macOS and you get an SSL error, run the following command:

    ```bash
    bash '/Applications/Python 3.X/Install Certificates.command'
    ```

- Gather verbs:

    ```bash
    python3 gather-verbs.py
    ```

- Get types and frames:

    ```bash
    python3 get-types-frames.py -v verbs.json
    ```

## Note

- Each sense in WordNet is included in only 1 synset. This makes sense since if a sense was included in 2 synsets, those synsets could be merged into 1. This means that one cannot extrapolate semantic roles of several annotated frames into all, or even most of, the senses in WordNet. One must annotate each synset, which is a whole lot of work.
