#### Results from ./vespa_batch_run.sh -v file=example_post_data.json
---
```
/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.7.0", "host": "2b09375594f9499698a39749ec773c3f.example.org"}, {"package": "mint-linux", "version": "2012.6.0", "host": "2b09375594f9499698a39749ec773c3f.example.org"}, {"package": "osquery", "version": "2.7.5", "host": "2b09375594f9499698a39749ec773c3f.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.2", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "photoshop", "version": "2.1.1", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "flash", "version": "78.3.9", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}, {"package": "mint-linux", "version": "2015.2.0", "host": "74d2d85b57664f819ccea15b57fed5c0.example.org"}]}'
{"74d2d85b57664f819ccea15b57fed5c0.example.org":["CVE-2020-0003","CVE-2020-0004","CVE-2020-0001","CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2012.2.0", "host": "13a67708e0f14d10b7091e5c6ab75906.example.org"}, {"package": "osquery", "version": "2.3.1", "host": "13a67708e0f14d10b7091e5c6ab75906.example.org"}, {"package": "freeciv", "version": "2.8.8", "host": "13a67708e0f14d10b7091e5c6ab75906.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "13a67708e0f14d10b7091e5c6ab75906.example.org"}, {"package": "freeciv", "version": "1.3.9", "host": "13a67708e0f14d10b7091e5c6ab75906.example.org"}, {"package": "photoshop", "version": "0.0.0", "host": "13a67708e0f14d10b7091e5c6ab75906.example.org"}]}'
{"13a67708e0f14d10b7091e5c6ab75906.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.0", "host": "3f0be76cbc2c46fea90c335b8a2d7ed1.example.org"}, {"package": "freeciv", "version": "0.5.0", "host": "3f0be76cbc2c46fea90c335b8a2d7ed1.example.org"}, {"package": "osquery", "version": "0.7.3", "host": "3f0be76cbc2c46fea90c335b8a2d7ed1.example.org"}]}'
{"3f0be76cbc2c46fea90c335b8a2d7ed1.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.0.9", "host": "34a5bf0669ce4f4888477377dc1a4eeb.example.org"}, {"package": "freeciv", "version": "0.4.2", "host": "34a5bf0669ce4f4888477377dc1a4eeb.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "34a5bf0669ce4f4888477377dc1a4eeb.example.org"}, {"package": "osquery", "version": "0.8.9", "host": "34a5bf0669ce4f4888477377dc1a4eeb.example.org"}, {"package": "flash", "version": "401.1.7", "host": "34a5bf0669ce4f4888477377dc1a4eeb.example.org"}]}'
{"34a5bf0669ce4f4888477377dc1a4eeb.example.org":["CVE-2020-0004","CVE-2020-0003","CVE-2020-0002","CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "0.7.1", "host": "f5711a942c3e455287a2bc16b7ec5d9b.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "1.2.0", "host": "df1ed4ee4c364b2483261c404f5ba453.example.org"}, {"package": "freeciv", "version": "1.3.4", "host": "df1ed4ee4c364b2483261c404f5ba453.example.org"}, {"package": "pytwitter", "version": "0.1.0", "host": "df1ed4ee4c364b2483261c404f5ba453.example.org"}]}'
{"df1ed4ee4c364b2483261c404f5ba453.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.9.5", "host": "d1783b2b4fd448cebddeb096bbc80ae9.example.org"}]}'
{"d1783b2b4fd448cebddeb096bbc80ae9.example.org":["CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.0.2", "host": "f5fc93782bf74d75be0226963ab55fb4.example.org"}, {"package": "osquery", "version": "2.9.3", "host": "f5fc93782bf74d75be0226963ab55fb4.example.org"}, {"package": "freeciv", "version": "0.9.6", "host": "f5fc93782bf74d75be0226963ab55fb4.example.org"}, {"package": "pytwitter", "version": "2.6.7", "host": "f5fc93782bf74d75be0226963ab55fb4.example.org"}, {"package": "freeciv", "version": "0.5.8", "host": "f5fc93782bf74d75be0226963ab55fb4.example.org"}, {"package": "mint-linux", "version": "2014.2.0", "host": "f5fc93782bf74d75be0226963ab55fb4.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.2", "host": "cd559c3472c140ee9405d5df4cd00132.example.org"}, {"package": "freeciv", "version": "1.1.0", "host": "cd559c3472c140ee9405d5df4cd00132.example.org"}, {"package": "pytwitter", "version": "1.7.1", "host": "cd559c3472c140ee9405d5df4cd00132.example.org"}, {"package": "photoshop", "version": "2.9.0", "host": "cd559c3472c140ee9405d5df4cd00132.example.org"}, {"package": "osquery", "version": "0.8.3", "host": "cd559c3472c140ee9405d5df4cd00132.example.org"}]}'
{"cd559c3472c140ee9405d5df4cd00132.example.org":["CVE-2020-0003","CVE-2020-0001","CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "1.0.8", "host": "edd1c8fae1f5481287771dcbd7724ac9.example.org"}, {"package": "photoshop", "version": "2.0.9", "host": "edd1c8fae1f5481287771dcbd7724ac9.example.org"}, {"package": "freeciv", "version": "2.6.4", "host": "edd1c8fae1f5481287771dcbd7724ac9.example.org"}, {"package": "mint-linux", "version": "2014.1.0", "host": "edd1c8fae1f5481287771dcbd7724ac9.example.org"}, {"package": "osquery", "version": "0.8.2", "host": "edd1c8fae1f5481287771dcbd7724ac9.example.org"}]}'
{"edd1c8fae1f5481287771dcbd7724ac9.example.org":["CVE-2020-0004","CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2011.2.0", "host": "6374fb1c428241da9c9916776b6f6d08.example.org"}, {"package": "freeciv", "version": "2.0.3", "host": "6374fb1c428241da9c9916776b6f6d08.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "6374fb1c428241da9c9916776b6f6d08.example.org"}, {"package": "pytwitter", "version": "2.9.9", "host": "6374fb1c428241da9c9916776b6f6d08.example.org"}, {"package": "osquery", "version": "0.9.3", "host": "6374fb1c428241da9c9916776b6f6d08.example.org"}, {"package": "photoshop", "version": "2.7.7", "host": "6374fb1c428241da9c9916776b6f6d08.example.org"}]}'
{"6374fb1c428241da9c9916776b6f6d08.example.org":["CVE-2020-0001","CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "2.9.7", "host": "748a370a9bb644629fefdb78045be5cf.example.org"}, {"package": "freeciv", "version": "0.7.4", "host": "748a370a9bb644629fefdb78045be5cf.example.org"}, {"package": "mint-linux", "version": "2012.10.0", "host": "748a370a9bb644629fefdb78045be5cf.example.org"}, {"package": "photoshop", "version": "2.1.1", "host": "748a370a9bb644629fefdb78045be5cf.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "748a370a9bb644629fefdb78045be5cf.example.org"}]}'
{"748a370a9bb644629fefdb78045be5cf.example.org":["CVE-2020-0004","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.7.7", "host": "cb74feabc26f4a6eb7b774c83814a8af.example.org"}, {"package": "osquery", "version": "0.5.6", "host": "cb74feabc26f4a6eb7b774c83814a8af.example.org"}, {"package": "freeciv", "version": "1.8.4", "host": "cb74feabc26f4a6eb7b774c83814a8af.example.org"}, {"package": "freeciv", "version": "1.6.3", "host": "cb74feabc26f4a6eb7b774c83814a8af.example.org"}, {"package": "mint-linux", "version": "2010.5.0", "host": "cb74feabc26f4a6eb7b774c83814a8af.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2017.2.6", "host": "3b37b83a2e484f4b88ece02627e951e3.example.org"}, {"package": "pytwitter", "version": "2.0.6", "host": "3b37b83a2e484f4b88ece02627e951e3.example.org"}, {"package": "freeciv", "version": "1.3.8", "host": "3b37b83a2e484f4b88ece02627e951e3.example.org"}]}'
{"3b37b83a2e484f4b88ece02627e951e3.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.7.7", "host": "d33dcfcffbbc4f7e868462f3c6c54fa2.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "2.9.4", "host": "67714828f5494e89a3def8a14ad78eb8.example.org"}, {"package": "photoshop", "version": "0.0.7", "host": "67714828f5494e89a3def8a14ad78eb8.example.org"}, {"package": "freeciv", "version": "1.7.9", "host": "67714828f5494e89a3def8a14ad78eb8.example.org"}, {"package": "mint-linux", "version": "2014.8.0", "host": "67714828f5494e89a3def8a14ad78eb8.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "1.1.2", "host": "e83badd357dc4b38937a3fd367ddaa65.example.org"}, {"package": "freeciv", "version": "2.0.0", "host": "e83badd357dc4b38937a3fd367ddaa65.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.3.9", "host": "e5bee0d9321842d780e09dcdfdf0d5ee.example.org"}, {"package": "freeciv", "version": "2.3.1", "host": "e5bee0d9321842d780e09dcdfdf0d5ee.example.org"}, {"package": "pytwitter", "version": "0.2.0", "host": "e5bee0d9321842d780e09dcdfdf0d5ee.example.org"}, {"package": "freeciv", "version": "1.4.3", "host": "e5bee0d9321842d780e09dcdfdf0d5ee.example.org"}, {"package": "photoshop", "version": "0.0.0", "host": "e5bee0d9321842d780e09dcdfdf0d5ee.example.org"}, {"package": "mint-linux", "version": "2017.1.5", "host": "e5bee0d9321842d780e09dcdfdf0d5ee.example.org"}]}'
{"e5bee0d9321842d780e09dcdfdf0d5ee.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "0.9.4", "host": "92897825d03a472e895313dfe767388a.example.org"}, {"package": "osquery", "version": "1.1.2", "host": "92897825d03a472e895313dfe767388a.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "0.1.0", "host": "461edbf822414620bda71d4d682fe4d5.example.org"}, {"package": "osquery", "version": "0.8.2", "host": "461edbf822414620bda71d4d682fe4d5.example.org"}, {"package": "photoshop", "version": "2.5.2", "host": "461edbf822414620bda71d4d682fe4d5.example.org"}, {"package": "mint-linux", "version": "2015.3.0", "host": "461edbf822414620bda71d4d682fe4d5.example.org"}]}'
{"461edbf822414620bda71d4d682fe4d5.example.org":["CVE-2020-0006","CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "flash", "version": "571.9.3", "host": "b341e8f7e8034328bf6e46d039acd1b3.example.org"}, {"package": "freeciv", "version": "2.6.0", "host": "b341e8f7e8034328bf6e46d039acd1b3.example.org"}, {"package": "mint-linux", "version": "2018.4.9", "host": "b341e8f7e8034328bf6e46d039acd1b3.example.org"}, {"package": "osquery", "version": "2.8.7", "host": "b341e8f7e8034328bf6e46d039acd1b3.example.org"}, {"package": "freeciv", "version": "1.3.3", "host": "b341e8f7e8034328bf6e46d039acd1b3.example.org"}, {"package": "photoshop", "version": "2.1.0", "host": "b341e8f7e8034328bf6e46d039acd1b3.example.org"}]}'
{"b341e8f7e8034328bf6e46d039acd1b3.example.org":["CVE-2020-0005","CVE-2020-0007","CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.0.5", "host": "90895d2e7ded47149a3a29d7bc2011ac.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "90895d2e7ded47149a3a29d7bc2011ac.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "90895d2e7ded47149a3a29d7bc2011ac.example.org"}]}'
{"90895d2e7ded47149a3a29d7bc2011ac.example.org":["CVE-2020-0006","CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.6.0", "host": "fe5131e24b57410084e62d686fc76b20.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "fe5131e24b57410084e62d686fc76b20.example.org"}, {"package": "osquery", "version": "0.3.0", "host": "fe5131e24b57410084e62d686fc76b20.example.org"}, {"package": "mint-linux", "version": "2013.2.0", "host": "fe5131e24b57410084e62d686fc76b20.example.org"}, {"package": "pytwitter", "version": "0.5.3", "host": "fe5131e24b57410084e62d686fc76b20.example.org"}, {"package": "photoshop", "version": "1.5.7", "host": "fe5131e24b57410084e62d686fc76b20.example.org"}]}'
{"fe5131e24b57410084e62d686fc76b20.example.org":["CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "2.5.4", "host": "a41604fb0e634523ab0c3a709243bbd1.example.org"}, {"package": "pytwitter", "version": "1.1.7", "host": "a41604fb0e634523ab0c3a709243bbd1.example.org"}, {"package": "freeciv", "version": "2.7.1", "host": "a41604fb0e634523ab0c3a709243bbd1.example.org"}, {"package": "freeciv", "version": "2.3.2", "host": "a41604fb0e634523ab0c3a709243bbd1.example.org"}, {"package": "photoshop", "version": "0.6.3", "host": "a41604fb0e634523ab0c3a709243bbd1.example.org"}, {"package": "mint-linux", "version": "2013.11.0", "host": "a41604fb0e634523ab0c3a709243bbd1.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.2.4", "host": "3214efdf5122408aa0e46df210534db9.example.org"}, {"package": "pytwitter", "version": "0.0.4", "host": "3214efdf5122408aa0e46df210534db9.example.org"}, {"package": "mint-linux", "version": "2010.12.0", "host": "3214efdf5122408aa0e46df210534db9.example.org"}, {"package": "osquery", "version": "2.0.0", "host": "3214efdf5122408aa0e46df210534db9.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "3214efdf5122408aa0e46df210534db9.example.org"}]}'
{"3214efdf5122408aa0e46df210534db9.example.org":["CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2017.5.7", "host": "05b726ed7cb24d0a82db41767b9b554a.example.org"}]}'
{"05b726ed7cb24d0a82db41767b9b554a.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "2.8.1", "host": "f3969fffe4574ae9ac315790820eac03.example.org"}, {"package": "osquery", "version": "2.7.2", "host": "f3969fffe4574ae9ac315790820eac03.example.org"}, {"package": "freeciv", "version": "2.0.9", "host": "f3969fffe4574ae9ac315790820eac03.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.2", "host": "6199b815e9f2446997882c3bb45c4813.example.org"}, {"package": "mint-linux", "version": "2016.7.0", "host": "6199b815e9f2446997882c3bb45c4813.example.org"}, {"package": "pytwitter", "version": "0.1.0", "host": "6199b815e9f2446997882c3bb45c4813.example.org"}]}'
{"6199b815e9f2446997882c3bb45c4813.example.org":["CVE-2020-0003","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.0.9", "host": "417615a82cb9458e887a749d6483961c.example.org"}, {"package": "osquery", "version": "1.2.6", "host": "417615a82cb9458e887a749d6483961c.example.org"}, {"package": "mint-linux", "version": "2013.10.0", "host": "417615a82cb9458e887a749d6483961c.example.org"}]}'
{"417615a82cb9458e887a749d6483961c.example.org":["CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "1.3.0", "host": "e81bf6407d8d4adbac7aa82f86383c27.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "0.1.0", "host": "72725f1eceb54d959d3f1bd595011520.example.org"}, {"package": "mint-linux", "version": "2014.11.0", "host": "72725f1eceb54d959d3f1bd595011520.example.org"}]}'
{"72725f1eceb54d959d3f1bd595011520.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2013.12.0", "host": "bd93ace2ba704f598a04faa0a27a3d7d.example.org"}, {"package": "freeciv", "version": "0.7.0", "host": "bd93ace2ba704f598a04faa0a27a3d7d.example.org"}, {"package": "photoshop", "version": "2.1.0", "host": "bd93ace2ba704f598a04faa0a27a3d7d.example.org"}, {"package": "pytwitter", "version": "1.0.2", "host": "bd93ace2ba704f598a04faa0a27a3d7d.example.org"}, {"package": "osquery", "version": "1.3.0", "host": "bd93ace2ba704f598a04faa0a27a3d7d.example.org"}, {"package": "freeciv", "version": "1.2.9", "host": "bd93ace2ba704f598a04faa0a27a3d7d.example.org"}]}'
{"bd93ace2ba704f598a04faa0a27a3d7d.example.org":["CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2012.3.0", "host": "ed5b8a50993a4c88afb8e9235148f11c.example.org"}, {"package": "osquery", "version": "0.8.4", "host": "ed5b8a50993a4c88afb8e9235148f11c.example.org"}, {"package": "freeciv", "version": "0.4.2", "host": "ed5b8a50993a4c88afb8e9235148f11c.example.org"}]}'
{"ed5b8a50993a4c88afb8e9235148f11c.example.org":["CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "2.5.3", "host": "7c8e910168e94357a4620f08a4bfb665.example.org"}, {"package": "freeciv", "version": "1.0.1", "host": "7c8e910168e94357a4620f08a4bfb665.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "7c8e910168e94357a4620f08a4bfb665.example.org"}]}'
{"7c8e910168e94357a4620f08a4bfb665.example.org":["CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.3.9", "host": "9da907c1521a466c82e34089fb245138.example.org"}, {"package": "freeciv", "version": "2.2.6", "host": "9da907c1521a466c82e34089fb245138.example.org"}, {"package": "osquery", "version": "0.7.5", "host": "9da907c1521a466c82e34089fb245138.example.org"}, {"package": "photoshop", "version": "2.0.4", "host": "9da907c1521a466c82e34089fb245138.example.org"}, {"package": "mint-linux", "version": "2018.7.4", "host": "9da907c1521a466c82e34089fb245138.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "9da907c1521a466c82e34089fb245138.example.org"}]}'
{"9da907c1521a466c82e34089fb245138.example.org":["CVE-2020-0007","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "flash", "version": "422.6.9", "host": "8995655610bc4e8e8d1565764a8434fd.example.org"}, {"package": "photoshop", "version": "2.4.1", "host": "8995655610bc4e8e8d1565764a8434fd.example.org"}, {"package": "mint-linux", "version": "2014.2.0", "host": "8995655610bc4e8e8d1565764a8434fd.example.org"}, {"package": "freeciv", "version": "0.2.7", "host": "8995655610bc4e8e8d1565764a8434fd.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "8995655610bc4e8e8d1565764a8434fd.example.org"}]}'
{"8995655610bc4e8e8d1565764a8434fd.example.org":["CVE-2020-0005","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.2.1", "host": "17c739043b494a4a876819b74e2a085c.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.9.4", "host": "d71fc1d72494484f826eadab2934c2ab.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.4", "host": "e86b225ddf2d41d6865e9016f3f5957b.example.org"}, {"package": "photoshop", "version": "1.8.1", "host": "e86b225ddf2d41d6865e9016f3f5957b.example.org"}, {"package": "mint-linux", "version": "2020.1.4", "host": "e86b225ddf2d41d6865e9016f3f5957b.example.org"}]}'
{"e86b225ddf2d41d6865e9016f3f5957b.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.2.0", "host": "b8002722b8f645bd943fe1aaa84fbcf5.example.org"}, {"package": "photoshop", "version": "2.6.6", "host": "b8002722b8f645bd943fe1aaa84fbcf5.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.1.2", "host": "723f5908f69e43e0838664944dca2935.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.3.2", "host": "e9871f1a1a8c48319c60598fff4a74f7.example.org"}, {"package": "mint-linux", "version": "2012.1.0", "host": "e9871f1a1a8c48319c60598fff4a74f7.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.0", "host": "76dd1a2ff70a40d8914814abfb6fe516.example.org"}, {"package": "photoshop", "version": "1.8.3", "host": "76dd1a2ff70a40d8914814abfb6fe516.example.org"}]}'
{"76dd1a2ff70a40d8914814abfb6fe516.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2014.8.0", "host": "85f119b615a34e8cbdfba63f9831ee50.example.org"}, {"package": "osquery", "version": "0.4.1", "host": "85f119b615a34e8cbdfba63f9831ee50.example.org"}, {"package": "pytwitter", "version": "1.5.4", "host": "85f119b615a34e8cbdfba63f9831ee50.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2011.9.0", "host": "36c0a89168974e128fff30ccd5cd64b4.example.org"}, {"package": "photoshop", "version": "0.2.0", "host": "36c0a89168974e128fff30ccd5cd64b4.example.org"}, {"package": "freeciv", "version": "2.7.8", "host": "36c0a89168974e128fff30ccd5cd64b4.example.org"}, {"package": "osquery", "version": "1.5.1", "host": "36c0a89168974e128fff30ccd5cd64b4.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.2.3", "host": "d295cad701b94db79b43a043e8ede53f.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "d295cad701b94db79b43a043e8ede53f.example.org"}]}'
{"d295cad701b94db79b43a043e8ede53f.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.6.8", "host": "24be4cab8e4e4f4da5d3fb7aeac2bf85.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.8.9", "host": "b5c12174ff2d4483b50a952d365a8f3f.example.org"}, {"package": "freeciv", "version": "2.1.3", "host": "b5c12174ff2d4483b50a952d365a8f3f.example.org"}]}'
{"b5c12174ff2d4483b50a952d365a8f3f.example.org":["CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "0.7.8", "host": "8fe205cfb0b94bd68245302a68fa7547.example.org"}, {"package": "photoshop", "version": "1.3.6", "host": "8fe205cfb0b94bd68245302a68fa7547.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "8fe205cfb0b94bd68245302a68fa7547.example.org"}, {"package": "freeciv", "version": "2.4.2", "host": "8fe205cfb0b94bd68245302a68fa7547.example.org"}]}'
{"8fe205cfb0b94bd68245302a68fa7547.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.2.7", "host": "6fe56303e1454b43b61393c93d07a16b.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "6fe56303e1454b43b61393c93d07a16b.example.org"}]}'
{"6fe56303e1454b43b61393c93d07a16b.example.org":["CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "2.9.2", "host": "4ac5d758bfa64174b282b33cfb57549e.example.org"}, {"package": "photoshop", "version": "1.3.0", "host": "4ac5d758bfa64174b282b33cfb57549e.example.org"}, {"package": "freeciv", "version": "2.1.1", "host": "4ac5d758bfa64174b282b33cfb57549e.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "4ac5d758bfa64174b282b33cfb57549e.example.org"}]}'
{"4ac5d758bfa64174b282b33cfb57549e.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "2.4.4", "host": "0905665e7f794b7a8e97218f39f82fe6.example.org"}, {"package": "photoshop", "version": "1.7.3", "host": "0905665e7f794b7a8e97218f39f82fe6.example.org"}, {"package": "osquery", "version": "2.3.7", "host": "0905665e7f794b7a8e97218f39f82fe6.example.org"}, {"package": "freeciv", "version": "0.5.5", "host": "0905665e7f794b7a8e97218f39f82fe6.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "0.6.9", "host": "f32f863b967d440a8ce040c4a96281e0.example.org"}, {"package": "freeciv", "version": "1.7.6", "host": "f32f863b967d440a8ce040c4a96281e0.example.org"}, {"package": "pytwitter", "version": "2.9.4", "host": "f32f863b967d440a8ce040c4a96281e0.example.org"}, {"package": "mint-linux", "version": "2012.1.0", "host": "f32f863b967d440a8ce040c4a96281e0.example.org"}, {"package": "photoshop", "version": "1.4.3", "host": "f32f863b967d440a8ce040c4a96281e0.example.org"}, {"package": "osquery", "version": "2.5.3", "host": "f32f863b967d440a8ce040c4a96281e0.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2012.2.0", "host": "e0ddd02b1d544f81ad529df596f234de.example.org"}, {"package": "freeciv", "version": "2.9.2", "host": "e0ddd02b1d544f81ad529df596f234de.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "e0ddd02b1d544f81ad529df596f234de.example.org"}, {"package": "osquery", "version": "1.5.7", "host": "e0ddd02b1d544f81ad529df596f234de.example.org"}]}'
{"e0ddd02b1d544f81ad529df596f234de.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.3.4", "host": "28df633e2d244f0fa6d6a40712f1d3b5.example.org"}, {"package": "flash", "version": "394.4.2", "host": "28df633e2d244f0fa6d6a40712f1d3b5.example.org"}, {"package": "pytwitter", "version": "1.3.9", "host": "28df633e2d244f0fa6d6a40712f1d3b5.example.org"}, {"package": "mint-linux", "version": "2014.4.0", "host": "28df633e2d244f0fa6d6a40712f1d3b5.example.org"}]}'
{"28df633e2d244f0fa6d6a40712f1d3b5.example.org":["CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.2.0", "host": "55c23e0643fa4bce857549f2a248ae26.example.org"}, {"package": "freeciv", "version": "1.1.1", "host": "55c23e0643fa4bce857549f2a248ae26.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "55c23e0643fa4bce857549f2a248ae26.example.org"}]}'
{"55c23e0643fa4bce857549f2a248ae26.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "0.3.8", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}, {"package": "pytwitter", "version": "1.0.0", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}, {"package": "mint-linux", "version": "2019.9.1", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}, {"package": "flash", "version": "864.3.2", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}, {"package": "freeciv", "version": "1.2.4", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}, {"package": "osquery", "version": "2.4.6", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}, {"package": "freeciv", "version": "0.8.3", "host": "3a6764cbf2c941a4969f89165be9e79d.example.org"}]}'
{"3a6764cbf2c941a4969f89165be9e79d.example.org":["CVE-2020-0007","CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "0.1.0", "host": "bf6e6f523e8d40e5b4970d576326f24a.example.org"}, {"package": "osquery", "version": "0.7.5", "host": "bf6e6f523e8d40e5b4970d576326f24a.example.org"}, {"package": "freeciv", "version": "0.6.0", "host": "bf6e6f523e8d40e5b4970d576326f24a.example.org"}, {"package": "mint-linux", "version": "2017.9.3", "host": "bf6e6f523e8d40e5b4970d576326f24a.example.org"}, {"package": "freeciv", "version": "1.0.9", "host": "bf6e6f523e8d40e5b4970d576326f24a.example.org"}, {"package": "photoshop", "version": "2.8.6", "host": "bf6e6f523e8d40e5b4970d576326f24a.example.org"}]}'
{"bf6e6f523e8d40e5b4970d576326f24a.example.org":["CVE-2020-0006","CVE-2020-0007","CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.1.0", "host": "e6f7277ad6284bca8a4762fbf60692fc.example.org"}, {"package": "freeciv", "version": "1.7.8", "host": "e6f7277ad6284bca8a4762fbf60692fc.example.org"}, {"package": "pytwitter", "version": "1.3.8", "host": "e6f7277ad6284bca8a4762fbf60692fc.example.org"}, {"package": "osquery", "version": "2.9.0", "host": "e6f7277ad6284bca8a4762fbf60692fc.example.org"}, {"package": "mint-linux", "version": "2013.4.0", "host": "e6f7277ad6284bca8a4762fbf60692fc.example.org"}]}'
{"e6f7277ad6284bca8a4762fbf60692fc.example.org":["CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.1.0", "host": "583dcd34467c4ac9807fead51e110253.example.org"}, {"package": "freeciv", "version": "2.4.5", "host": "583dcd34467c4ac9807fead51e110253.example.org"}, {"package": "osquery", "version": "0.9.2", "host": "583dcd34467c4ac9807fead51e110253.example.org"}]}'
{"583dcd34467c4ac9807fead51e110253.example.org":["CVE-2020-0004","CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2018.6.5", "host": "41a153d57d6d4d5582d6182e15c9da23.example.org"}, {"package": "osquery", "version": "0.5.1", "host": "41a153d57d6d4d5582d6182e15c9da23.example.org"}, {"package": "photoshop", "version": "2.0.9", "host": "41a153d57d6d4d5582d6182e15c9da23.example.org"}]}'
{"41a153d57d6d4d5582d6182e15c9da23.example.org":["CVE-2020-0007","CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "0.1.0", "host": "b264ecf63784416eace3ed203fbe79ba.example.org"}, {"package": "photoshop", "version": "0.4.8", "host": "b264ecf63784416eace3ed203fbe79ba.example.org"}, {"package": "flash", "version": "746.6.4", "host": "b264ecf63784416eace3ed203fbe79ba.example.org"}]}'
{"b264ecf63784416eace3ed203fbe79ba.example.org":["CVE-2020-0006","CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.7.2", "host": "9ecf806f5d6e4ce3979b930566e190cb.example.org"}, {"package": "freeciv", "version": "0.2.5", "host": "9ecf806f5d6e4ce3979b930566e190cb.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2018.1.3", "host": "16b0eaa29b6f4154a0d57d14fb6cafef.example.org"}]}'
{"16b0eaa29b6f4154a0d57d14fb6cafef.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "1.1.9", "host": "9398506568e24c3a975b2f141178c1cd.example.org"}, {"package": "freeciv", "version": "2.1.0", "host": "9398506568e24c3a975b2f141178c1cd.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2014.12.0", "host": "719c1e69089643488c0c5a717b36edb1.example.org"}, {"package": "freeciv", "version": "0.5.3", "host": "719c1e69089643488c0c5a717b36edb1.example.org"}, {"package": "photoshop", "version": "2.1.1", "host": "719c1e69089643488c0c5a717b36edb1.example.org"}]}'
{"719c1e69089643488c0c5a717b36edb1.example.org":["CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "0.5.5", "host": "07102abf208a47219785fc60e1721a45.example.org"}, {"package": "osquery", "version": "0.4.3", "host": "07102abf208a47219785fc60e1721a45.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2011.3.0", "host": "b28c459606c44880a25189922c7f0a0b.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2014.12.0", "host": "618c8a0594cd421ea02d5cbcca003976.example.org"}, {"package": "pytwitter", "version": "0.1.0", "host": "618c8a0594cd421ea02d5cbcca003976.example.org"}, {"package": "photoshop", "version": "2.6.9", "host": "618c8a0594cd421ea02d5cbcca003976.example.org"}]}'
{"618c8a0594cd421ea02d5cbcca003976.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.2.1", "host": "34b29196e177430da13be61bbe138f79.example.org"}, {"package": "freeciv", "version": "0.7.9", "host": "34b29196e177430da13be61bbe138f79.example.org"}, {"package": "photoshop", "version": "0.6.3", "host": "34b29196e177430da13be61bbe138f79.example.org"}, {"package": "mint-linux", "version": "2018.5.4", "host": "34b29196e177430da13be61bbe138f79.example.org"}, {"package": "osquery", "version": "2.8.5", "host": "34b29196e177430da13be61bbe138f79.example.org"}, {"package": "pytwitter", "version": "2.5.0", "host": "34b29196e177430da13be61bbe138f79.example.org"}]}'
{"34b29196e177430da13be61bbe138f79.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.9", "host": "7b91215bc7964082840f2d665671a079.example.org"}, {"package": "photoshop", "version": "2.1.0", "host": "7b91215bc7964082840f2d665671a079.example.org"}, {"package": "mint-linux", "version": "2013.11.0", "host": "7b91215bc7964082840f2d665671a079.example.org"}, {"package": "osquery", "version": "2.8.8", "host": "7b91215bc7964082840f2d665671a079.example.org"}, {"package": "freeciv", "version": "0.0.6", "host": "7b91215bc7964082840f2d665671a079.example.org"}]}'
{"7b91215bc7964082840f2d665671a079.example.org":["CVE-2020-0004"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "2.8.1", "host": "de82c039aadb465ea120e03b6311cf5b.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "0.4.6", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}, {"package": "pytwitter", "version": "2.0.6", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}, {"package": "mint-linux", "version": "2016.5.0", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}, {"package": "osquery", "version": "2.6.6", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}, {"package": "freeciv", "version": "0.8.4", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}, {"package": "flash", "version": "787.9.7", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}, {"package": "freeciv", "version": "2.0.1", "host": "f3a9393213e24e619fe8edc658e3aa7e.example.org"}]}'
{"f3a9393213e24e619fe8edc658e3aa7e.example.org":["CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.0.9", "host": "9d270207ac1b4f4792b237065cd70fac.example.org"}, {"package": "flash", "version": "620.9.7", "host": "9d270207ac1b4f4792b237065cd70fac.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "9d270207ac1b4f4792b237065cd70fac.example.org"}, {"package": "freeciv", "version": "0.8.8", "host": "9d270207ac1b4f4792b237065cd70fac.example.org"}]}'
{"9d270207ac1b4f4792b237065cd70fac.example.org":["CVE-2020-0001","CVE-2020-0005","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.1.4", "host": "12254e96c2694b2d91c5ae5a983c1904.example.org"}, {"package": "freeciv", "version": "1.1.0", "host": "12254e96c2694b2d91c5ae5a983c1904.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "12254e96c2694b2d91c5ae5a983c1904.example.org"}]}'
{"12254e96c2694b2d91c5ae5a983c1904.example.org":["CVE-2020-0001","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.0.9", "host": "7ecf131b7dcc476891f3809e5c0807ba.example.org"}, {"package": "osquery", "version": "0.5.9", "host": "7ecf131b7dcc476891f3809e5c0807ba.example.org"}]}'
{"7ecf131b7dcc476891f3809e5c0807ba.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "2.5.1", "host": "b1e83259c72e4d24adabb1dd70acc13a.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "2.5.5", "host": "53dc62b414e84184b3392ee9ca29ec5d.example.org"}, {"package": "osquery", "version": "0.9.6", "host": "53dc62b414e84184b3392ee9ca29ec5d.example.org"}, {"package": "photoshop", "version": "2.9.2", "host": "53dc62b414e84184b3392ee9ca29ec5d.example.org"}, {"package": "pytwitter", "version": "0.1.1", "host": "53dc62b414e84184b3392ee9ca29ec5d.example.org"}]}'
{"53dc62b414e84184b3392ee9ca29ec5d.example.org":["CVE-2020-0002","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.1.5", "host": "9a5fc0165f2b4241949355de09e940a2.example.org"}, {"package": "freeciv", "version": "0.5.0", "host": "9a5fc0165f2b4241949355de09e940a2.example.org"}, {"package": "mint-linux", "version": "2012.1.0", "host": "9a5fc0165f2b4241949355de09e940a2.example.org"}, {"package": "osquery", "version": "0.9.6", "host": "9a5fc0165f2b4241949355de09e940a2.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "9a5fc0165f2b4241949355de09e940a2.example.org"}]}'
{"9a5fc0165f2b4241949355de09e940a2.example.org":["CVE-2020-0002","CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.7.9", "host": "8e1c4ac11ebc4b17bf6fab3f52065ad2.example.org"}, {"package": "flash", "version": "865.9.1", "host": "8e1c4ac11ebc4b17bf6fab3f52065ad2.example.org"}, {"package": "mint-linux", "version": "2018.0.8", "host": "8e1c4ac11ebc4b17bf6fab3f52065ad2.example.org"}, {"package": "freeciv", "version": "2.9.0", "host": "8e1c4ac11ebc4b17bf6fab3f52065ad2.example.org"}, {"package": "osquery", "version": "0.7.8", "host": "8e1c4ac11ebc4b17bf6fab3f52065ad2.example.org"}]}'
{"8e1c4ac11ebc4b17bf6fab3f52065ad2.example.org":["CVE-2020-0005","CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "pytwitter", "version": "0.1.1", "host": "c3a2a5900f9b472592fdfc6d46777ad7.example.org"}]}'
{"c3a2a5900f9b472592fdfc6d46777ad7.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.9.0", "host": "c4ae6cc45ed24a9291a60b7b9ae7210f.example.org"}, {"package": "freeciv", "version": "1.6.4", "host": "c4ae6cc45ed24a9291a60b7b9ae7210f.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.5.3", "host": "33326f09c69241be9d1f809201f1e5ec.example.org"}, {"package": "photoshop", "version": "2.6.1", "host": "33326f09c69241be9d1f809201f1e5ec.example.org"}, {"package": "pytwitter", "version": "2.6.7", "host": "33326f09c69241be9d1f809201f1e5ec.example.org"}, {"package": "mint-linux", "version": "2011.12.0", "host": "33326f09c69241be9d1f809201f1e5ec.example.org"}, {"package": "osquery", "version": "0.9.4", "host": "33326f09c69241be9d1f809201f1e5ec.example.org"}, {"package": "freeciv", "version": "2.5.5", "host": "33326f09c69241be9d1f809201f1e5ec.example.org"}]}'
{"33326f09c69241be9d1f809201f1e5ec.example.org":["CVE-2020-0002"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.1.0", "host": "2f22381360eb45d99d164203c6712d44.example.org"}, {"package": "pytwitter", "version": "0.1.4", "host": "2f22381360eb45d99d164203c6712d44.example.org"}, {"package": "photoshop", "version": "0.6.8", "host": "2f22381360eb45d99d164203c6712d44.example.org"}, {"package": "freeciv", "version": "1.1.2", "host": "2f22381360eb45d99d164203c6712d44.example.org"}, {"package": "freeciv", "version": "0.8.6", "host": "2f22381360eb45d99d164203c6712d44.example.org"}]}'
{"2f22381360eb45d99d164203c6712d44.example.org":["CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.4.2", "host": "33f2e4c1d9614e92b190a1f1c0b55ca2.example.org"}, {"package": "pytwitter", "version": "0.2.8", "host": "33f2e4c1d9614e92b190a1f1c0b55ca2.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.0.0", "host": "e32079a060564b39bba4805cd11cf987.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.0.9", "host": "9692f20fcc4a44b2a53e2843de499e97.example.org"}, {"package": "freeciv", "version": "2.0.4", "host": "9692f20fcc4a44b2a53e2843de499e97.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2013.2.0", "host": "6ddadef124ab4910825dfffa03f7af6e.example.org"}, {"package": "pytwitter", "version": "2.1.3", "host": "6ddadef124ab4910825dfffa03f7af6e.example.org"}, {"package": "osquery", "version": "1.1.6", "host": "6ddadef124ab4910825dfffa03f7af6e.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "0.9.4", "host": "1d2ccf3470bd49c4ba0a3ead9cfdce63.example.org"}, {"package": "mint-linux", "version": "2018.9.8", "host": "1d2ccf3470bd49c4ba0a3ead9cfdce63.example.org"}, {"package": "flash", "version": "203.1.0", "host": "1d2ccf3470bd49c4ba0a3ead9cfdce63.example.org"}, {"package": "freeciv", "version": "2.5.3", "host": "1d2ccf3470bd49c4ba0a3ead9cfdce63.example.org"}]}'
{"1d2ccf3470bd49c4ba0a3ead9cfdce63.example.org":["CVE-2020-0007","CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.2", "host": "e69001727972424aa4fd2a737c6f99d4.example.org"}, {"package": "mint-linux", "version": "2011.11.0", "host": "e69001727972424aa4fd2a737c6f99d4.example.org"}, {"package": "osquery", "version": "2.6.8", "host": "e69001727972424aa4fd2a737c6f99d4.example.org"}, {"package": "pytwitter", "version": "2.3.8", "host": "e69001727972424aa4fd2a737c6f99d4.example.org"}, {"package": "freeciv", "version": "2.8.6", "host": "e69001727972424aa4fd2a737c6f99d4.example.org"}]}'
{"e69001727972424aa4fd2a737c6f99d4.example.org":["CVE-2020-0003"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "0.3.6", "host": "7f4c7da1b0aa447390f7ae0dbe1779e8.example.org"}, {"package": "photoshop", "version": "2.0.9", "host": "7f4c7da1b0aa447390f7ae0dbe1779e8.example.org"}, {"package": "freeciv", "version": "1.3.7", "host": "7f4c7da1b0aa447390f7ae0dbe1779e8.example.org"}, {"package": "pytwitter", "version": "2.3.6", "host": "7f4c7da1b0aa447390f7ae0dbe1779e8.example.org"}, {"package": "flash", "version": "648.5.2", "host": "7f4c7da1b0aa447390f7ae0dbe1779e8.example.org"}, {"package": "osquery", "version": "1.5.8", "host": "7f4c7da1b0aa447390f7ae0dbe1779e8.example.org"}]}'
{"7f4c7da1b0aa447390f7ae0dbe1779e8.example.org":["CVE-2020-0004","CVE-2020-0005"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "osquery", "version": "0.9.1", "host": "3f599cf1c4e845f29fbc6da017f4799d.example.org"}, {"package": "mint-linux", "version": "2015.12.0", "host": "3f599cf1c4e845f29fbc6da017f4799d.example.org"}, {"package": "pytwitter", "version": "0.1.0", "host": "3f599cf1c4e845f29fbc6da017f4799d.example.org"}]}'
{"3f599cf1c4e845f29fbc6da017f4799d.example.org":["CVE-2020-0002","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "0.9.1", "host": "a62df0ee73ea4ead87af0aeb8912790d.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.1.2", "host": "aa0b43190366494d9ac9839a9ad23456.example.org"}, {"package": "mint-linux", "version": "2013.11.0", "host": "aa0b43190366494d9ac9839a9ad23456.example.org"}, {"package": "pytwitter", "version": "0.1.0", "host": "aa0b43190366494d9ac9839a9ad23456.example.org"}, {"package": "photoshop", "version": "0.4.8", "host": "aa0b43190366494d9ac9839a9ad23456.example.org"}, {"package": "freeciv", "version": "0.8.9", "host": "aa0b43190366494d9ac9839a9ad23456.example.org"}]}'
{"aa0b43190366494d9ac9839a9ad23456.example.org":["CVE-2020-0003","CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "0.1.0", "host": "73e1ade78c074621a6d45e713c91bbd8.example.org"}]}'
{}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "mint-linux", "version": "2020.1.9", "host": "6c792b3df106497095ece40c9480cb12.example.org"}, {"package": "osquery", "version": "2.7.7", "host": "6c792b3df106497095ece40c9480cb12.example.org"}]}'
{"6c792b3df106497095ece40c9480cb12.example.org":["CVE-2020-0007"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "2.7.4", "host": "4ad0da7dc6ad45adba64c0d6f721a6aa.example.org"}, {"package": "pytwitter", "version": "0.1.0", "host": "4ad0da7dc6ad45adba64c0d6f721a6aa.example.org"}, {"package": "mint-linux", "version": "2015.12.0", "host": "4ad0da7dc6ad45adba64c0d6f721a6aa.example.org"}]}'
{"4ad0da7dc6ad45adba64c0d6f721a6aa.example.org":["CVE-2020-0006"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "photoshop", "version": "1.7.3", "host": "916e33f0ba934bc6bd1dfe0dbc7d85e9.example.org"}, {"package": "freeciv", "version": "1.4.7", "host": "916e33f0ba934bc6bd1dfe0dbc7d85e9.example.org"}, {"package": "freeciv", "version": "1.1.0", "host": "916e33f0ba934bc6bd1dfe0dbc7d85e9.example.org"}]}'
{"916e33f0ba934bc6bd1dfe0dbc7d85e9.example.org":["CVE-2020-0001"]}

/usr/bin/curl -s http://127.0.0.1:8080/vespa/api/v2.0/vuln -d '{"data": [{"package": "freeciv", "version": "1.4.0", "host": "330facf12c55432d9f7eed27c5448ac8.example.org"}, {"package": "mint-linux", "version": "2016.3.0", "host": "330facf12c55432d9f7eed27c5448ac8.example.org"}]}'
{}

STATS: lines-processed: 100 example_post_data.json.  Start: Tue May 19 00:47:58 UTC 2020   End: Tue May 19 00:48:00 UTC 2020
```
