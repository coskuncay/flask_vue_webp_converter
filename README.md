# AppsProject

[![Netlify Status](https://api.netlify.com/api/v1/badges/4cd42864-0222-485a-9d5a-589ab84b37db/deploy-status)](https://app.netlify.com/sites/apps-project/deploys)

You need to create server in PostgreSQL same name with POSTGRES_DB

```console
docker-compose up -d 
```

- [x] Connect to local relational DB (PostgreSQL)  
  - [x] Connect to dockerize DB with host name in same network
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
