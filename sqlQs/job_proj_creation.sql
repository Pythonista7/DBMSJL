create database OPUSDB;
use OPUSDB;
create table COMPANY(
	company_name varchar(30) PRIMARY KEY,
    biz_stream varchar(30),
    website varchar(100),
    description varchar(1000)
);

create table RECUITER(
	email varchar(50) PRIMARY KEY,
    passwd varchar(128) NOT NULL,  
	company_name varchar(30) NOT NULL,
    foreign key (company_name) references COMPANY(company_name)
);

create table APPLICANT_PROFILE(
	email_id varchar(50) PRIMARY KEY,
    applicant_passwd varchar(128) NOT NULL,
    signUp_date date,
    first_nm varchar(30) NOT NULL,
	last_nm varchar(30) NOT NULL,
	location varchar(30),
    gender varchar(30)
);


create table APPLICANT_EDU(
	email_id varchar(50) PRIMARY KEY,
	university varchar(50) NOT NULL,	
	major varchar(50) NOT NULL,
	start_date date,
    end_date date,
	cgpa float NOT NULL,
    
    foreign key (email_id)
    references APPLICANT_PROFILE(email_id)
);

create table APPLICANT_SKILLS(
	email_id varchar(50),
	skill varchar(30),
	primary key(email_id,skill),
    foreign key (email_id)
    references APPLICANT_PROFILE(email_id)
    
);

create table APPLICANT_EXP(
	email_id varchar(50),
	total_exp int NOT NULL,
    start_date date,
	end_date date,
	company varchar(30),
    primary key(email_id,start_date,end_date),
    foreign key (email_id)
    references APPLICANT_PROFILE(email_id)

);

create table JOBS(
	job_id int auto_increment PRIMARY KEY,
    company varchar(30) NOT NULL,
    title varchar(30) NOT NULL,
    category varchar(30),
    rec_email varchar(50) NOT NULL,
    posting_loc varchar(30) ,
    requriments varchar(1000)NOT NULL,
    job_type varchar(30),
    posted_on date,
    deadline date,
    no_of_positions int ,
    foreign key (company) references COMPANY(company_name),
	foreign key (rec_email) references RECUITER(email)
    
);
