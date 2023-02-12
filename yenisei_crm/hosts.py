import os

def get_allowed_hosts() -> list[str]:
    allowed_hosts = [
        'localhost',
        '127.0.0.1',
        '::1',
    ]

    custom_host = os.environ.get("Y_CRM_HOST", None)
    if custom_host is not None:
        allowed_hosts.append(custom_host)

    return allowed_hosts
