## Ideas for future versions

#### Additional resources

1) Pass a single CVE-id to retrieve CVE records (from CVE-datastores) for passed id:  
**GET /vespa/api/v2.X/data?cve=CVE-2020-0006**  
Response:
```
{ "cve_id": "CVE-2020-0006", "package": "pytwitter", "vulnerable_version": "0.1.0", "patched_version": "0.1.2" }
```

2) Post list of CVE-ids to retrieve CVE records for one or more CVE-ids:  
**POST /vespa/api/v2.X/data  { 'cve': [ "CVE-2020-0006", "CVE-2020-0001" ] }**   
Response:
```
 [ { "cve_id": "CVE-2020-0006", "package": "pytwitter", "vulnerable_version": "0.1.0", "patched_version": "0.1.2" }
   { "cve_id": "CVE-2020-0001", "package": "freeciv", "vulnerable_version": "1.0.9", "patched_version": "1.1.1" } ]
```

3) Pass a single package name to retrieve CVE records for passed package:   
**GET /vespa/api/v2.X/data?package=pytwitter**   
Response:
```
{ "cve_id": "CVE-2020-0006", "package": "pytwitter", "vulnerable_version": "0.1.0", "patched_version": "0.1.2" }
```

4) Post list of package names to retrieve CVE records from one or more packages:  
**POST /vespa/api/v2.X/data  { 'package': [ "freeciv", "photoshop" ] }**  
Response:
```
 [ { "cve_id": "CVE-2020-0006", "package": "pytwitter", "vulnerable_version": "0.1.0", "patched_version": "0.1.2" }
   { "cve_id": "CVE-2020-0004", "package": "photoshop", "vulnerable_version": "2.0.9", "patched_version": "2.1.2" } ]
```
