docker build -t rasa . 
docker run -v $(pwd)/actions:/app/actions --net rasa_net --name action-server rasa/rasa-sdk:3.3.0 -d