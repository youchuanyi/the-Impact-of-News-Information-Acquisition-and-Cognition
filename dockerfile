FROM alpine:latest
RUN apk update && apk add git python3
RUN git clone https://github.com/youchuanyi/the-Impact-of-News-Information-Acquisition-and-Cognition.git

CMD ["/bin/sh"]
