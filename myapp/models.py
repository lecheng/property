import datetime
from myapp import db, bcrypt



class Agent(db.Model):

    __tablename__ = "agent"

    id = db.Column(db.String(45), primary_key=True)
    agent_name = db.Column(db.String(45), nullable=True)
    agent_license = db.Column(db.String(45), nullable=True)
    agent_phone = db.Column(db.String(45), nullable=True)
    agent_phone_china = db.Column(db.String(45), nullable=True)
    agent_wechat = db.Column(db.String(45), nullable=True)
    agent_email = db.Column(db.String(45), unique=True, nullable=True)
    agent_office = db.Column(db.String(100), nullable=True)
    agent_qrcode = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    registered_on = db.Column(db.DateTime, nullable=True)
    confirmed = db.Column(db.Boolean, nullable=True)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    last_login = db.Column(db.DateTime, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)
    password_reset_token = db.Column(db.String(100), nullable=True)
    is_login = db.Column(db.Boolean, nullable=True)

    def __init__(self, id, agent_name, agent_email, password, agent_license="",agent_phone="",
        agent_phone_china="", agent_wechat="", agent_office="",
        agent_qrcode="", confirmed=False, confirmed_on=None,
        last_login=None,is_admin=False,password_reset_token=None, is_login=False):
        self.id = id
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.is_admin = is_admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
        self.password_reset_token = password_reset_token
        self.agent_name = agent_name
        self.agent_license = agent_license
        self.agent_phone = agent_phone
        self.agent_phone_china = agent_phone_china
        self.agent_wechat = agent_wechat
        self.agent_email = agent_email
        self.agent_office = agent_office
        self.agent_qrcode = agent_qrcode
        self.last_login = last_login

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<email {}'.format(self.agent_email)

class Property(db.Model):

    __tablename__ = "property"

    idproperty = db.Column(db.String(45), primary_key=True)
    agent_id = db.Column(db.String(45, db.ForeignKey('agent.id')))
    address1 = db.Column(db.String(45), nullable=True)
    address2 = db.Column(db.String(45), nullable=True)
    address3 = db.Column(db.String(45), nullable=True)
    price = db.Column(db.String(45), nullable=True)
    price_CNY = db.Column(db.String(45), nullable=True)
    beds = db.Column(db.String(45), nullable=True)
    baths = db.Column(db.String(45), nullable=True)
    home_size = db.Column(db.String(45), nullable=True)
    home_size_meter = db.Column(db.String(45), nullable=True)
    lot_size = db.Column(db.String(45), nullable=True)
    lot_size_meter = db.Column(db.String(45), nullable=True)
    year_built = db.Column(db.String(45), nullable=True)
    property_type_English = db.Column(db.String(45), nullable=True)
    property_type_Chinese = db.Column(db.String(45), nullable=True)
    description_English = db.Column(db.String(2000), nullable=True)
    description_Chinese = db.Column(db.String(2000), nullable=True)
    slogan_title_English = db.Column(db.String(100), nullable=True)
    slogan_subtitle_English = db.Column(db.String(100), nullable=True)
    slogan_title_Chinese = db.Column(db.String(100), nullable=True)
    slogan_subtitle_Chinese = db.Column(db.String(100), nullable=True)
    vimeo = db.Column(db.String(45), nullable=True)
    youtube = db.Column(db.String(45), nullable=True)
    grid_overview = db.Column(db.String(100), nullable=True)
    grid_gallery = db.Column(db.String(100), nullable=True)
    grid_contact = db.Column(db.String(100), nullable=True)
    grid_explore = db.Column(db.String(100), nullable=True)
    background_overview = db.Column(db.String(100), nullable=True)
    background_contact = db.Column(db.String(100), nullable=True)
    background_contact_phone = db.Column(db.String(100), nullable=True)
    background_explore = db.Column(db.String(100), nullable=True)
    domain = db.Column(db.String(100), nullable=True)
    property_number = db.Column(db.String(45), nullable=True)
    floors = db.Column(db.String(45), nullable=True)
    list_date_English = db.Column(db.String(45), nullable=True)
    school_district_English = db.Column(db.String(45), nullable=True)
    school_district_Chinese = db.Column(db.String(45), nullable=True)