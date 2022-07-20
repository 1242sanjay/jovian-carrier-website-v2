import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                      connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), val=id)
    rows = result.all()
    if len(rows)==0:
      return None
    else:
      return dict(rows[0])


def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query,
                 job_id = job_id,
                 full_name = application['full_name'],
                 email = application['email'],
                 linkedin_url = application['linkedin_url'],
                 education = application['education'],
                 work_experience = application['work_experience'],
                 resume_url = application['resume_url']
                )
