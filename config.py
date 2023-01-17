import os
import paypalrestsdk

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AQzBqIRqVEJjCBT8GaLgwx6kIULtqzpBi30EhKy22tlllmrWxpxs_pUliXCYEzm_3ul5f3zJRWN_AL7J",
  "client_secret": "EEdf2mQmRW-euVNHRtLQPQqTJQ3uBnSs1ZJTcgXrApbD_fTfq4vGCJk3IgRdR8yF8VkP6-06HHs-PYm3" })

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 'db' : 'myflixvid' } # mongolocal
    
    # MONGODB_SETTINGS = { 'db' : 'myflix', "host":'mongodb://restheart:R3ste4rt!@34.142.32.93:80/myflix'} # gcloud
    # MONGODB_SETTINGS = { 'db' : 'myflix', "host":'http:34.142.32.93/myflix'} # gcloud