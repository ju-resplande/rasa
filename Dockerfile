FROM rasa/rasa:3.3.0-full

USER root

RUN python -m spacy download pt_core_news_md
