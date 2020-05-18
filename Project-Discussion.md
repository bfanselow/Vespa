## Code-Project Design Discussion

The biggest challange in developing Vespa v1.0 was trying to determine how I wanted to store the CVE data on the service. I ended up settling for simple CSV-file storage for the first iteration of the service.  This choice brought up the issue of whether to load the CSV data once into app-context memory on service initialization or to reload it upon every request.  I decided to provide both options and make this choice a Config parameter.  The pro/cons of each choice are discussed in the code docstings as well as the *README*. With the two options I was able to compare performance based on batch-requesting the 100 payloads in the **example_post_data.json** file. Performance is discussed at the end of the *README*.

In a production environment with a very large CVE dataset, the ideal storage for this kind of service would probably be a local (or remote) database. However, there might be some situations where a database is less than ideal (even if providing better performance).  This led to the idea of making a CVE-data access-abstraction-layer, such that the CVE data could be stored in various storage formats, without having to make any code changes to the service - updating storage-type is simply a config-file setting.  The abstraction layer allows us to use a single, common set of data-access methods regardless of storage format.

Vespa v2.0 has the same basic architectureal design, but adds several new features:
 * adds  database to the available CVE data storage options, backed by a MySql (MariaDB) database
 * ETL functionality - transformations between the CSV and database formats
 * New "GET /vespa/api/v2.0/data/timestamp" resource to get last update timestamp of CVE data source
