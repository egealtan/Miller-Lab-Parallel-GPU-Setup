FROM nvidia/cuda:11.3.0-cudnn8-runtime-ubuntu20.04

ENV SHELL /bin/bash

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get install git &&

COPY ./data_folder /data_folder