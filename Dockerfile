#FROM nvidia/cuda:11.3.0-cudnn8-runtime-ubuntu20.04
FROM pytorch/pytorch:latest

#ENV SHELL /bin/bash

COPY requirements.txt ./

RUN apt-get -y install git

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./data_folder /data_folder