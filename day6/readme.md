
day 5 we have studied about standard project structure

### Day 6
#### Flask Forms

There are two methods we can create a form

* NormalHTML forms (Manual Method)
            
                        | Step | What Happens                                 |
            | ---- | -------------------------------------------- |
            | 1    | HTML form sends POST request with user input |
            | 2    | Flask route detects method as POST           |
            | 3    | `request.form` extracts submitted data       |
            | 4    | Data is saved using SQLAlchemy               |
            | 5    | Redirect to GET route to avoid re-submission |
            
* Using wtf library


