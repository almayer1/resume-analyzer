# cleans up files for extraction of key details later

def parse_resume_txt(path: str) -> str:
    file = open(path)
    data = file.read()
    file.close()
    return data

def parse_job_txt(path: str) -> str:
    file = open(path)
    data = file.read()
    file.close()
    return data


