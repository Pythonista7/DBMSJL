use TESTDB;
DROP TRIGGER IF EXISTS inc_app_count;
DROP TRIGGER IF EXISTS inc_rec_count;
DROP TRIGGER IF EXISTS inc_job_count;

DROP TRIGGER IF EXISTS dec_app_count;
DROP TRIGGER IF EXISTS dec_rec_count;
DROP TRIGGER IF EXISTS dec_job_count;

CREATE TRIGGER TESTDB.inc_app_count
AFTER INSERT ON APPLICANT_PROFILE
FOR EACH ROW
UPDATE SITE_STATS SET no_of_applicants=no_of_applicants + 1 WHERE  id = 1 ;

CREATE TRIGGER TESTDB.inc_rec_count
AFTER INSERT ON RECUITER
FOR EACH ROW
UPDATE SITE_STATS SET no_of_recruiters=no_of_recruiters + 1 WHERE  id = 1 ;

CREATE TRIGGER TESTDB.inc_job_count
AFTER INSERT ON JOBS
FOR EACH ROW
UPDATE SITE_STATS SET no_of_jobs=no_of_jobs + 1 WHERE  id = 1 ;

##################################################################################

CREATE TRIGGER TESTDB.dec_app_count
AFTER DELETE ON APPLICANT_PROFILE
FOR EACH ROW
UPDATE SITE_STATS SET no_of_applicants=no_of_applicants - 1 WHERE  id = 1 ;

CREATE TRIGGER TESTDB.dec_rec_count
AFTER DELETE ON RECUITER
FOR EACH ROW
UPDATE SITE_STATS SET no_of_recruiters=no_of_recruiters - 1 WHERE  id = 1 ;

CREATE TRIGGER TESTDB.dec_job_count
AFTER DELETE ON JOBS
FOR EACH ROW
UPDATE SITE_STATS SET no_of_jobs=no_of_jobs - 1 WHERE  id = 1 ;

