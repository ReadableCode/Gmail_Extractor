# Gmail_Extractor

## Running with pipenv

* Install dependencies for system:

  Linux:

    ```bash
    pip install pipenv
    ```

  Windows:

    In powershell as admin:

    ```bash
    pip install pipenv
    ```
  
    On Windows you may need to add the path to pipenv to your PATH environment variable, it will be printed at the end of the install command most likely

* To install dependencies:

  ```bash
  pipenv install
  ```

  To run:

  ```bash
  pipenv run python src/gmail_search_extractor.py
  ```

* To make changes to requirements.txt, change the file and then:

  ```bash
  pipenv --rm
  rm Pipfile.lock
  rm Pipfile
  pipenv install # to use the new requirements.txt
  ```

* To enter bash in the virtual environment:

  ```bash
  pipenv shell
  ```

* To Activate or Source the environment and not have to prepend each command with pipenv:

  On Linux:

  ```bash
  source $(pipenv --venv)/bin/activate
  ```
  
  On Windows (Powershell):

  ```bash
  & "$(pipenv --venv)\Scripts\activate.ps1"
  ```

* To Deactivate:

  ```bash
  deactivate
  ```

## Running with docker

To Build and run the docker image:

```bash
docker build -t gmail_extractor .
docker run -it gmail_extractor /bin/bash
```

To run tests:

```bash
cd tests
pytest # include name of test_file.py to run specific test
```

To exit:

```bash
exit
```
