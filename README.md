# AppsProject

[![Netlify Status](https://api.netlify.com/api/v1/badges/4cd42864-0222-485a-9d5a-589ab84b37db/deploy-status)](https://app.netlify.com/sites/apps-project/deploys)


```console
docker-compose up -d 
```

### Flask + Vue.JS (Vuex + PrimeVue + Bootstrap) Project


# Screenshots
![login](https://user-images.githubusercontent.com/29631083/137338085-cc114657-f483-4699-a4bd-11cbd3659400.png)
![discover](https://user-images.githubusercontent.com/29631083/137338165-7cdd0a8c-2147-405d-99ef-3f8429533e18.png)
![converter](https://user-images.githubusercontent.com/29631083/137338190-371f2f7a-2c8c-496e-9a04-d73cf5598295.png)


# ToDo List

- [x] Connect to local relational DB (PostgreSQL)  
  - [x] Connect to dockerize DB with host name in same network
  - [x] Create DB init script
- [x] Create Models and Table in DB
  - [x] Set foreign key apps_id to id in App Table
- [x] Read CSV file
  - [x] Add into DB
  - [x] updated_at fields set to today date and time (optional)
- [x] Create User Model (optional) authentication
  - [x] Register User (optional)
  - [x] Local Authentication (optional)
- [x] Get Apps and Screenshots(include app) Methods
- [x] Design UI
  - [x] Design App&Screenshots Page with Vue.JS ,Bootstrap and PrimeVue
	- [x] Use Vuex , state management (login auth) 
  - [x] Design Webp Converter Page 
    - [x] Create Client-Side method
- [x] Generate Dockerfile and set dependencies
- [x] Generate Kubernetes yaml files (optional)
- [x] Serve on netlify (optional)
