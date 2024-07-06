1) Install Docker Engine
2) Build docker image: docker build -t pygnmi .
3) Modify app.py file
4) Execute this command: docker run -it --rm --network clab -v $(pwd):/usr/src/pygnmi/ --name pygnmi1 pygnmi python ./app.py
Note: Modify this command with the right bridge: --network clab 
