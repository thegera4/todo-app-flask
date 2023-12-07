# todo-app-flask
This is a simple to-do web app built with flask and a MySQL database (via docker container).

## How to run
1. Clone the repository and make sure you have docker installed, if not install it, including
docker desktop (to run docker-compose). You can install it from here: https://docs.docker.com/engine/install
2. Run `docker-compose up` in the root directory (make sure docker desktop is up and running).
3. Open your browser and go to `http://localhost:5000/login` to see the app running.
4. To stop the app, run `docker-compose stop` in the root directory if you want to keep/persist the data in the 
database so that, when you run the app again, the data is still there.
5. Or run `docker-compose down` to stop the app and delete all data in the database, as well as the docker container.

**Note:** Remember that you need a '.env' file in the root directory to run the app.

## How to use
When you start in the login route, you will see a login form. You can register a new account by clicking the
`Register` link. You will be redirected to the register route:

![register](https://github.com/thegera4/todo-app-flask/assets/84020433/4d0ec3a5-e002-45c1-b0c3-d362b2d95f2a)

After you click on the register button, you will be redirected to the login page, so use your new user:

![login](https://github.com/thegera4/todo-app-flask/assets/84020433/9ba38656-3a9a-4024-946f-e16395e704ec)

When you log in, you will see the home page, where all of your todos will be listed, right now is empty:

![index empty](https://github.com/thegera4/todo-app-flask/assets/84020433/60cef703-d764-4115-9da2-5a37838fd6d0)

If you click on the `New` link to be redirected to the create route, so you can create a new todo:

![create](https://github.com/thegera4/todo-app-flask/assets/84020433/b5af71fc-00a2-4ebe-98a1-b24e98c1c6f3)

Click on the create button and you will be redirected again to the home page, where you will see your new todo:

![index with todo](https://github.com/thegera4/todo-app-flask/assets/84020433/5c154d81-8a21-4309-87c8-a01960948e47)

After that, if you click on the `Edit` link in the todo item, you will be redirected to the update route:

![update](https://github.com/thegera4/todo-app-flask/assets/84020433/52e069e5-b497-4a3f-9dfc-fa804c629b45)

You can update the description of your to-do as well as the completed status. Click on the update button to be redirected
to the home page or click on the delete button to delete your to-do:

![index with update](https://github.com/thegera4/todo-app-flask/assets/84020433/72779736-3ac2-45fb-8347-99551b284e5d)


![delete](https://github.com/thegera4/todo-app-flask/assets/84020433/f5778bf5-ef36-4666-b1cc-2b0ab0f497c1)
