import re

def domain_name(url):
    # Use regular expression to extract the domain name
    match = re.search(r'(?:https?://)?(?:www\d?\.)?(?P<domain>[\w-]+)\.', url)
    
    if match:
        return match.group('domain')
    else:
        return ''
