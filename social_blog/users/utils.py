import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from social_blog import mail # conda install -c conda-forge flask-mail


def add_profile_pic(pic_upload, username):
    """
    create storage name for new pics,
    squeeze pics into specific size, and put pics into folder,
    return new storage name
    """
    # to get ext of filename
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    # create new storage_filename
    storage_filename = str(username) + '.' + ext_type
    # create the path, which can store the storage_filename
    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    # squeeze pics into specific size
    pic.thumbnail(output_size)
    pic.save(filepath)
    return storage_filename  # username.png

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])  

    # _external=True mean abs URL
    msg.body = f'''To reset your password, visit the following link:
                {url_for('users.reset_token', token=token, _external=True)} '''
    mail.send(msg)
