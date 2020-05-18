## MySql/MariaDB setup

#### The Vespa Project development server OS is Debian 9, with a MariaDb install
```
$ sudo apt update; sudo apt install mariadb-server
...

$ mysql --version
mysql  Ver 15.1 Distrib 10.1.44-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2
```

### 3 Steps Required for database setup
Once the mysql/maria DB is installed and running, the following three setup tasks must be performed:
 1) Create the database and Vespa users
 2) Create the "cve_records" table
 3) Import data from cve.csv file to "cve_records" table

**1) Create database and users**
First, edit mariadb/db_setup.mysql to add password strings, then execute:
```
 $ sudo mysql -p < mariadb/db_setup.mysql
```
This will drop/create the database name, **vespa**, and create a *read-only* and *read-write* user with appropirate access rights to the Vespa db tables. This will **NOT** create the tables - this is done separately using the CveRecord() model defined in database.py module as we want this CveRecord() model to be the single source of schema definition.

**2) Create the tables (from python vertual-env)**
```
 (venv) $ cd app
 (venv) $ python -c 'import database; database.create_tables(username="vespa_admin", password="*****")'
```

**3) Import CVE data from CSV file**
```
 (venv) $ cd app
 (venv) $ python -c 'import database; database.csv_to_sql(csv_filepath, username="vespa_rw", password="*****")'
>> TRUNCATING TABLE: cve_records
>> INSERTING: ['CVE-2020-0001', 'freeciv', '1.0.9', '1.1.1']
>> INSERTING: ['CVE-2020-0002', 'osquery', '0.8', '1.0']
>> INSERTING: ['CVE-2020-0003', 'freeciv', '1.1.2', '1.1.3']
>> INSERTING: ['CVE-2020-0004', 'photoshop', '2.0.9', '2.1.2']
>> INSERTING: ['CVE-2020-0005', 'flash', '0.0.1', '999.0']
>> INSERTING: ['CVE-2020-0006', 'pytwitter', '0.1.0', '0.1.2']
>> INSERTING: ['CVE-2020-0007', 'mint-linux', '2016.10', '2020.04']
```

