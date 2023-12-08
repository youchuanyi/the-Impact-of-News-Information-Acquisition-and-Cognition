FROM python:3.8
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libffi-dev \
 && rm -rf /var/lib/apt/lists/*


RUN git clone https://github.com/youchuanyi/the-Impact-of-News-Information-Acquisition-and-Cognition.git

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"


RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.org/simple


RUN pip install --no-cache-dir -r the-Impact-of-News-Information-Acquisition-and-Cognition/requirements.txt

CMD ["/bin/sh"]
