from src.parser import parse_resume_txt, parse_job_txt

RESUME_PATH = 'data/resume.txt'
JOB_PATH = 'data/job.txt'

def main():
    resume = parse_resume_txt(RESUME_PATH)
    job = parse_job_txt(JOB_PATH)

    print(resume)

if (__name__ == "__main__") :
    main()