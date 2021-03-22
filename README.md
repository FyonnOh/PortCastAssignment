# FastApi with postgresql
This application is built with FASTApi with a postgredsql database.
It allows users to store containers' information and its associated transshipments details.

## Setup
Set up a virtual environment and install the requirements:
```shell
$ python3.6 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then you can run it with Uvicorn:
```shell
$ uvicorn portcast.main:app --reload
```
if Uvicorn is not installed, run
"pip install uvicorn"

And then, you can open your browser at http://127.0.0.1:8000/docs  
And you will be able to interact with your FastAPI application, reading data from a real database:  
<img width="1425" alt="Screenshot 2021-03-22 at 7 41 48 PM" src="https://user-images.githubusercontent.com/59982275/111984683-a5c42980-8b46-11eb-85d2-8521e5a1f2c8.png">

Below shows some examples on how to send API calls to the application via postman.  

*CREATE A CONTAINER*\
<img width="1347" alt="Screenshot 2021-03-22 at 7 20 42 PM" src="https://user-images.githubusercontent.com/59982275/111984855-e1f78a00-8b46-11eb-9ac1-46c9c93c3474.png">

*GET A CONTAINER*\
<img width="1348" alt="Screenshot 2021-03-22 at 7 20 51 PM" src="https://user-images.githubusercontent.com/59982275/111984917-f2a80000-8b46-11eb-8e42-61cacbc17e8f.png">

*CREATE A TRANSSHIPMENT FOR AN ASSOCIATED CONTAINER*\
In this example. the container has been loaded onto another ship at Xiamen on 12/02/2021 and has yet been discharged.

<img width="1361" alt="Screenshot 2021-03-22 at 7 21 11 PM" src="https://user-images.githubusercontent.com/59982275/111985191-44e92100-8b47-11eb-996c-995882808db9.png">

*UPDATE A TRANSSHIPMENT*\
Following the above example, we will update its corresponding value when the shipment has been discharged at Tanjung Pelepas on 17/02/2021
<img width="1367" alt="Screenshot 2021-03-22 at 7 21 43 PM" src="https://user-images.githubusercontent.com/59982275/111985449-95607e80-8b47-11eb-9ea4-d8017e95652c.png">

*GET ALL TRANSSHIPMENTS*\
<img width="1342" alt="Screenshot 2021-03-22 at 7 21 28 PM" src="https://user-images.githubusercontent.com/59982275/111985627-cc369480-8b47-11eb-8dc8-d32a016dff7e.png">

