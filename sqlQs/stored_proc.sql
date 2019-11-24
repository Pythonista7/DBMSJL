CREATE DEFINER=`Ash`@`localhost` PROCEDURE `delete_job_proc`(IN jid INT)
BEGIN

DELETE FROM JOBS WHERE job_id = jid ;

END