### Forget Password implementation

#### Library

```
pip install itsdangerous
```

#### Generation of expiration link

```
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
```

In the above library there's no such thing called TimedJSONWebSignatureSerializer anymore now it was used in older verisons


#### Instead To below

```
from itsdangerous import URLSafeTimedSerializer

def generate_token(email):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps({'email': email})

```



* URLSafeTimedSerializer - It generates a time-sensitive and URL-safe token(Bases On Secret Key ) , It uses your app’s SECRET_KEY to ensure that no one else can tamper with the token.

    >`s = URLSafeTimedSerializer(app.config['SECRET_KEY']) `

So now s is an object that can encrypt and decrypt data securely.


* s.dumps({'email': email})

it passes the email(in a encrpyted form ) inside the token  (which is generated and stored in obj s in previous step..)

but why to pass email why not send a random str..? Becase later that encrypted string is passed into resetpassword route and from which email is Decoded (verify) the token to get back the email stored inside.



#### verification Phase:
```
def verify_token(token, max_age=1800):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token, max_age=max_age)
        return data['email']
    except Exception:
        return None
```

* s.loads() tries to decode the token.
* token is only valid for 1800 seconds (30 minutes).
* if the token is expired, invalid, or corrupted, this returns None.















