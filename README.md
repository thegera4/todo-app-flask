# todo-app-flask
This is a simple todo web app built with flask and MySQL database (via docker container).

## How to run
1. Clone the repository and make sure you have docker installed, if not install it, including
docker desktop (to run docker-compose). You can install it from here: https://docs.docker.com/engine/install
2. Run `docker-compose up` in the root directory (make sure docker desktop is up and running).
3. Open your browser and go to `http://localhost:5000/login` to see the app running.
4. To stop the app, run `docker-compose stop` in the root directory, if you want to keep/persist the data in the 
database so that, when you run the app again, the data is still there.
5. Or run `docker-compose down` to stop the app and delete all data in the database, as well as the docker container.

**Note:** Remember that you need an '.env' file in the root directory to run the app.

## How to use
When you start in the login route, you will see a login form. You can register a new account by clicking the
`Register` link. You will be redirected to the register route:
