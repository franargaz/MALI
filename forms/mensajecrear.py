from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import User


class emailForm(FlaskForm):
    Nombre = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=30),
        ],
        render_kw={"nombre": "interesado"},
    )

    Apellido = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=30),
        ],
        render_kw={"apellido": "interesado"},
    )


    email = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=30),
        ],
        render_kw={"email": "interesado"},
    )



    mensaje = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=300),
        ],
        render_kw={"mensaje": "interesado"},
    )


    submit = SubmitField("create")
