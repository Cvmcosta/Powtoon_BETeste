# Powtoon_BETeste
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  ![made-with-python](https://img.shields.io/badge/Made%20with-DjangoREST-ff1709.svg)
---
## About
This repositorie is about BackEnd test. It Was developed with python 3.8 and Django==3.2.9.
In the repositorie has requeriment.txt with all dependecies of project
## Data
Inside folder has a file called fixture.json, this file is the fixture, just load to get all data about user, permission and groups
## User, Permission and Groups
When load the fixture will has,as following informations:

Permissions: 
share_powtoon(able to share any powtoon existent) and  get_all (able to get all powtoon existent)

groups:
powtoonAdmin:this group has the two permission mentioned above

Users:
powtoonadmin with the group powtoonadmin and password:123.

test1 with no group and password:qwer@1234

test2 with no group and password:qwer@1234

## Authentication

The autentication used is simplejwt

To authenticate you must POST the endpoint: 
```bash
http://localhost:8000/token/
```
with this params:
```bash
{
  "username":{username}
  "password":{password}
}
```
The post will return a json with acces token callend "acess" and "refresh"
```bash
{
    "refresh": "...",
    "access": "..."
}
```
you must to have pass the token as bearer token in each requisition as Autorization.


## API
The api has the folowwing functions:

1 -[method = GET] Get: get all powtonw you own and shared with you (if user is powtoonadmin you can get all the powtoons)
```bash
http://localhost:8000/powtoon
```
2 -[method = GET] Get: get especifict powtoon you onw or shared with you (if user is powtoonadmin you can get all the powtoons)
```bash
http://localhost:8000/powtoon/{powtoonid}/
```
3 - [method = post] create : create a powtoon:
```bash
http://localhost:8000/powtoon/
```
body :
```bash
{
    "name":{name},
    "content":{content}
}
```
4- edit: you should do a PUT or Patch passing data in body of requisition (if user is powtoon admin you can edit all the powtoons)
```bash
http://localhost:8000/powtoon/{powtoonid}/
```

5- [method = get] Get Shared powtoons with me
```bash
http://localhost:8000/share/
```
6- [method = post] share a powtoon with other user (you just can share if you are the owner or admin)
```bash
http://localhost:8000/share/
```
body:
```bash
{
    "userid":{userid},
    "powtoonid":{powtoonid}
}
```


