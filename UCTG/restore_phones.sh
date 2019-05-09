#!/bin/bash
# restore 8861 to clean config
curl -s http://173.39.153.176/admin/resync?http://173.39.153.187/bsiot23sync/clean_8861_173.39.153.176.xml >> /dev/null
# resotre 8811 to clean config
curl -s http://173.39.153.171/admin/resync?http://173.39.153.187/bsiot23sync/clean_8811_173.39.153.171.xml >> /dev/null
