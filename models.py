from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Float, DateTime
import bcrypt
from datetime import datetime
from sqlalchemy import event

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=True)
    middlename = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    confirmation_token = db.Column(db.String(100), unique=True, nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    height = db.Column(db.String(100), nullable=True)
    landline = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    citizenship = db.Column(db.String(100), nullable=True)
    pwd = db.Column(db.String(100), nullable=True)
    user_type = db.Column(db.String(100), nullable=False)
    user_status = db.Column(db.String(100), nullable=True)
    profile_pic = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=True)

    lastname = db.Column(db.String(100), nullable=True)
    civil_status = db.Column(db.String(100), nullable=True)
    suffix = db.Column(db.String(100), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    houseNoStreet = db.Column(db.String(100), nullable=True)
    brgy = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    province = db.Column(db.String(100), nullable=True)
    religion = db.Column(db.String(100), nullable=True)
    tinID = db.Column(db.Integer, nullable=True)
    gsisNO = db.Column(db.Integer, nullable=True)
    pagibigNo = db.Column(db.Integer, nullable=True)
    philNo = db.Column(db.Integer, nullable=True)
    disability = db.Column(db.String(100), nullable=True)
    employmentStatus = db.Column(db.String(100), nullable=True)
    employmentType = db.Column(db.String(100), nullable=True)
    activeWork = db.Column(db.String(100), nullable=True)
    willingToWork = db.Column(db.String(100), nullable=True)
    porPs = db.Column(db.String(100), nullable=True)
    prefoccupation = db.Column(db.String(100), nullable=True)
    preflocation = db.Column(db.String(100), nullable=True)
    locationSelected = db.Column(db.String(100), nullable=True)
    salary = db.Column(db.Integer, nullable=True)
    passportNo = db.Column(db.Integer, nullable=True)
    passportExp = db.Column(db.Date, nullable=True)
    elemschool = db.Column(db.String(100), nullable=True)
    yearGradElem = db.Column(db.Integer, nullable=True)
    secondarySchool = db.Column(db.String(100), nullable=True)
    yearGradSec = db.Column(db.Integer, nullable=True)
    terSchool = db.Column(db.String(100), nullable=True)
    courseTer = db.Column(db.String(100), nullable=True)
    yearGradTer = db.Column(db.Integer, nullable=True)
    gradSchool = db.Column(db.String(100), nullable=True)
    courseGrad = db.Column(db.String(100), nullable=True)
    yearGradGrad = db.Column(db.Integer, nullable=True)

    skills = db.Column(db.String(100), nullable=True)
    aboutme = db.Column(db.String(100), nullable=True)
    workStatus = db.Column(db.String(100), nullable=True)
    jobform = db.Column(db.LargeBinary, nullable=True)





    employer_details = db.relationship('EmployerDetails', backref='user', uselist=False)
    applications = db.relationship('Application', backref='user', lazy=True)
    peso = db.relationship('PESO', backref='user', uselist=False)
    messages = db.relationship('Message', backref='user', lazy=True)

    def __init__(self, email, password, name,  firstname, lastname, user_type, user_status, confirmation_token=None,):
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.confirmation_token = confirmation_token
        self.user_type = user_type
        self.user_status=user_status
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class EmployerDetails(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    tin_id = db.Column(db.Integer, nullable=True)
    company_name = db.Column(db.String(100), nullable=True)
    company_address = db.Column(db.String(100), nullable=True)
    company_logo = db.Column(db.String(255))
    trade_name = db.Column(db.String(100), nullable=True)
    employer_type = db.Column(db.String(100), nullable=True)
    business_type = db.Column(db.String(100), nullable=True)
    contact_person = db.Column(db.String(100), nullable=True)
    position = db.Column(db.String(100), nullable=True)
    phone_no = db.Column(db.Integer, nullable=True)
    email_add = db.Column(db.String(100), nullable=True)
    verification_status = db.Column(db.String(100), nullable=True)
    company_gmap = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    jobs = db.relationship('Jobs', backref='employer', lazy=True)
    

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    job_address = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.String(100), nullable=False)
    job_requirements = db.Column(db.String(100), nullable=False)
    job_requirementdocu = db.Column(db.String(100), nullable=False)
    salary_range_min = db.Column(db.Float, nullable=False)
    salary_range_max = db.Column(db.Float, nullable=False)
    job_type = db.Column(db.String(100), nullable=False)
    job_status = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    job_benefits = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    email_add = db.Column(db.String(100), nullable=False)
    company_logo = db.Column(db.String(255), nullable=True)


    employer_id = db.Column(db.Integer, db.ForeignKey('employer_details.company_id'), nullable=False)
    applications = db.relationship('Application', backref='job', lazy=True)

class Application(db.Model):
    application_id = db.Column(db.Integer, primary_key=True)
    requirements = db.Column(db.LargeBinary, nullable=True)
    application_date = db.Column(db.DateTime)
    application_status = db.Column(db.String(100), nullable=False)
    company_id = db.Column(db.Integer, nullable=True)
    company_applied = db.Column(db.String(100), nullable=False)
    position_applied = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)

class PESO(db.Model):
    peso_id = db.Column(db.Integer, primary_key=True)
    peso_username = db.Column(db.String(100), nullable=False)
    peso_password = db.Column(db.String(100), nullable=False)
    peso_employee_name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.relationship('Message', backref='peso', lazy=True)

class SPES(db.Model):
    spes_id = db.Column(db.Integer, primary_key=True)
    spes_code = db.Column(db.Integer, nullable=False)
    spes_password = db.Column(db.String(100), nullable=False)
    spes_name =  db.Column(db.String(100), nullable=False)
    spes_firstname =  db.Column(db.String(100), nullable=False)
    spes_middlename =  db.Column(db.String(100), nullable=False)
    spes_lastname =  db.Column(db.String(100), nullable=False)
    spes_civil =  db.Column(db.String(100), nullable=False)
    spes_spestype =  db.Column(db.String(100), nullable=False)
    spes_citizenship =  db.Column(db.String(100), nullable=False)
    spes_gsisbeneficiary =  db.Column(db.String(100), nullable=False)
    spes_gsisstatus =  db.Column(db.String(100), nullable=False)
    spes_social =  db.Column(db.String(100), nullable=False)
    spes_presentadd =  db.Column(db.String(100), nullable=False)
    spes_permanentadd =  db.Column(db.String(100), nullable=False)

    spes_elemschool =  db.Column(db.String(100), nullable=False)
    spes_elemgrad =  db.Column(db.String(100), nullable=False)
    spes_elemlvl =  db.Column(db.String(100), nullable=False)
    spes_junschool =  db.Column(db.String(100), nullable=False)
    spes_jungrad =  db.Column(db.String(100), nullable=False)
    spes_junlvl =  db.Column(db.String(100), nullable=False)
    spes_senschool =  db.Column(db.String(100), nullable=False)
    spes_strand =  db.Column(db.String(100), nullable=False)
    spes_sengrad =  db.Column(db.String(100), nullable=False)
    spes_senlvl =  db.Column(db.String(100), nullable=False)
    spes_colschool =  db.Column(db.String(100), nullable=False)
    spes_course =  db.Column(db.String(100), nullable=False)
    spes_colgrad =  db.Column(db.String(100), nullable=False)
    spes_collvl =  db.Column(db.String(100), nullable=False)
    spes_parent_status =  db.Column(db.String(100), nullable=False)

    spes_mofirstname =  db.Column(db.String(100), nullable=False)
    spes_momiddlename =  db.Column(db.String(100), nullable=False)
    spes_molastname =  db.Column(db.String(100), nullable=False)
    spes_mocontact =  db.Column(db.String(100), nullable=False)
    spes_moocupation =  db.Column(db.String(100), nullable=False)


    spes_fafirstname =  db.Column(db.String(100), nullable=False)
    spes_famiddlename =  db.Column(db.String(100), nullable=False)
    spes_falastname =  db.Column(db.String(100), nullable=False)
    spes_facontact =  db.Column(db.String(100), nullable=False)
    spes_faocupation =  db.Column(db.String(100), nullable=False)
    

    resume = db.Column(db.LargeBinary, nullable=True)
    birth_certificate = db.Column(db.LargeBinary, nullable=True)
    grades = db.Column(db.LargeBinary, nullable=True)


    spes_email = db.Column(db.String(100), nullable=False)
    spes_gender = db.Column(db.String(100), nullable=True)
    spes_birthday = db.Column(db.Date)
    spes_confirmation_token = db.Column(db.String(100), unique=True, nullable=True)
    spes_address =  db.Column(db.String(100), nullable=False)
    spes_phoneno = db.Column(db.String(100), nullable=False)
    spes_post = db.Column(db.String(100), nullable =False)
    spes_application_status = db.Column(db.String(100), nullable=False)
    spes_application_date = db.Column(db.DateTime, default=datetime.utcnow)
    spes_status = db.Column(db.String(100), nullable=False)
    spes_profile_pic = db.Column(db.String(100), nullable=True)
    messages = db.relationship('Message', backref='spes', lazy=True)

    def __init__(self, spes_email, spes_password, spes_name, spes_status, spes_confirmation_token=None):
        self.spes_name = spes_name
        self.spes_email = spes_email
        self.spes_password = bcrypt.hashpw(spes_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.spes_confirmation_token = spes_confirmation_token
        self.spes_status=spes_status
    
    def check_password(self, password):
     return bcrypt.checkpw(password.encode('utf-8'), self.spes_password.encode('utf-8'))
    
class SPESApplication(db.Model):
    fullname =  db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address =  db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    application_id = db.Column(db.Integer, primary_key=True)
    application_date = db.Column(db.DateTime, default=datetime.utcnow)
    application_status = db.Column(db.String(100), default='Pending', nullable=False)  # Can be 'Pending', 'Approved', 'Rejected'
    application_message = db.Column(db.Text, nullable=True)

    spes_id = db.Column(db.Integer, db.ForeignKey('spes.spes_id'), nullable=False)
    peso_id = db.Column(db.Integer, db.ForeignKey('peso.peso_id'), nullable=False)

    spes = db.relationship('SPES', backref=db.backref('applications', lazy=True))
    peso = db.relationship('PESO', backref=db.backref('applications', lazy=True))

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_title = db.Column(db.String(255), nullable=False)
    task_description = db.Column(db.Text, nullable=True)
    task_assigned_date = db.Column(db.DateTime, default=datetime.utcnow)
    task_due_date = db.Column(db.DateTime, nullable=True)
    task_status = db.Column(db.String(100), default='Pending', nullable=False)  # Can be 'Pending', 'Completed', etc.
    file = db.Column(db.LargeBinary, nullable=True)

    peso_id = db.Column(db.Integer, db.ForeignKey('peso.peso_id'), nullable=False)
    spes_id = db.Column(db.Integer, db.ForeignKey('spes.spes_id'), nullable=False)


    peso = db.relationship('PESO', backref=db.backref('tasks', lazy=True))
    spes = db.relationship('SPES', backref=db.backref('tasks', lazy=True))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    peso_id = db.Column(db.Integer, db.ForeignKey('peso.peso_id'))
    spes_id = db.Column(db.Integer, db.ForeignKey('spes.spes_id'))
