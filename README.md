# VESPA
### Vulnerable or Exposed Software-Package Analyzer

<img src="https://github.com/bfanselow/Vespa/blob/master/img/vespa.png" width="180" height="238">

### Latest version: 2.0

#### Major changes from v1.0
 * Added support for database storage.
 * Added ETL methods for transforming data storage formats (CSV->database, database->CSV).
 * Added new **GET /data/timestamp** to get the timestamp of last CVE data update. 

--- 
## Summary
*VESPA* is a simple Python3/Flask API for assessing whether or not a software-package with a specific version number is vulnerable or exposed based on CVE data stored on the *VESPA* server.  Clients pass a JSON payload containing a list of **package-version-host** objects to the Vespa-API. Each package-version-host object contains a software-package, its version and the host on which it is installed (which is the same for all objects in a specific payload). *VESPA* analyzes each package-version-host object and returns a list of CVE-ids (if any) associated with the vulnerable package-version pairs from the input (see **Details** section below for more in-depth on the service design, operation and requets/response formats).

---
## Requirements
 Python 3.6+

 pip install:
 * pandas
 * pytest
 * jsonschema
 * packaging
 * flask==1.1.2 (auto-installs lots of other pkgs)

### If using database storage
 * MySql/MariaDB backend database (i.e. "sudo apt update; sudo apt install mariadb-server" on Deb9) 
 * pip install flask_sqlalchemy 
 * pip install mysql-connector-python

---
## Setup
```
 $ git clone https://github.com/bfanselow/Vespa.git
 $ cd Vespa/
 $ virtualenv -p python3.6 venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
```

### Database setup (if using database storage)
 1) See **mariadb/README** for information on mysql install, creating the database, *Vespa* db-users, table, and importing data from csv-file.
 2) Configure all database parameters in **app.config.STORAGE_ARGS['database']** used in STEP 1.
 

---
### Running the Service
Start the Flask service with development server from **Vespa/app** dir.  **(NOT for production!)**   
```
 (venv) $ cd app/
 (venv) $ python vespa_flask.py 
```

**Production environment**  
See documentation in *vespa-flask.wsgi* for running service with Apache

---
### Client-side use of VESPA 
#### Identifying vulnerable packages in a single *package-version-host* list:
Call the service directly:
```
 $ curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{ "data": [{p_obj1}, ... {p_obj1}] }'
```

#### Assessing vulnerable packages in multiple *package-version-host* lists contained in a file:
Use the batch-processing script to iterate over a file list of *package-version-host* lists:
```
 (venv) $ ./vespa_batch_run.sh file=example_post_data.json
```

#### Re-initializing CVE data for file updates without shutting off service **(More discussion on this below)**
```
 $ curl -s http://127.0.0.1:8080/vespa/api/v2.0/data/refresh -H "X-Api-Key: ******" 
```
**See config for API-key**

---
## Testing
#### Unit
From the **Vespa** project base directory run all test_* files in *tests/unit* dir:
```
(venv) $ python -m pytest -v tests/unit
```

#### Integration 
From the **Vespa** project base directory run all test_* files in *tests/integration* dir:
```
(venv) $ python -m pytest --setup-show -v tests/integration
```

#### Functional 
From **Vespa** project base directory    
1) Batch-run on **example_post_data.json** 
```
 $ ./vespa_batch_run.sh file=example_post_data.json | tee RESULTS.batch-example-post

 # Show commands and preformance stats - run in verbose mode
 $ ./vespa_batch_run.sh  -v file=example_post_data.json | tee RESULTS-VERBOSE.batch-example-post
```
2) Batch run of various remote requests to all resources to verify error-handling, etc.  
Run this for both config.STORAGE_TYPE settings: **csv** and **database**
```
 $ tests/functional/curl_remote_requests.sh | tee curl-test.out 
```

---
## VESPA Details

#### Process Flow Summary
The *VESPA* Flask app routing engine passes the Posted "package-version-host" list payload to **cve_analysis.analyze_vulnerable_package_list()** along with a CVE-data-access object.  For each "package-version-host" object in the list, the package's CVE records are retrieved from the data-access object. The input package's version is compared to the affected-versions for that package by methods in **version_math.py**. If the package version is found to be affected, the assocated CVE information is added to a response object of all affected packages from the input payload list.  This object is returned as a JSON by the Flask app. 

#### Storage formats
*VESPA* currently supports multiple different CVE data storage formats:
  * CSV file
  * Local or remote database    

Future versions could include Yaml, remote-API, etc. 

#### Storage Access
*VESPA* accesses stored CVE data via a data-absraction-layer (CVE-data-handler) which provides the flexibility for storing the CVE data in different storage formats while using a single set of common data-access methods independent of the choice of storage format. This abstraction-layer also gives flexibility on how we load and query the data. For CSV file storage we can configure the data-handler to refresh the data on every query, or load it once into app memory upon app initialization and make queries to in-memory objects. Obviously, there are PROS/CONS to each option as discussed in **app/cve_data_abstraction.py**. Optimal performance can probably be achieved by using a database format especially as the number of CVE records gets very large.

#### Storage Configurations
The main Flask config file holds storage configurations including which type of storage-format to use and the parameters assocated with each type - CVE-file path, database params, etc.

An important config parameter when using CSV-file storage is **persist**:
 * *persist=True*: CSV data will be loaded once on init and remain in app-context memory for all queries. This has performance advantages but opens the risk of making queries to stale data (if/when new CVE data is added).  Use the **GET /data/refresh** API resource to keep up with data updates. 
 * *persist=False*: CSV data will be re-loaded prior to every query. This essentially eliminates (though not 100%) the issue of stale data, but create performance problems, especially when the size of the file gets large (see **Performance** section below). 

#### Storage Schema
CVE data used by *VESPA* must be stored with the following four-column schema:
 1) **CVE** (string):  CVE-id
 2) **package** (string): name of software-package
 3) **vulnerable_version** (string): *first* vulnerable version of the package
 4) **patched_version** (string): *first* patched version of the package

### API Details 
*VESPA's* API makes available two GET methods and one POST method:
 * **POST /vespa/api/v2.0/vuln**
 * **GET  /vespa/api/v2.0/data/refresh**
 * **GET  /vespa/api/v2.0/data/timestamp**

#### POST /vespa/api/v2.0/vuln 
This method is used to POST a list of (package-version-host) objects containing package-name, version and host on which the package is installed.  **No authorization** is required to access this resource.  
**Example payload:**
```
  { "data": [{"package": "freeciv", "version": "1.4.0", "host": "330facf12c55432d9f7eed27c5448ac8.example.org"}, {"package": "mint-linux", "version": "2016.3.0", "host": "330facf12c55432d9f7eed27c5448ac8.example.org"}] }
```
For each object in the list, *VESPA* will perform a lookup in it's CVE data stores for the package-name and identify if the input version is inside the **vulnerable-version-window** for that package. *VESPA* defines this "vulnerable-version-window" as follows:  if the version is greater than or equal to the first vulnerable version and less than the first patched version, it is inside the vulnerable-version-window and is therefore affected by that CVE.

The **@api_validation** route-decorator validates the format of the input payload prior to processing, using **jsonschema** to perform the validation. 

The response to this request is a JSON which identifies the hostname (from the input payload) and a list of all of the CVE ids that were found to be vulnerable (inside the vulnerable-version-window).  
**Example response:** 
```
{"748a370a9bb644629fefdb78045be5cf.example.org": ["CVE-2020-0004", "CVE-2020-0006"]}
```
If none of the packages from the input payload are identified as vulnerable the response is an empty JSON object: **{}**

#### GET /vespa/api/v2.0/data/refresh  
**Requires API-key in request Headers**    
This method can be used to re-initialize CVE data storage without having to restart the service. For CSV file storage this involves re-reading and re-loading the file data into the Flask app object, and should be auto-triggered anytime a file-update is made.  For database storage, this involves dropping and re-initializing the database connection, which is useful in the event of a change to the backend database connection parameters (i.e. password change, etc.).   

This method does require an API-KEY (set in Flask config) to be passed in the request HEADERS. This is not intended to be a strong Seucrity measure. Rather it serves as a demo/stub for future API-authorization capability, since performing a re-initialization of the CVE data from the API needs to have some authorization mechanism in place. 

**Example request without the API-key:** 
```
 $ /usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/data/refresh
{"error":{"exception":"ApiAuthorizationError","message":"API request authorization failed: no api-key in payload or headers","timestamp":"2020-05-14 13:56:51"}}
```

**Example request with the API-key:** 
```
 $ /usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/data/refresh -H "X-Api-Key: William.Fanselow.Vespa.1.0"
{"status":true}
```

#### GET /vespa/api/v2.0/data/timestamp  
**No authorization required**    
This method is used to retrieve the timestamp of the last CVE source-data update, and the storage-format-type. For CSV file storage this is the file-modification time of the CSV file. For database storage this is the **max(timestamp)** for all rows in the **cve_records** table.   
**Example response:** 
```
 $ /usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/data/timestamp
{"last_update":"2020-05-16 17:51:10","storage_type":"csv"}
```

---
### VESPA Performance
#### CSV Storage
Numerous executions of **./vespa_batch_run.sh -v file=example_post_data.json** were performed with timing stats enabled to evaluate service performance (both with **persist=True** and **persist=False**).

With **persist=True** (only load the CVE data on init) runs were able to process the 100 requests in about 2 seconds.   
```
lines-processed: 100 example_post_data.json.  Start: Thu May 14 12:37:46 UTC 2020   End: Thu May 14 12:37:48 UTC 2020 
```
With **persist=False** (reload on every query) the same batch-run typically took 3-4 seconds (50%-100% increase).

#### Database Stroage
Multiple executions of **./vespa_batch_run.sh -v file=example_post_data.json** were processed in 1-2 seconds.
```
STATS: lines-processed: 100 example_post_data.json.  Start: Mon May 18 21:33:58 UTC 2020   End: Mon May 18 21:34:00 UTC 2020
```
While this is not much better than the CSV file processing, I would expect the database storage to outperform the file storage when the number of CVE records gets very large - I would expect that the Pandas-based file-load and query, **(df.loc[df['package'] == package_name])** will eventually lag compared to database queries with indexed records.
