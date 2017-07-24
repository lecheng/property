# myapp/main/views.py


#################
#### imports ####
#################
import uuid
import os

from flask import render_template, request, redirect, url_for, jsonify
from flask import Blueprint
from flask_login import current_user
from flask_login import login_required
from werkzeug.utils import secure_filename


from myapp.models import Property, Agent
from myapp import db
from utils import mkdir
################
#### config ####
################

property_blueprint = Blueprint('property', __name__,)
IMG_UPLOAD_FOLDER = 'myapp/static/assets/img/'

################
#### routes ####
################

@property_blueprint.route('/property')
@login_required
def property_list():
    properties = Property.query.all()
    if not properties:
        flash("Please add your first property!","danger")
    return render_template('property.html', property_list=properties)

@property_blueprint.route('/property/form', methods=['GET'])
@login_required
def property_form():
    if 'id' not in request.args:
        return render_template('form.html', property = {})
    id = request.args.get('id')
    property_obj = Property.query.filter_by(idproperty=id).first()
    return render_template('form.html', property=property_obj)

@property_blueprint.route('/property/save', methods=['POST'])
@login_required
def property_save():
    id = request.form.get('id')
    print id
    domain = request.form.get('domain')
    address1 = request.form.get('address1')
    address2 = request.form.get('address2')
    address3 = request.form.get('address3')
    property_num = request.form.get('property-num')
    price_us = request.form.get('price_us')
    beds = request.form.get('beds')
    baths = request.form.get('baths')
    floors = request.form.get('floors')
    home_size = request.form.get('home-size')
    lot_size = request.form.get('lot-size')
    year = request.form.get('year')
    property_type_eng = request.form.get('property-type-eng')
    property_type_chn = request.form.get('property-type-chn')
    date = request.form.get('date')
    school_district_eng = request.form.get('school-district-eng')
    school_district_chn = request.form.get('school-district-chn')
    sale_state = request.form.get('sale-state')
    description_eng = request.form.get('description-eng')
    description_chn = request.form.get('description-chn')
    vimeo_id = request.form.get('vimeo-id')
    youtube_id = request.form.get('youtube-id')
    slogan_title_eng = request.form.get('slogan-title-eng')
    slogan_subtitle_eng = request.form.get('slogan-subtitle-eng')
    slogan_title_chn = request.form.get('slogan-title-chn')
    slogan_subtitle_chn = request.form.get('slogan-subtitle-chn')
    if id:
        property_obj = Property.query.filter_by(idproperty=id).first()
        property_obj.address1 = address1
        property_obj.address2 = address2
        property_obj.address3 = address3
        property_domain = domain
        flash('Save success! Please upload images for the property next!','success')
    else:
        property_obj = Property(
                address1 = address1,
                domain = domain,
                address2 = address2,
                address3 = address3,
                agent_id = current_user.id,
                idproperty = uuid.uuid4()
            ) 
    property_obj.property_number = property_num
    property_obj.price = price_us
    property_obj.beds = beds
    property_obj.baths = baths
    property_obj.home_size = home_size
    property_obj.lot_size = lot_size
    property_obj.year_built = year
    property_obj.property_type_English = property_type_eng
    property_obj.property_type_Chinese = property_type_chn
    property_obj.description_English = description_eng
    property_obj.description_Chinese = description_chn
    property_obj.slogan_subtitle_English = slogan_subtitle_eng
    property_obj.slogan_title_English = slogan_title_eng
    property_obj.slogan_subtitle_Chinese = slogan_subtitle_chn
    property_obj.slogan_title_Chinese = slogan_title_chn
    property_obj.vimeo = vimeo_id
    property_obj.youtube = youtube_id
    property_obj.floors = floors
    property_obj.list_date_English = date
    property_obj.school_district_English = school_district_eng
    property_obj.school_district_Chinese = school_district_chn
    db.session.add(property_obj)
    db.session.commit()
    return redirect(url_for('property.property_list'))

@property_blueprint.route('/property/upload', methods=['POST'])
@login_required
def upload_images():
    id = request.args.get('id')
    grid_overview = request.files['grid-overview']
    grid_gallery = request.files['grid-gallery']
    grid_contact = request.files['grid-contact']
    grid_explore = request.files['grid-explore']
    bg_overview = request.files['bg-overview']
    bg_contact = request.files['bg-contact']
    bg_contact_phone = request.files['bg-contact-phone']
    bg_explore = request.files['bg-explore']
    slideshows = request.files.getlist('slideshow[]')
    gallerys =  request.files.getlist('gallery[]')
    property_obj = Property.query.filter_by(idproperty=id).first()
    PROPERTY_UPLOAD_FOLDER = IMG_UPLOAD_FOLDER + current_user.agent_email + '/property/' + property_obj.domain
    mkdir(PROPERTY_UPLOAD_FOLDER)
    
    # save grid_overview
    filename = secure_filename(grid_overview.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        property_obj.grid_overview = fileurl
        grid_overview.save(filepath)
    
    # save grid_gallery
    filename = secure_filename(grid_gallery.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        property_obj.grid_gallery = fileurl
        grid_gallery.save(filepath)

    # save grid_contact
    filename = secure_filename(grid_contact.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        grid_contact.save(filepath)
        property_obj.grid_contact = fileurl

    # save grid_explore
    if filename:
        filename = secure_filename(grid_explore.filename)
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        grid_explore.save(filepath)
        property_obj.grid_explore = fileurl

    # save background_overview
    filename = secure_filename(bg_overview.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_overview.save(filepath)
        property_obj.background_overview = fileurl

    # save background_contact
    filename = secure_filename(bg_contact.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_contact.save(filepath)
        property_obj.background_contact = fileurl

    # save background_contact_phone
    filename = secure_filename(bg_contact_phone.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_contact_phone.save(filepath)
        property_obj.background_contact_phone = fileurl

    # save background_explore
    filename = secure_filename(bg_explore.filename)
    if filename:
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_explore.save(filepath)
        property_obj.background_explore = fileurl

    # save gallery
    fileurl = []
    for gallery in gallerys:
        filename = secure_filename(gallery.filename)
        if filename:
            filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
            fileurl += [filepath[13:]]
            gallery.save(filepath)
    property_obj.gallerys = ",".join(fileurl)

    # save slideshows
    fileurl = []
    for slideshow in slideshows:
        filename = secure_filename(slideshow.filename)
        if filename:
            filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
            fileurl += [filepath[13:]]
            slideshow.save(filepath)
    property_obj.slideshows = ",".join(fileurl)
    db.session.add(property_obj)
    db.session.commit()
    return jsonify({"message":"Upload success!","code":1})

@property_blueprint.route('/property/preview',methods=['GET'])
def preview():
    id = request.args.get('id')
    property_obj = Property.query.filter_by(idproperty = id).first()
    slideshows = property_obj.slideshows.split(',')
    gallerys = property_obj.gallerys.split(',')
    full_address = property_obj.address1
    agent = Agent.query.filter_by(id = property_obj.agent_id).first()
    if property_obj.address2:
        full_address = full_address + ', ' + property_obj.address2
    full_address = full_address + ', ' + property_obj.address3 
    return render_template('template_en1.html',full_address=full_address, property=property_obj,
        slideshows=slideshows, gallerys=gallerys, agent = agent)

@property_blueprint.route('/property/delete',methods=['POST'])
@login_required
def property_delete():
    id = request.form.get('id')
    property_obj = Property.query.filter_by(idproperty=id).delete()
    db.session.commit()
    return jsonify({"message":"Delete success!", "code":1})