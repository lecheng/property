# myapp/user/forms.py


from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from myapp.models import Agent


class LoginForm(Form):
    email = TextField('login_email', validators=[DataRequired(), Email()])
    password = PasswordField('login_password', validators=[DataRequired()])


class RegisterForm(Form):
    name = TextField(
        'r_name',
        validators=[DataRequired()]
        )
    email = TextField(
        'r_email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=255)])
    password = PasswordField(
        'r_password',
        validators=[DataRequired(), Length(min=6, max=255)]
    )
    confirm = PasswordField(
        'r_password_confirm',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        agent = agent.query.filter_by(agent_email=self.email.data).first()
        if agent:
            self.email.errors.append("Email already registered")
            return False
        return True


class ForgotForm(Form):
    email = TextField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=255)])

    def validate(self):
        initial_validation = super(ForgotForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append("This email is not registered")
            return False
        return True


class ChangePasswordForm(Form):
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=255)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
