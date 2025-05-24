
Notes to keep up:
    * can absolutely use Flask in any directory on your system — both inside and outside current folder where we used pip install flask 
    * Flask installation is not tied to the folder , it’s tied to the Python environment(just the place where your Python and its packages live and run).
    * when do we use venv ??
            We use venv when we want to isolate project dependencies — so that packages used in one project don’t mess up other projects.
            For eg:

                Project A uses Flask 2.0
                Project B uses Flask 3.0

            If you install Flask globally, you can only have one version at a time, which can cause problems.
            But with venv, each project can have its own version of Flask (and other packages) — no conflicts!

    *how to create and activate venv
        >> python -m venv venv in the folder u are working with(curren folder)
        >> venv\Scripts\activate

    Here Below u can see that we are not using global env thats y flask is not found... is shown
    so install them seperatly in the current folder for avoid version Conflicts.

    (venv) PS C:\Users\jeffr\OneDrive\Desktop\SUMMER PROJECTS\web dev\flask-applications\day3> pip show flask
     WARNING: Package(s) not found: flask
    (venv) PS C:\Users\jeffr\OneDrive\Desktop\SUMMER PROJECTS\web dev\flask-applications\day3> 


### DAY 3 Challenges (TEMPLATES INHERITANCE)


### Challenge Faced

The image (`icon.png`) was not displaying in the HTML page when using Flask.

### How It Was Solved

The issue was due to placing the image inside the `templates/` folder. Flask requires all static files (images, CSS, JS) to be inside a folder named `static/`. After moving `icon.png` to the correct `static/` folder and using `{{ url_for('static', filename='icon.png') }}`, the image loaded successfully.

### Keep in Mind (FOLDER STRUCTURE IS THE KEY)

* Place HTML files in the `templates/` folder.
* Place images, CSS, and JS in the `static/` folder.
* Use `url_for('static', filename='yourfile')` to link static files.
* Maintain the correct folder structure:

  ```
  your_project/
  ├── app.py
  ├── templates/
  │   └── base.html
  └── static/
      └── icon.png
  ```

