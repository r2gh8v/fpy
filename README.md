# fpy

Download the repo in the directory of your choice or clone it to the the directory of your choice.<br>

Change the directoy to the one that you have added in the last step.<br>

If you do not have docker in your system, please follow <br>
https://docs.docker.com/engine/install/

If docker is present in your system:<br>

sudo docker run --name flask-fampay -p 5000:5000 flask-fampay

In case this doesn't work:<br>
  sudo docker ps -a<br>
  sudo docker rm -f <process id><br>
  
If there's no process, try building the image again:<br>
  sudo docker build --tag flask-fampay .<br>
  
And then run:<br>
  sudo docker run --name flask-fampay -p 5000:5000 flask-fampay


Get video API:
  http://127.0.0.1:5000/videos?offset=1
  1) Since there was no page number mentioned, I made the page size=2.
  2) the response will contain a "next_offset" field which can be passed to the api in "offset" query parameter yielding the desired results.
  3) API key limit was exhausted and on creation of new api keys as well I was not able to hit the API, I have added a test json in case the quoata is still not
      renewed. I was not able to test at the end with the live youtube API hence it might break.
  
  
Search API:
  http://127.0.0.1:5000/search?title=look&description=look
  1) title specify the words that you wish to be searched in title.
  2) description specify the words that you wish to be searched in description.
  3) If neither title nor description is present, the response will contain an error keyword.
  

