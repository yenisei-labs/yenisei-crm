import os

def get_allowed_hosts(add_scheme = False) -> list[str]:
    """Get a list of allowed hosts for security settings."""
    scheme = 'http://' if add_scheme else ''
    allowed_hosts = [
        scheme + 'localhost',
        scheme + '127.0.0.1',
        scheme + '::1',
    ]

    custom_host = os.environ.get("Y_CRM_HOST", None)
    if custom_host is not None:
        url = 'https://' + custom_host if add_scheme else custom_host
        allowed_hosts.append(url)

    return allowed_hosts
