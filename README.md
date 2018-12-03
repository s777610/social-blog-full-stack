# Social_Media_Blog
The back-end of this web-application is built by flask, which is a framework of python. I used HTML5, CSS, and SASS to build the front-end for this application. All data of users are stored in SQLite database locally. It uses flask_sqlalchemy to create database object. Then, it takes an advantage of object relation mapping to access data. In addition, it uses flask_migrate to upgrade the database in case of needs. It uses a library called flask_login to check if the current user is login or not and create the login decorator in order to make sure the user is login. It uses flask_wtf to create form classes for registers, login, create blog posts, updates pictures and so on. It uses Pillow library to do image processing to handle profile pictures of users.

## Functionality
1. This social company blog allows users to register and login first.<br>
2. Some functionality only available if users are login.<br>
3. Then, users are able to create the blog post, update the profile picture, and edit the blog post.<br>
4. Owners can edit or delete their own posts.
5. Users can request reset password in case of needs, the confirmation email will be send to users.<br>

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
<img width="809" alt="screen shot 2018-08-07 at 3 52 06 pm" src="https://user-images.githubusercontent.com/35472776/49350037-374fba80-f662-11e8-8afb-05d9d19b1eef.png">


## This is a register page.
<img width="852" alt="screen shot 2018-08-07 at 3 52 48 pm" src="https://user-images.githubusercontent.com/35472776/49350055-50f10200-f662-11e8-8fb3-7bb8c9bb4460.png">


## This is a login page.
<img width="852" alt="screen shot 2018-08-07 at 3 52 48 pm" src="https://user-images.githubusercontent.com/35472776/49350058-54848900-f662-11e8-809f-9c748accdc8e.png">




## This is Info page.
<img width="821" alt="screen shot 2018-08-07 at 3 52 14 pm" src="https://user-images.githubusercontent.com/35472776/49350063-58b0a680-f662-11e8-843d-abe24ca9d11b.png">



## This is a profile page of users. Users can update profile picture and edit and information.
<img width="852" alt="screen shot 2018-08-07 at 3 52 23 pm" src="https://user-images.githubusercontent.com/35472776/49350069-5ea68780-f662-11e8-8e61-a5cdca3325d0.png">



## This is a creating a blog post page, users can create post after registering. Users can delete the posts later on.
<img width="852" alt="screen shot 2018-08-07 at 3 52 48 pm" src="https://user-images.githubusercontent.com/35472776/49350075-6403d200-f662-11e8-9ead-853ce309d42e.png">
