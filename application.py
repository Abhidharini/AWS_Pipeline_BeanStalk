import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jenish Revaldo C - Data Analyst Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
        }

        h1 {
            font-size: 28px;
        }

        h2 {
            font-size: 24px;
            margin-top: 10px;
        }

        h3 {
            font-size: 20px;
            margin-top: 10px;
        }

        p {
            margin: 5px 0;
        }

        .contact {
            margin-top: 20px;
        }

        .education, .projects, .languages, .interests {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <h1>Jenish Revaldo C   -  Data Analyst</h1>
  
    <p>Driven and adaptable Data Analyst with a passion for continuous learning and leadership. Skilled in mathematics, statistics, and programming, I excel at solving complex problems and extracting valuable insights from data. Committed to staying updated on industry trends to deliver impactful data-driven solutions.</p>
    
    <div class="contact">
        <h2>Contact Information</h2>
        <p>Email: jenishrev0603@gmail.com</p>
        <p>Phone: 7358941365</p>
        <p>Location: Kanyakumari, India</p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/jenish-revaldo-c-004670245">linkedin.com/in/jenish-revaldo-c-004670245</a></p>
        <p>GitHub: <a href="https://github.com/JenishRevaldo">github.com/JenishRevaldo</a></p>
    </div>

    <div class="education">
        <h2>Education</h2>
        <h3>B.Sc. Mathematics</h3>
        <p>Loyola College</p>
        <p>06/2019 - 04/2022, Chennai</p>
        <p>Graduate with a first-class degree.</p>

        <h3>M.Sc. Data Science</h3>
        <p>Loyola College</p>
        <p>06/2022 - Present, Chennai</p>
        <p>Pursuing degree in data Science with a commendable CGPA.</p>
    </div>

    <div class="projects">
        <h2>Projects</h2>
       <p>IPL Analysis through Power BI</p>
        <p>Supervised-Unsupervised integration for Breast Cancer diagnosis</p>
    </div>

    <div class="languages">
        <h2>Languages</h2>
        <p>Tamil - Native or Bilingual Proficiency</p>
        <p>English - Full Professional Proficiency</p>
    </div>

    <div class="interests">
        <h2>Interests</h2>
        <p>Data Analysis</p>
        <p>Predictive Modelling</p>
        <p>Natural Language Processing</p>
        <p>Data Visualization</p>
    </div>
</body>
</html>
"""


def application(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'],
                            environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
