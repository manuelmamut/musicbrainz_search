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
    **Content:** 
    ```
    {
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
    }
    ```
 
* **Error Response:**

  * **Code:** 404 NotFound <br />
    **Content:** `{ detail : "Not found" }`
    You will get this error when an artist_id is not found
    

  * **Code:** 400 <br />
    **Content:** `{"Request missing Artist ID":"You must pass an artist_id in your request"}`
    
 

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

