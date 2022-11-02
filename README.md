# CPSC-449-project2

    Add your name here

    Team Members:

    Zhiqiang Liu 
    Sam Le


# Initialize the database

cd CPSC449project2/

Under the project directory, type:

./bin/init.sh

If the permission is denied. try:

sh ./bin/init.sh

# Start the API service

foreman start

# Testing API

See http://127.0.0.1:5000/docs

Or

1. Find All user

    GET: curl -v http://localhost:5000/

2. Register

    GET: curl -v "http://localhost:5000/register?username=jacob&password=123456"
    
    POST: curl -X POST -d 'username=jacob' -d 'password=123456' http://localhost:5000/register
    
3. Login(Support GET/POST request)

    GET: curl -v "http://localhost:5000/login?username=jacob&password=123456"
    
    POST: curl -X POST -d 'username=jacob' -d 'password=123456' http://localhost:5000/login

3. Start a new game

    GET: curl -v "http://localhost:5000/startgame?username=jacob"

    Copy the game_id for next step.
4. Guess a word

    GET: curl -v "http://localhost:5000/guess?username=jacob&game_id=1&word=mixed"
    
5. List all game of an user

    GET: curl -v "http://localhost:5000/allgame?username=jacob"

6. Retrieve a game with the game_id

    GET: curl -v "http://localhost:5000/retrievegame?game_id=1"
    
