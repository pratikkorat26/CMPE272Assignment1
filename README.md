<<<<<<< HEAD
# CMPE272Assignment1
=======
# Assignment 1 : Hello World from MicroServices
## Author : Pratikkumar Dalsukhbhai Korat
### SJSU ID : 017512508

## How to Run Applications individually

### 1. appHello Application
> 1. Move into directory apphello/
> 2. open CMD and run following command "pip install -r requirements.txt"
> 3. run following command "python main.py"
> 4. Application will be live on localhost and port number 5000 "http://localhost:5000/hello"

### 1. appWorld Application
> 1. Move into directory appworld/
> 2. open CMD and run following command "pip install -r requirements.txt"
> 3. run following command "python main.py"
> 4. Application will be live on localhost and port number 6001 "http://localhost:6001/hello"


### Docker Images Built Using this Applications
> * apphello application docker image
>   * pratikkorat/flask-hello-app 

> * appworld application docker image
>   * pratikkorat/flask-world-app
 

> 1. To run and pull apphello application using docker image, run following commands
>    1. "docker pull pratikkorat/flask-hello-app"
>    2. "docker run -p 5000:5000 pratikkorat/flask-hello-app"
>    3. open "http://localhost:5000/hello"
 

> 2. To pull appworld docker image,run following command
>    * "docker pull pratikkorat/flask-world-app"
>    * "docker run -p 6001:6001 pratikkorat/flask-world-app"
>    * open "http://localhost:6001/world"
>>>>>>> master
