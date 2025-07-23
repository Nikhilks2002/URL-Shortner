import random
import string
import re

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    pattern = re.compile(
        r'^(http|https)://'  # http:// or https://
        r'([\w.-]+)'         # domain
        r'([/\w.-]*)*/?$'    # path
    )
    return re.match(pattern, url) is not None
