from matcher import calculate_match

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    resume = read_file("data/resumes/resume1.txt")
    job = read_file("data/job_descriptions/jd1.txt")

    score = calculate_match(resume, job)
    print(f"Resume–Job Match Score: {score}%")

    if score >= 70:
        print("Strong match – Recommended")
    elif score >= 40:
        print("Moderate match – Consider")
    else:
        print("Low match – Not recommended")
