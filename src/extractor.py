KEYWORDS = {
    "hard_skills": {
        # Tech
        "python", "java", "c", "c++", "c#", "javascript", "typescript", "sql",
        "html", "css", "bash", "linux", "docker", "kubernetes", "react",
        "node", "aws", "azure", "gcp", "git", "flask", "django", "graphql",
        # Business / Finance
        "excel", "forecasting", "budgeting", "bookkeeping", "accounting",
        "auditing", "fp&a", "crm", "saas", "risk analysis", "financial modeling",
        # Marketing
        "seo", "sem", "content strategy", "copywriting", "analytics", 
        "google ads", "meta ads", "email marketing",
        # Healthcare
        "patient care", "vital signs", "charting", "emr", "ehr", "triage",
        # Retail / Customer Service
        "pos", "inventory", "merchandising", "upselling", "cash handling",
        # Trades / Construction
        "hvac", "blueprints", "cad", "diagnostics", "welding", "machining"
    },

    "tools_technologies": {
        # Tech tools
        "jira", "confluence", "postman", "jenkins", "terraform", "ansible",
        "mysql", "postgresql", "mongodb", "redis", "vs code", "intellij",
        # Business tools
        "salesforce", "hubspot", "quickbooks", "tableau", "power bi",
        # Marketing tools
        "google analytics", "hootsuite", "canva", "figma",
        # Healthcare tools
        "epic", "cerner", "meditech",
        # Retail tools
        "square", "shopify", "lightspeed"
    },

    "core_concepts": {
        # Tech concepts
        "data structures", "algorithms", "object oriented programming",
        "time complexity", "networking", "databases", "distributed systems",
        # Business / Finance
        "market research", "competitive analysis", "pricing strategy",
        # Marketing
        "branding", "target audience", "campaign strategy",
        # Healthcare
        "medical terminology", "infection control",
        # Education
        "lesson planning", "curriculum development"
    },

    "qualifications_education": {
        "bachelor", "bachelors", "bs", "ms", "mba", "high school diploma",
        "associates", "phd", "gpa", "degree", "major",
        "entry level", "junior", "senior", "internship", "experience"
    },

    "certifications": {
        # Tech
        "security+", "network+", "a+", "aws certified", "ccna", "cissp",
        "scrum master", "pmp",
        # Healthcare
        "cpr", "bls", "emt", "cna", "rn",
        # Finance
        "cpa", "cfa", "series 7"
    },

    "soft_skills": {
        "communication", "leadership", "teamwork", "problem solving",
        "adaptability", "customer service", "time management",
        "attention to detail", "collaboration", "critical thinking",
        "work ethic", "interpersonal skills"
    },

    "action_verbs": {
        "led", "created", "designed", "implemented", "developed",
        "analyzed", "improved", "optimized", "managed", "coordinated",
        "supported", "built", "debugged", "maintained", "presented",
        "documented", "organized", "streamlined", "tested"
    }
}


#normalize data
def normalize(data: str) -> str:
    result = ""
    for char in data:
        if (char == "•" or char == "." or char == "," or char == "(" or char == ")" or char == ":"):
            continue
        result += char
    result = result.lower()
    return result

#convert string to list and clean up
def cleanup(data: str) -> list:
    ALL_KEYWORDS = set().union(*KEYWORDS.values())
    result = data.split()
    #remove junk words
    temp = set()
    for i in result:
        if i in ALL_KEYWORDS:
            temp.add(i)
    return list(temp)

#sort?



