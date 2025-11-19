from src.parser import parse_resume_txt, parse_job_txt
from src.extractor import normalize, cleanup
from src.compare import score

RESUME_PATH = 'data/resume.txt'
JOB_PATH = 'data/job.txt'

def main():
    #read file and simplify
    resume = parse_resume_txt(RESUME_PATH)
    job = parse_job_txt(JOB_PATH)

    #extract important info from file
    resume = normalize(resume)
    resume = cleanup(resume)

    job = normalize(job)
    job = cleanup(job)

    #compare info
    grade = score(resume, job)
    print(resume)


    #suggest edits



if (__name__ == "__main__") :
    main()