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
<html>
<head>
<title>Profile</title>
<link rel="stylesheet" href="styles.css">
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
    }
    .bio-data {
      margin-top: 20px;
    }
    .label {
      font-weight: bold;
    }
    table {
      width: 100%;
      margin-top: 10px;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    .achievements {
      margin-top: 20px;
    }
  </style>
</head>
<body>

    
<div class="profile-container">
	<div class="profile-picture">
       <center> <img src="rini.jpg" alt="Profile Picture"></center>


    <div class="bio-data">
      <div class="label">Name:</div>
      <div>Abhidharini.R</div>
    </div>
    <div class="bio-data">
      <div class="label">Age:</div>
      <div>23</div>
    </div>
    <div class="bio-data">
      <div class="label">Address:</div>
      <div>Cuddalore</div>
    </div>
    <div class="bio-data">
      <div class="label">Email:</div>
      <div>abhidharini27@gmail.com</div>
    </div>
    <div class="bio-data">
      <div class="label">Phone:</div>
      <div>8754086301</div>
    </div>

    <!-- Education Table -->
    <div class="bio-data">
      <div class="label">Education:</div>
      <table>
        <tr>
          <th>Degree</th>
          <th>Institution</th>
          <th>Year</th>
        </tr>
        <tr>
          <td>Bachelor's</td>
          <td>Thiruvalluvar University</td>
          <td>2022</td>
        </tr>
        <tr>
          <td>HSC</td>
          <td>ST.Anne's</td>
          <td>2019</td>
        </tr>
      </table>
    </div>

    <!-- Achievements -->
    <div class="achievements">
      <div class="label">Achievements:</div>
      <ul>
        <li>Won Gold Medal in INFOMATRIx</li>
        <li>Got RAJIYA PURASHAKAR award in bharath scouts and guides</li>
      </ul>
    </div>

  </div>
	</div>


    </div>
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
