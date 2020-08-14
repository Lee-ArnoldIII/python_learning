from flask import request, render_template, make_response, redirect, url_for
from datetime import datetime as dt
from flask import current_app as app
from . models import db, User

@app.route('/', methods=['GET'])
def user_records():
    '''Create a user via query string parameters.'''
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email.first()
        )
        if existing_user:
            return make_response(f'{username} ({email}) already created!')
        new_user = User(
            username=username,
            email=email,
            created=dt.now()
            admin=False
        )
        db.session.add(new_user)
        db.session.commit()
        redirect(url_for('user_records'))
    return render_template(
        'users.jinja2',
        users=User.query.all(),
        title='Show Users'
    )
    