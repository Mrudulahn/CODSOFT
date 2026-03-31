from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔴 Replace with your Adzuna credentials
APP_ID = "45cad28b"
API_KEY = "73c5bb69ad39e606484392d6d61b8750"


def get_jobs(skill):
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1?app_id={APP_ID}&app_key={API_KEY}&what={skill}&results_per_page=10"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "redirect_url": job.get("redirect_url")
        })

    return jobs


@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []

    if request.method == "POST":
        skills = request.form["skills"]
        jobs = get_jobs(skills)

    return render_template("index.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)