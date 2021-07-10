import time
import atexit

from apscheduler.scheduler import Scheduler
from client_secrets import API_URL, API_KEY, SEARCH_QUERY, test_vid
import logging
import requests
import json
from sqlite3 import IntegrityError




cron1 = Scheduler(daemon=True)
cron1.start()
atexit.register(lambda: cron1.shutdown(wait=False))




@cron1.interval_schedule(seconds=10)
def job_function():
    print("cron started")

    from db import get_db, close_db
    from task2 import app
    with app.app_context():
        db = get_db()
    
    final_url = API_URL+ "?key=" +API_KEY+ SEARCH_QUERY
    resp = requests.get(final_url)  
    
    result = json.loads(resp.content)

    
    if resp.status_code == 403:
        print(resp.status_code)
        print("Quota finished!!!!!!")
        result=test_vid

    vid = result.get("items")

    for item in vid:
        vid_id = item.get("id", {}).get("videoId", None)
        if not id:
            continue

        item_details = item.get("snippet", {})
        title = item_details.get("title")
        description = item_details.get("description")
        publish_time = item_details.get("publishTime")
        thumbnails = str(item_details.get("thumbnails"))

        # print("==============================================")

        # print(vid_id, title, description, publish_time, thumbnails)
        # ("==============================================")

        try:

            db.execute(
                'INSERT INTO vid (vid_id, title, description, publish_time, thumbnails) VALUES (?,?,?,?,?)', (vid_id, title, description, publish_time, thumbnails)
            )
        except IntegrityError as e:
            print("Video is already added!!!!!!")
            print(e)

        db.commit()
