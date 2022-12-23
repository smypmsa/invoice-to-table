from celery import Celery


celery_app = Celery(__name__,
                    backend='redis://localhost',
                    broker='redis://localhost')
