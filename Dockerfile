#FROM pure/python:3.7-cuda10.2-cudnn7-runtime
FROM python:3.7.13-buster

WORKDIR /frameBERT

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader popular wordnet averaged_perceptron_tagger omw-1.4
RUN git clone https://github.com/machinereading/koreanframenet.git
RUN gdown https://drive.google.com/drive/folders/1bDUoIniUNUm2I0ztXWo6hitOpLmU9lv4 -O ./en --folder

EXPOSE 5000
CMD ["python", "api.py"]
