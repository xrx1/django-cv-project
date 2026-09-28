# Django CV Project

This project converts my CV into a web page using Django and Django Templates.

## Demo

A short demo video of the Django CV website is included below.


## Project Overview

This project presents my education, work experience, internships, competitions, projects, and technical skills as a web-based CV.

The page is built with HTML and CSS, while Django is used to provide the CV data and render the HTML template.

## How Django Is Used

### 1. Django Project and Application

The project is organized as a Django project called `cv_project` with an application called `cv`.

The main CV page is connected to the Django view through `urls.py`:

    path('', cv)

This maps the home page to the `cv` view.

### 2. Django View

The main view is defined in `cv/views.py`.

The CV information is stored in a Python dictionary called `context`:

    context = {
        "name": "Ruixin Xu",
        ...
    }

The context is passed to the Django template using:

    return render(request, "cv.html", context)

This allows the template to use the CV information provided by the Python code.

### 3. Django Template Variables

I used Django Template variables to display information from the `context` dictionary.

For example:

    <h1>{{ name }}</h1>

Other examples include:

    {{ experience.company }}
    {{ experience.position }}
    {{ project.name }}

The values are provided by the Django view instead of being written directly into the HTML.

### 4. Django Template Loops

I used Django Template `for` loops to generate repeated sections of the CV.

For example:

    {% for experience in experiences %}

        <h3>{{ experience.position }}</h3>
        <p>{{ experience.company }}</p>

    {% endfor %}

I also used nested loops for projects and project descriptions:

    {% for project in experience.projects %}

        <h4>{{ project.name }}</h4>

        {% for item in project.description %}
            <li>{{ item }}</li>
        {% endfor %}

    {% endfor %}

This allows the HTML structure to be reused for multiple experiences, projects, and descriptions.

### 5. Template-Based Data Rendering

Instead of writing each CV section repeatedly in HTML, the information is stored as Python data in `views.py`.

Django then uses the template to generate the corresponding HTML page.

The basic data flow is:

    views.py
        ↓
    context dictionary
        ↓
    cv.html
        ↓
    Django Template
        ↓
    Rendered CV webpage

## Technologies Used

- Python
- Django
- HTML
- CSS

## Project Structure

    cv_project/
    │
    ├── manage.py
    │
    ├── cv/
    │   ├── views.py
    │   ├── templates/
    │   │   └── cv.html
    │   └── ...
    │
    ├── cv_project/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    │
    └── db.sqlite3

## How to Run the Project

### 1. Install Django

Make sure Python and Django are installed.

    pip install django

### 2. Open the Project Directory

Open the `cv_project` directory in Visual Studio Code.

### 3. Start the Django Development Server

Run:

    python manage.py runserver

### 4. Open the Website

Open the following address in a web browser:

    http://127.0.0.1:8000/
