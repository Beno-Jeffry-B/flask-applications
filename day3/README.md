
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



    