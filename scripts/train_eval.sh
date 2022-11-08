#!/bin/bash
EXPERIMENT_NAME=$1

sudo rm -rf results/${EXPERIMENT_NAME}
sudo rm -rf models/${EXPERIMENT_NAME}.tar.gz

docker run -it -v $(pwd):/app --net rasa_net rasa train --fixed-model-name ${EXPERIMENT_NAME}
docker run -it -v $(pwd):/app --net rasa_net rasa test --out results/${EXPERIMENT_NAME}
cp config.yml results/${EXPERIMENT_NAME}