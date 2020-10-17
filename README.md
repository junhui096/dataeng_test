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
Refer to *er_diagram.jpg* for the ER diagram of the database design.

To launch the postgres container, execute the following steps:

First, build the docker image from the docker file.

    docker build --tag db:1.0 .

Next, run the docker image

    docker run --name cars -d db:1.0

Finally, you can log into the running docker container, to ensure that all tables are successfully created.

    docker exec -it cars psql -U docker -d car
    psql >> \dt 

## Section 3: System Design
You are designing data infrastructure on the cloud for a company whose main business is in processing images. 

The company has a web application which collects images uploaded by customers. The company also has a separate web application which provides a stream of images using a Kafka stream. The company’s software engineers have already some code written to process the images. The company  would like to save processed images for a minimum of 7 days for archival purposes. Ideally, the company would also want to be able to have some Business Intelligence (BI) on key statistics including number and type of images processed, and by which customers.

Produce a system architecture diagram (e.g. Visio, Powerpoint) using any of the commercial cloud providers' ecosystem to explain your design. Please also indicate clearly if you have made any assumptions at any point.


