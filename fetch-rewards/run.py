from flask import Flask, request

app = Flask(__name__)


def filter_email(email):
    # if at is not a valid email, return empty string
    if '@' not in email: return ''
    at_index = email.index('@')
    front_at = email[:at_index]
    filtered = ''
    for c in front_at:
        if c == '+': break
        elif c == '.': continue
        filtered += c
    return filtered + email[at_index:]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'Post method needs to send data'
    elif request.method == 'POST':
        json_data = request.get_json()
        if 'email_list' not in json_data:
            return 'email_list is not in the given request'
        email_list = json_data['email_list']
        email_set = set()
        for email in email_list:
            filtered_email = filter_email(email)
            # skip the addition if it is not a vaild email format
            if filtered_email: email_set.add(filtered_email)
        return str(len(email_set))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)