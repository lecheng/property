import datetime
from myapp import db, bcrypt



class Agent(db.Model):

    __tablename__ = "agent"

    id = db.Column('id', db.Integer, primary_key=True)
    agent_name = db.Column('username', db.VARCHAR(255), nullable=False)
    agent_license = db.Column('dre', db.VARCHAR(255), nullable=True)
    agent_phone = db.Column('cellphone', db.VARCHAR(30), nullable=True)
    agent_phone_china = db.Column('chinesecellphone', db.VARCHAR(45), nullable=True)
    agent_wechat = db.Column('wxid', db.VARCHAR(255), nullable=True)
    agent_email = db.Column('email', db.VARCHAR(60), unique=True, nullable=False)
    agent_office = db.Column('office', db.VARCHAR(30), nullable=True)
    agent_qrcode = db.Column('wxqrcode', db.VARCHAR(500), nullable=True)
    password = db.Column('password', db.VARCHAR(255), nullable=False)
    registered_on = db.Column('createtime', db.DateTime, nullable=True)
    last_login = db.Column('lastlogin', db.DateTime, nullable=True)

    def __init__(self, id, agent_name, agent_email, password, agent_license="",agent_phone="",
        agent_phone_china="", agent_wechat="", agent_office="", agent_qrcode="", last_login=None):
        self.id = id
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
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

    idproperty = db.Column('id', db.Integer, primary_key=True)
    agent_id = db.Column('agent_id', db.Integer)
    address1 = db.Column(db.String(45), nullable=True)
    address2 = db.Column(db.String(45), nullable=True)
    address3 = db.Column(db.String(45), nullable=True)
    price = db.Column('price', db.DECIMAL(16,2), nullable=True)
    price_CNY = db.Column(db.String(45), nullable=True)
    beds = db.Column('beds', db.FLOAT, nullable=True)
    baths = db.Column('baths', db.FLOAT, nullable=True)
    home_size = db.Column(db.String(45), nullable=True)
    home_size_meter = db.Column(db.String(45), nullable=True)
    lot_size = db.Column('lotSize', db.DECIMAL(10,2), nullable=True)
    lot_size_meter = db.Column(db.String(45), nullable=True)
    year_built = db.Column('yearBuilt', db.Integer, nullable=True)
    property_type_English = db.Column('propertyType_en', db.VARCHAR(255), nullable=True)
    property_type_Chinese = db.Column('propertyType', db.String(45), nullable=True)
    description_English = db.Column('description_en', db.VARCHAR(4000), nullable=True)
    description_Chinese = db.Column('description', db.String(2000), nullable=True)
    # slogan_title_English = db.Column(db.String(100), nullable=True)
    # slogan_subtitle_English = db.Column(db.String(100), nullable=True)
    # slogan_title_Chinese = db.Column(db.String(100), nullable=True)
    # slogan_subtitle_Chinese = db.Column(db.String(100), nullable=True)
    # vimeo = db.Column(db.String(45), nullable=True)
    # youtube = db.Column(db.String(45), nullable=True)
    
    domain = db.Column(db.String(100), unique=True, nullable=True)
    property_number = db.Column(db.String(45), nullable=True)
    floors = db.Column(db.String(45), nullable=True)
    list_date_English = db.Column('listdate', db.VARCHAR(255), nullable=True)
    school_district_English = db.Column('schooldistrict', db.String(45), nullable=True)
    # school_district_Chinese = db.Column(db.String(45), nullable=True)
    created_on = db.Column('createtime', db.DateTime, nullable=True)
    


    def __init__(self, idproperty, address1, address3, agent_id, domain, address2=""):
        self.idproperty = idproperty
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.agent_id = agent_id
        self.domain = domain

class PropertyImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.VARCHAR(100), nullable=True)
    grid_overview = db.Column(db.VARCHAR(100), nullable=True)
    grid_gallery = db.Column(db.VARCHAR(100), nullable=True)
    grid_contact = db.Column(db.VARCHAR(100), nullable=True)
    grid_explore = db.Column(db.VARCHAR(100), nullable=True)
    background_overview = db.Column(db.VARCHAR(100), nullable=True)
    background_contact = db.Column(db.VARCHAR(100), nullable=True)
    background_contact_phone = db.Column(db.VARCHAR(100), nullable=True)
    background_explore = db.Column(db.VARCHAR(100), nullable=True)
    gallerys = db.Column(db.VARCHAR(300), nullable=True)
    slideshows = db.Column(db.VARCHAR(300), nullable=True)

        self.created_on = datetime.datetime.now()