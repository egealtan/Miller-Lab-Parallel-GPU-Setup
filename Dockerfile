FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

COPY requirements.txt ./

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt