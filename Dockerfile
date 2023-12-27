FROM --platform=linux/amd64 python:3.10.12

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /Gmail_Extractor
COPY . /Gmail_Extractor

# Create an alias for 'll' as 'ls -al'
RUN echo 'alias ll="ls -al"' >> /root/.bashrc && echo 'alias ll="ls -al"' > /root/.bash_aliases

CMD ["python"]
