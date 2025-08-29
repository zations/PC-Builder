from django.apps import AppConfig
import threading

class PcpickerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pcpicker'

    def ready(self):
        from .Scrapper import run_web_scraper
        def run_once():
            if not getattr(run_once, 'done', False):
                run_web_scraper()
                run_once.done = True

        threading.Thread(target=run_web_scraper).start()

