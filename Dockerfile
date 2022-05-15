FROM python:3.9.12-slim-buster as builder

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get -y install binutils
RUN pip3 install -r requirements.txt
COPY . .
RUN pyinstaller run.py --onefile

FROM ubuntu:21.04
COPY --from=builder /app/dist/run .
# Copy this to binary for usage
ENTRYPOINT [ "/app/dist/run" ]
