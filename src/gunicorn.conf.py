from os import environ

# Logs
accesslog = '-'
access_log_format = r"%(h)s %(u)s %(t)s %(p)s '%(f)s' %(r)s %(s)s %(T)ss %(b)sB %(a)s"

# WSGI App
wsgi_app = environ.setdefault('APP_WSGI', 'project.wsgi')

# Server config
_HOST = environ.setdefault('APP_HOST', '127.0.0.1')
_PORT = environ.setdefault('APP_PORT', '8000')
bind = f'{_HOST}:{_PORT}'
# timeout = getenv("GUNICORN_TIMEOUT", "30")
# graceful_timeout = 30
# keepalive = 5
# worker_class = getenv("GUNICORN_WORKER_CLASS", "sync")
# workers = getenv("GUNICORN_WORKERS", multiprocessing.cpu_count() * 2 + 1)
max_requests = 500
max_requests_jitter = int(max_requests / 10)
