# cleans up files for extraction of key details later

def parse_resume_txt(path: str) -> str:
    result = ""
    with open(path) as file:
        for line in file:
            result += line.strip()
    return result

def parse_job_txt(path: str) -> str:
    result = ""
    with open(path) as file:
        for line in file:
            result += line.strip()
    return result


