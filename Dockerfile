FROM pytorch/pytorch:latest

ENV SHELL /bin/bash

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .