## Flashes
#### Definition:

Shows one-time messages to the user like : "Form submitted successfully!" , "Invalid username or password." etc..
Is stored temporarily in session and Disappears after being shown once (like a flash)

Since it stores in session whenever we use session  `we must use secret key` (to get rid of error and as well as for protection) 

#### Basic Syntax and Explaination

##### app.py

* Import flash

* Use flash("message") inside the route

##### .html

```
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>
      {% for message in messages %}
        <li style="color: green;">{{ message }}</li>
      {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```


* get_flashed_messages() - This is a Flask function that retrieves all flash messages stored in the session. Once they are retrieved, they’re cleared automatically. You must call this inside the template to show the flashed messages.

* The `with block` creates a temporary variable messages to store the flashed messages.

* Why do we loop inside the if?

If your Flask route has:
```

            flash("Welcome, Jeffrey!")
            flash("Your profile is updated.")
            flash("Logout successful.")

```

Then get_flashed_messages() will return:
```
["Welcome, Jeffrey!", "Your profile is updated.", "Logout successful."]
```

so thats Why we loop and retrive the Flashes

#### Why is this inside the template?
Because the flash() happens in the Python code, but the display of the message must happen in HTML (template) using Jinja.



