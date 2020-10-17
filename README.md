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
I have used the services offered by Google Cloud Platform to design the image processing pipeline.

Refer to *system_design_task3.jpg* for the diagram.

1. Assuming that Kafka is deployed on GCP, the Kafka connector has to be installed, so that all messages published to a specifc topic in Kafka, will be published to the PubSub queue too.
2. Deploy a cloud function that is triggered once a new message is published to the pubsub topic.
3. The cloud function should process the images and write the processed images to a cloud storage bucket(GCS), in coldline storage class, assuming it is for archival purposes and rarely accessed.
4. The bucket should also implement an object lifecycle management policy to delete an image after 7 days.
5. The cloud function should produce logs, which are synced to the cloud logging platform. These logs should be structured with the necessary fields for analysis.
6. These logs can be periodically exported to a data warehouse, such as BigQuery for further analysis. The scheduling of these jobs can be done via cloud scheduler.

