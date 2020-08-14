from . import db

class User(db.Model):

    __tablename__ = 'sm-search-app-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(255),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(200),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

    
    # class Activity(db.Model):
    #     __tablename__ = 'sm-search-app-activity'
    #     activity_type = db.Column(
    #         db.String(255),
    #         index=False,
    #         unique=False,
    #         nullable=False
    #     )
    #     length = db.Column(
    #         db.Float,
    #         index=False,
    #         unique=False,
    #         nullable=False
    #     )
    #     description = db.Column(
    #         db.Text,
    #         index=False,
    #         unique=False,
    #         nullable=True
    #     )
    #     modifications = db.Column(
    #         db.Boolean,
    #         index=False,
    #         unique=False,
    #         nullable=False
    #     )
    #     modifications_explanation = db.Column(
    #         db.Text,
    #         index=False,
    #         unique=False,
    #         nullable=True
    #     )

