from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

PROJECTS = [
    {
        "slug": "drone-club",
        "title": "Aerial Drone Competition",
        "description": "Led autonomous drone navigation code (Java/Python) and flight-control tuning; advanced to Captain of an all-girls team, earning multiple awards.",
        "tags": ["Python", "Java", "Autonomous Navigation", "Leadership"],
        "image": "images/drone-club.jpg",
    },
    {
        "slug": "robotics",
        "title": "First Tech Challenge Robotics",
        "description": "Team Captain for FTC robot design, construction, and Java tele-op programming integrating motors, servos, and control systems.",
        "tags": ["Java", "CAD", "Mechanical Engineering", "Leadership"],
        "image": "images/robotics.png",
    },
    {
        "slug": "astrobee",
        "title": "MIT Zero Robotics — Astrobee",
        "description": "Finalists in the Agriculture Challenge, programming a microgravity Astrobee robot in C++ for crop management, navigation, and task prioritization under 240-second constraints.",
        "tags": ["C++", "Autonomous Navigation", "Space", "Agriculture"],
        "image": "images/astrobee.png",
    },
    {
        "slug": "molecular-docking",
        "title": "Molecular Docking Research",
        "description": "Screened 200 natural compounds against the Delta Opioid Receptor (AutoDock Vina), identifying 15 top candidates for pain management and opioid-use disorder treatment.",
        "tags": ["AutoDock Vina", "Computational Biology", "Research"],
        "image": "images/molecular-docking.png",
    },
    {
        "slug": "embedded-systems",
        "title": "Embedded Systems Dashboard",
        "description": "Built a vehicle dashboard GUI in C++/Qt on a Raspberry Pi with climate control, speedometer, and hazard lights; wired GPIO circuits for physical button/LED interaction.",
        "tags": ["C++", "Qt", "Raspberry Pi", "GPIO"],
        "image": "images/embedded-systems.svg",
        "video": "videos/embedded-systems.mp4",
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


@app.route("/contact", methods=["POST"])
def contact():
    return redirect(url_for("index", sent=1) + "#contact")


if __name__ == "__main__":
    app.run(debug=True)
