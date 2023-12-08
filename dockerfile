FROM python:3.8-alpine


RUN apk update && apk add \
    git \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev


RUN git clone https://github.com/youchuanyi/the-Impact-of-News-Information-Acquisition-and-Cognition.git


RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

CMD ["/bin/sh"]
