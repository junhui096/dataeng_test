# DSAID Data Engineering Technical Test Documentation

This test is split into 3 sections, **data pipelines**, **databases** and **system design**. 

1. Clone the repo into the home directory, and cd into it.

## Section 1: Data Pipelines
Refer to the file *process_csv.py* for the python code that implements the various data processing requirements.

The program accepts as command-line arguments the *input_file_name* and *output_file_name*.

The file *output.csv* is the file of the processed dataset.

There exists a shell script *scheduler.sh* with the following command:

    /usr/bin/python ~/dataeng_test/process_csv.py ~/dataeng_test/dataset.csv ~/dataeng_test/output.csv
 
that follows the following format:

    <path_to_python_installation> <path_to_repo>/process_csv.py <path_to_input_file> <path_to_output_file>

You can change the script accordingly based on the above format.

Next, you can install a crontab to schedule the jobs at 1am daily.

    crontab - e   # opens the editor to add a cron job
    0 1 * * * /<path_to_repo>/scheduler.sh   # schedule cron job


## Section 2: Databases
You are appointed by a car dealership to create their database infrastructure. There is only one store. In each business day, cars are being sold by a team of salespersons. Each transaction would contain information on the date and time of transaction, customer transacted with, and the car that was sold. 

The following are known:
- Both used and new cars are sold.
- Each car can only be sold by one salesperson.
- There are multiple manufacturers’ cars sold.
- Each car has the following characteristics:
- Manufacturer
- Model name
- Model variant
- Serial number
- Weight
- Engine cubic capacity
- Price

Each sale transaction contains the following information:
- Customer Name
- Customer Phone
- Salesperson
- Characteristics of car sold

Set up a PostgreSQL database using the base `docker` image [here](https://hub.docker.com/_/postgres) given the above. We expect at least a `Dockerfile` which will stand up your database with the DDL statements to create the necessary tables. Produce entity-relationship diagrams as necessary to illustrate your design.

## Section 3: System Design
You are designing data infrastructure on the cloud for a company whose main business is in processing images. 

The company has a web application which collects images uploaded by customers. The company also has a separate web application which provides a stream of images using a Kafka stream. The company’s software engineers have already some code written to process the images. The company  would like to save processed images for a minimum of 7 days for archival purposes. Ideally, the company would also want to be able to have some Business Intelligence (BI) on key statistics including number and type of images processed, and by which customers.

Produce a system architecture diagram (e.g. Visio, Powerpoint) using any of the commercial cloud providers' ecosystem to explain your design. Please also indicate clearly if you have made any assumptions at any point.


