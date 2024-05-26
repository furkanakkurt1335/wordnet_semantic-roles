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
