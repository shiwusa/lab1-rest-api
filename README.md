# Laboratory work 2

---
### Variant: <em>custom private categories</em>
    `11 mod 3 = 2`
## Installation
1. `cd /project_directory`
2. `python -m pip instal --user virtualenvl`
3. `docker-compose up -d`

---
## Deployment 
- [v1.0.0](https://github.com/shiwusa/lab1-rest-api/releases/tag/v1.0.0) 
on [Heroku](https://lab1-rest-api.herokuapp.com/)
using GitHub actions
- current version on [Render](https://rest-api-7355.onrender.com) (as web service)
using existing docker file

---
## Endpoints
`GET methods`:
- `/user` - get all users
- `/record/user_id` - get user`s records by id
- `/record` - get record in category
- `/category` - get all public categories
- `/category/owner_id` - get private categories

`POST methods`:
- `/user` - create new user
- `/record` - create new record in category
- `/category` - create public category.
If `private: true` and `owner_id: ` are defined in request:
- `/category` - create private category
