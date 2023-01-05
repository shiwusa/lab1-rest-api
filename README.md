# Laboratory work 3

---

## Installation
1. `cd /project_directory`
2. `docker-compose up -d`

---
## Deployment 
- [v1.0.0](https://github.com/shiwusa/lab1-rest-api/releases/tag/v1.0.0) 
on [Heroku](https://lab1-rest-api.herokuapp.com/)
using GitHub actions
- [v2.0.0](https://github.com/shiwusa/lab1-rest-api/tree/v2.0.0) on [Render](https://rest-api-7355.onrender.com) (as web service)
using existing docker file
- [v3.0.0](https://github.com/shiwusa/lab1-rest-api/tree/v3.0.0) on [Render](https://lab3-back.onrender.com)

---
## Endpoints
`GET methods`:
- `/user` - get all users
- `/record/user_id` - get user`s records by id
- `/record/user_id&category_id` - get record in category
- `/category` - get all public categories
- `/category/owner_id` - get private categories

`POST methods`:
- `/user` - register
- `/login` - login
- `/record` - create new record in category
- `/category` - create public category.
If `private: true` and `owner_id: ` are defined in request:
- `/category` - create private category
