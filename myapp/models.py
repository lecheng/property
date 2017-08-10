import datetime
from myapp import db, bcrypt
from utils import currentConvert



class Agent(db.Model):

    __tablename__ = "agent"

    id = db.Column('id', db.Integer, primary_key=True)
    agent_name = db.Column('realname', db.VARCHAR(255), nullable=False)
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

    __tablename__ = "information"

    idproperty = db.Column('id', db.Integer, primary_key=True)
    agent_id = db.Column('agent_id', db.Integer)
    address = db.Column('streetname', db.VARCHAR(255), nullable=True)
    price = db.Column('price', db.DECIMAL(16,2), nullable=True)
    beds = db.Column('beds', db.FLOAT, nullable=True)
    baths = db.Column('baths', db.FLOAT, nullable=True)
    home_size = db.Column('totalBuildingArea', db.FLOAT, nullable=True)
    lot_size = db.Column('lotSize', db.DECIMAL(10,2), nullable=True)
    year_built = db.Column('yearBuilt', db.Integer, nullable=True)
    property_type_English = db.Column('propertyType_en', db.VARCHAR(255), nullable=True)
    property_type_Chinese = db.Column('propertyType', db.VARCHAR(255), nullable=True)
    description_English = db.Column('description_en', db.VARCHAR(4000), nullable=True)
    description_Chinese = db.Column('description', db.VARCHAR(4000), nullable=True)

    slogan_subtitle_English = db.Column('subtitle_en', db.VARCHAR(255), nullable=True)
    slogan_title_Chinese = db.Column('publicity', db.VARCHAR(255), nullable=True)
    slogan_subtitle_Chinese = db.Column('subtitle', db.VARCHAR(255), nullable=True)
    vimeo = db.Column('vimeo', db.VARCHAR(255), nullable=True)
    youtube = db.Column('youtube', db.VARCHAR(255), nullable=True)
    
    domain = db.Column('website', db.VARCHAR(255), unique=True, nullable=True)
    property_number = db.Column('mls', db.VARCHAR(255), nullable=True)
    list_date_English = db.Column('listdate', db.VARCHAR(255), nullable=True)
    school_district_English = db.Column('schooldistrict', db.VARCHAR(255), nullable=True)
    school_district_Chinese = db.Column('schooldistrict_cn', db.VARCHAR(255), nullable=True)
    created_on = db.Column('createtime', db.DateTime, nullable=True)
    is_published = db.Column('publishSite', db.Integer, nullable=True)
    threed_tour = db.Column('videoTour', db.VARCHAR(255), nullable=True)
    
    def __init__(self, idproperty, address, agent_id):
        self.idproperty = idproperty
        self.address = address
        self.agent_id = agent_id

    def get_price_CNY(self):
        convert = currentConvert(1,'USD','CNY')
        return self.price*convert

    def get_home_size_meter(self):
        return self.home_size * 0.092903

    def get_lot_size_meter(self):
        return self.lot_size * 0.092903

class PropertyImage(db.Model):

    __tablename__ = "propertyimage"
    
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, unique=True, nullable=True)
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

    def __init__(self, property_id):
        self.property_id = property_id

    def is_completed(self):
        if not self.slideshows or not self.gallerys or not self.grid_overview or not \
        self.grid_gallery or not self.grid_contact or not self.grid_explore or not \
        self.background_overview or not self.background_explore or not self.background_contact\
        or not self.background_contact_phone:
            return False
        return True