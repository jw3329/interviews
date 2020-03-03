from flask import Flask, request

app = Flask(__name__)


def filter_email(email):
    # assumming it is gmail as always
    at_index = email.index('@')
    front_at = email[:at_index]
    filtered = ''
    for c in front_at:
        if c == '+': break
        elif c == '.': continue
        filtered += c
    return filtered


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'Post method needs to send data'
    elif request.method == 'POST':
        email_list = request.get_json()['email_list']
        email_set = set()
        for email in email_list:
            unique_username = filter_email(email)
            # skip the addition if it is not a vaild email format
            if unique_username: email_set.add(unique_username)
        return str(len(email_set))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)