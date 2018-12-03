# Social_Media_Blog
The back-end of this web-application is built by flask, which is a framework of python. I used HTML5, CSS, and SASS to build the front-end for this application. All data of users are stored in SQLite database locally. It uses flask_sqlalchemy to create database object. Then, it takes an advantage of object relation mapping to access data. In addition, it uses flask_migrate to upgrade the database in case of needs. It uses a library called flask_login to check if the current user is login or not and create the login decorator in order to make sure the user is login. It uses flask_wtf to create form classes for registers, login, create blog posts, updates pictures and so on. It uses Pillow library to do image processing to handle profile pictures of users.

## Functionality
1. This social company blog allows users to register and login first.<br>
2. Then, users are able to create the blog post, update the profile picture, and edit the blog post.<br>
3. Users can request reset password in case of needs, the confirmation email will be send to users.<br>

## Installation (platform: osx-64)
1. Create environment
```
conda env create -f environment.yml
```
2. Activate environment
```
source activate socialblogenv
```
3. Run application
```
python app.py
```
## Installation of Dev-Tool
1. install dependencies from package.json
```
npm install
```


## This is a home page, which shows all blog posts.
<img width="809" alt="screen shot 2018-08-07 at 3 52 06 pm" src="https://user-images.githubusercontent.com/35472776/43806721-0547b038-9a5a-11e8-87d8-1f1b5117f3f7.png">



## This is a creating a blog post page, users can create post after registering.
<img width="821" alt="screen shot 2018-08-07 at 3 52 14 pm" src="https://user-images.githubusercontent.com/35472776/43806725-08345634-9a5a-11e8-878e-ee9ec3299b36.png">



## This is a profile page of users. Users can update profile picture and edit and information.
<img width="852" alt="screen shot 2018-08-07 at 3 52 23 pm" src="https://user-images.githubusercontent.com/35472776/43806728-0a9b6b74-9a5a-11e8-9c8f-c1852b7bb3f8.png">



## Only the author can delete blog posts. The confirmation message will pop up after clicking the delete button.
<img width="852" alt="screen shot 2018-08-07 at 3 52 48 pm" src="https://user-images.githubusercontent.com/35472776/43806730-0de70824-9a5a-11e8-9e30-d9d4f621c2fb.png">
