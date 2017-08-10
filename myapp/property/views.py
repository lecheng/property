# myapp/main/views.py


#################
#### imports ####
#################
import uuid
import os

from flask import render_template, request, redirect, url_for, jsonify, flash
from flask import Blueprint
from flask_login import current_user
from flask_login import login_required
from werkzeug.utils import secure_filename
from PIL import Image


from myapp.models import Property, Agent, PropertyImage
from myapp import db
from utils import mkdir, voffset_on_phone
################
#### config ####
################

property_blueprint = Blueprint('property', __name__,)
IMG_UPLOAD_FOLDER = 'myapp/static/assets/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

################
#### routes ####
################


# list properties on property manage page
@property_blueprint.route('/property')
@login_required
def property_list():
    properties = Property.query.filter_by(agent_id=current_user.id)
    if not properties:
        flash("Please add your first property!","danger")
    return render_template('property.html', property_list=properties)

# go to image uploading page
@property_blueprint.route('/property/images', methods=['GET'])
@login_required
def images_page():
    id = request.args.get('id')
    print id
    property_obj = PropertyImage.query.filter_by(property_id=id).first()
    if not property_obj:
        return render_template('images.html', property_id=id, property=None, slideshows=[], gallerys=[])
    slideshows = []
    gallerys = []
    if property_obj.slideshows:
        slideshows = property_obj.slideshows.split(',')
    if property_obj.gallerys:
        gallerys = property_obj.gallerys.split(',')
    print property_obj
    return render_template('images.html', property_id=id, property=property_obj, slideshows=slideshows, gallerys=gallerys)

# limit the type of uploaded file
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload image files
@property_blueprint.route('/property/upload', methods=['POST'])
@login_required
def upload_images():
    type_error = False
    id = request.form.get('id')
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
    property_main = Property.query.filter_by(idproperty=id).first()
    property_obj = PropertyImage.query.filter_by(property_id = id).first()
    if not property_obj:
        property_obj = PropertyImage(property_id=id)
    PROPERTY_UPLOAD_FOLDER = IMG_UPLOAD_FOLDER + current_user.agent_email + '/property/' + property_main.domain
    mkdir(PROPERTY_UPLOAD_FOLDER)
    
    # save grid_overview
    filename = secure_filename(grid_overview.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Grid overview file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        property_obj.grid_overview = fileurl
        grid_overview.save(filepath)
    
    # save grid_gallery
    filename = secure_filename(grid_gallery.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Grid gallery file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        property_obj.grid_gallery = fileurl
        grid_gallery.save(filepath)

    # save grid_contact
    filename = secure_filename(grid_contact.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Grid contact file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        grid_contact.save(filepath)
        property_obj.grid_contact = fileurl

    # save grid_explore
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Grid explore file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        filename = secure_filename(grid_explore.filename)
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        grid_explore.save(filepath)
        property_obj.grid_explore = fileurl

    # save background_overview
    filename = secure_filename(bg_overview.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Background overview file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_overview.save(filepath)
        property_obj.background_overview = fileurl

    # save background_contact
    filename = secure_filename(bg_contact.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Background contact file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_contact.save(filepath)
        property_obj.background_contact = fileurl

    # save background_contact_phone
    filename = secure_filename(bg_contact_phone.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Background contact phone file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_contact_phone.save(filepath)
        property_obj.background_contact_phone = fileurl

    # save background_explore
    filename = secure_filename(bg_explore.filename)
    if filename:
        if not allowed_file(filename):
            type_error = True
            flash('Background explore file type error! (.png/.jpg/.jpeg allowed!)','danger')
        filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
        fileurl = filepath[13:]
        bg_explore.save(filepath)
        property_obj.background_explore = fileurl

    # save gallery
    fileurl = []
    for gallery in gallerys:
        filename = secure_filename(gallery.filename)
        if filename:
            if not allowed_file(filename):
                type_error = True
                flash('Gallery file type error! (.png/.jpg/.jpeg allowed!)','danger')
            filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
            fileurl += [filepath[13:]]
            gallery.save(filepath)
    if fileurl:
        property_obj.gallerys = ",".join(fileurl)

    # save slideshows
    fileurl = []
    for slideshow in slideshows:
        filename = secure_filename(slideshow.filename)
        if filename:
            if not allowed_file(filename):
                type_error = True
                flash('Slideshow file type error! (.png/.jpg/.jpeg allowed!)','danger')
            filepath = os.path.join(PROPERTY_UPLOAD_FOLDER,filename)
            fileurl += [filepath[13:]]
            slideshow.save(filepath)
    if fileurl:
        property_obj.slideshows = ",".join(fileurl)
    if not type_error:
        db.session.add(property_obj)
        db.session.commit()
        flash(property_main.address + ' images upload success!','success')
    return redirect(url_for('property.property_list'))

# access to the published property website
@property_blueprint.route('/', methods=['GET'])
def website():
    print request.headers['Host']
    host = request.headers['Host']
    property_obj = Property.query.filter_by(domain = host.lower()).first()
    if not property_obj:
        property_obj = Property.query.filter_by(domain = ('www.'+host.lower())).first()
    if not property_obj:
        flash("No such domain!",'danger')
    property_image = PropertyImage.query.filter_by(property_id = property_obj.idproperty).first()
    slideshows = property_image.slideshows.split(',')
    gallerys = property_image.gallerys.split(',')
    gallerys_objs = []
    for gallery in gallerys:
        path = 'myapp/static/'+gallery
        im = Image.open(path)
        print im
        size = im.size
        obj = {
            'path': gallery,
            'voffset_on_phone': voffset_on_phone(size[0],size[1])
        }
        gallerys_objs += [obj]
    full_address = property_obj.address
    agent = Agent.query.filter_by(id = property_obj.agent_id).first()
    if 'cn' in request.args:
        return render_template('template_cn.html', full_address=full_address, property=property_obj,
        slideshows=slideshows, gallerys=gallerys_objs, agent = agent, property_image=property_image)
    return render_template('template_en.html',full_address=full_address, property=property_obj,
        slideshows=slideshows, gallerys=gallerys_objs, agent = agent, property_image=property_image)

# preview the website to be published 
@property_blueprint.route('/property/preview',methods=['GET'])
@login_required
def preview():
    id = request.args.get('id')
    property_obj = Property.query.filter_by(idproperty = id).first()
    if property_obj.agent_id != current_user.id:
        flash('No right to preview the property!')
        return redirect(url_for('property.property_list'))
    property_image = PropertyImage.query.filter_by(property_id = id).first()
    if not property_image.is_completed():
        flash('Missed some images! Please upload necessary images first!','danger')
        return redirect(url_for('property.property_list'))

    slideshows = property_image.slideshows.split(',')
    gallerys = property_image.gallerys.split(',')
    gallerys_objs = []
    for gallery in gallerys:
        path = 'myapp/static/'+gallery
        im = Image.open(path)
        print im
        size = im.size
        obj = {
            'path': gallery,
            'voffset_on_phone': voffset_on_phone(size[0],size[1])
        }
        gallerys_objs += [obj]
    full_address = property_obj.address
    complete = True
    if not slideshows:
        flash('Miss slideshows images, please upload images first!','danger')
        complete = False
    if not gallerys:
        flash('Miss gallerys images, please upload images first!','danger')
        complete = False
    if not property_image.grid_overview:
        flash('Miss grid overview image, please upload images first!','danger')
        complete = False
    if not property_image.grid_gallery:
        flash('Miss grid gallery image, please upload images first!','danger')
        complete = False
    if not property_image.grid_contact:
        flash('Miss grid contact image, please upload images first!','danger')
        complete = False
    if not property_image.grid_explore:
        flash('Miss grid explore image, please upload images first!','danger')
        complete = False
    if not property_image.background_overview:
        flash('Miss background overview image, please upload images first!','danger')
        complete = False
    if not property_image.background_explore:
        flash('Miss background explore image, please upload images first!','danger')
        complete = False
    if not property_image.background_contact:
        flash('Miss background contact image, please upload images first!','danger')
        complete = False
    if not property_image.background_contact_phone:
        flash('Miss background contact phone image, please upload images first!','danger')
        complete = False
    if not complete:
        return redirect(url_for('property.property_list'))
    agent = Agent.query.filter_by(id = property_obj.agent_id).first() 
    if 'cn' in request.args:
        return render_template('template_cn.html', full_address=full_address, property=property_obj,
        slideshows=slideshows, gallerys=gallerys_objs, agent = agent, property_image=property_image)
    return render_template('template_en.html',full_address=full_address, property=property_obj,
        slideshows=slideshows, gallerys=gallerys_objs, agent = agent, property_image=property_image)

# publish property website
@property_blueprint.route('/property/publish', methods=['POST'])
@login_required
def publish():
    id = request.form.get('id')
    property_image = PropertyImage.query.filter_by(property_id=id).first()
    property_obj = Property.query.filter_by(idproperty=id).first()
    message = ""
    if not property_image or not property_image.is_completed():
        message = "Can't publish because some images haven't been uploaded! Please upload images first!"
        return jsonify({'message':message,'status':0})
    if not property_obj.domain:
        message = "No domain is deteted! Please buy your domain for the property first!"
        return jsonify({'message':message,'status':0})
    if property_obj.is_published == 1:
        message = "The website has published!"
        return jsonify({'message':message,'status':0})
    property_obj.is_published = 1
    db.session.add(property_obj)
    db.session.commit()
    message = "Publish success!"
    return jsonify({'message':message,'status':1})