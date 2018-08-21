# musicbrainz_search

## Install

- To start the project create a virtualenv: `virtualenv musicbrainz_dev -p python3`

- Once in your virtualenv run `pip install -r requirements_<environment>_.txt`  
  (so far we have 'dev' an 'qa' environments)

- To run the project `python manage.py runserver <your_host>:<your_port> --settings=musicbrainz.settings.<environment>`


## Caching

   We use LocalMemCached for development environment and Memcache for qa environment.  
   You must install memcache in order to be able to cache on QA env.  

   Probably it could be already running if you are working of linux, you could check it  
   by running `netstat -antlp` on bash and search for a process listening on 127.0.0.1:11211

## Tests

  You can run the tests by going to the project folder 'musicbrainz' and run  
  `python manage.py test --settings=musicbrainz.settings.<environment>`
  
## Endpoints

**Release Groups**
----
Use this to get the Release Groups for an Artist. You can use pagination with this resource

* **URL**

  /release-groups/

* **Method:**
  
  `GET` 
  
*  **URL Params**

   **Required:**
 
   `artist_id = MB artist ID`

   **Optional:**
 
   `offset=[integer]`
   `limit=[integer]`

* **Data Params**

  NONE

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "albums": [
        {
            "id": "0da580f2-6768-498f-af9d-2becaddf15e0",
            "title": "Ride the Lightning",
            "year": 1984,
            "release_count": 37  
        }
    ],
    "next_offset": 2,  
    "showing": "1-1",  
    "release_group_count": 577,  
    "date": "2018-08-21T18:24:06.108140Z"  
    }`
 
* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in" }`

  OR

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{ error : "Email Invalid" }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/release-groups/?artist_id=65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab&limit=1&offset=1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

* **Notes:**

This endpoint caches every call for 15 minutes. You can use `/release-groups-nocache/`if you don't want to cache the call
