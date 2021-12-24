#FROM nvidia/cuda:11.3.0-cudnn8-runtime-ubuntu20.04
#FROM pytorch/pytorch:latest

FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

#ENV SHELL /bin/bash

COPY requirements.txt ./

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

#COPY ./data_folder /data_folder is this needed?