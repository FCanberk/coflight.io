## Project Details for Developers

Coflight will run on **Google Cloud Platform. Selenium WebDriver, Python** and **PhantomJS** will be used for scraping. **PostgreSQL** will be used for storing the data that collected. The project has 3 main parts:

### **1. Scraping**

**Selenium WebDriver**, **Python** and **PhantomJS** will be used for scraping flight data of airline companies linked below

* #### [Turkish Airlines](https://www.turkishairlines.com/)
* #### [Pegasus Airlines](https://www.flypgs.com/)
* #### [Atlas Global](https://www.atlasglb.com/)
* #### [Onur Air](https://www.onurair.com/)

Here are scraping guides for [**Turkish Airlines**](https://github.com/FCanberk/coflight-prep/blob/master/issue-drafts/scraping/thy%20scraping.md) ,
 [**Pegasus Airlines**](https://github.com/FCanberk/coflight-prep/blob/master/issue-drafts/scraping/flypgs%20scraping.md) , [**Atlas Global**](https://github.com/FCanberk/coflight-prep/blob/master/issue-drafts/scraping/atlasglobal%20scraping.md) and [**Onur Air**](https://github.com/FCanberk/coflight-prep/blob/master/issue-drafts/scraping/onur%20air%20scraping.md)

Ticket price `currency` will be `TRY`

For each airline company ticket price, flight date&time,current date&time and destination should be scraped.

<br>For Turkish Airlines 30 International 20 Domestic flights,
<br>For Pegasus Airlines 20 International 20 Domestic flights,
<br>For Atlas Global     15 International 15 Domestic flights,
<br>For Onur Air         15 International 15 Domestic flights data 
should be scraped with and without deleting cookies.

These data should be scraped every five minutes.

### **2. Collecting and Storing Data**

Collected data will be stored in a document db (most likely PostgreSQL). Scraped data should be stored in separate databases for each company. Each database should store ticket price, flight date&time, destination, date&time (UTC +03:00) when scraped infos taken.

Initial dataset should be stored in database and the database should be updated every flight update.

### **3. Reporting**

Collected data should be reported in different graphics to compare ticket prices **with** and **without** deleting **cookies** and to see ticket price fluctuation for different time periods.

* Daily ticket price of same ticket with and without cookies,
* Weekly ticket price of same ticket with and without cookies,
* Monthly ticket price of same ticket with and without cookies, 
* Annual ticket price of same ticket with and without cookies graphics should be reported.

### Bonus Objectives

* Ticket price of same destination for different departure dates&times will graphically shown for whole year for each company. To see which season of year has the cheapest/the most expensive tickets.

* Ticket price of one flight will graphically shown for whole year for each company. To see when is the cheapest/the most expensive ticket for a particular flight.

### Contribution

* Project is driven over Github. Please look at the Github issues not assigned yet.
* Please make sure that every functionality added has a test coverage and does not break any existing test.

### Installation

##### Windows

* Download [PhantomJS](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip).
* Copy the executable `PhantomJS` file inside `bin` folder.
* Paste it to `src` folder where the scrapers are.

##### Mac OS X

* Download [PhantomJS](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip).
* Copy the executable `PhantomJS` file inside `bin` folder.
* Paste it to `src` folder where the scrapers are.
* **Make sure the executable file is in `PATH`.**

##### Linux

* Download [PhantomJS(64 bit)](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2) or [PhantomJS(32 bit)](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2).
* Copy the executable `PhantomJS` file inside `bin` folder.
* Paste it to `src` folder where the scrapers are.
* **Make sure the executable file is in `PATH`.**


#### Build

* Project modules are written with `Python 3`.
* In order to install the dependencies use `pip3 install -r requirements.txt`


#### Test

* Running the tests requires `pytest`, just run `pytest tests/` in order to make sure there is no regression before submitting the PR.

Please refer to [scraping guide](scraping%20guide.md) to see detailed information about scraping.