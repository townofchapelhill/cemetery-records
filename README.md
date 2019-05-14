# Burial Records

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4e0e31671b494297a1a292905fea6a3b)](https://app.codacy.com/app/TownofChapelHill/cemetery-records?utm_source=github.com&utm_medium=referral&utm_content=townofchapelhill/cemetery-records&utm_campaign=Badge_Grade_Dashboard)

## Burial Records Aggregator

### Goal 
Scrape the Town of Chapel Hill burial records pages to create a single dataset
### Purpose 

Provide a single source for all town public cemetery burial data
### Methodology 
html scraping

### Data Source
[Town of Chapel Hill Cemeteries](https://www.townofchapelhill.org/town-hall/departments-services/parks-recreation/cemeteries)
### Output 
cemetery_data.csv

### Transformations
Select Last Name, First Name, Year Deceased, Section, Lot

### Constraints
Users the lxml library via ```pip install lxml```
