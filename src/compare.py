#takes two lists and returns a list of similar elements
def similaritylist(resume: list, job: list) -> list:
    result = []
    for i in job:
        for j in resume:
            if i == j:
                result.append(i)
    return result

#compares how well the resume list fits the job description list 
def score(resume: list, job: list) -> int:
    similar = similaritylist(resume, job)
    job_count = 0
    similar_count = 0
    for i in job:
        job_count += 1
    for i in similar:
        similar_count += 1
    score = similar_count / job_count
    return score

