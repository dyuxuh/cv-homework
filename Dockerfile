FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-lang-cyrillic \
    texlive-science \
    cm-super \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /cv

COPY . .

RUN pdflatex -interaction=nonstopmode main.tex
RUN pdflatex -interaction=nonstopmode main.tex

CMD ["bash"]