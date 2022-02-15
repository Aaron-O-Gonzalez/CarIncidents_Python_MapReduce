# Post-Sales Automobile Incidents

The following code implements a Python-based MapReduce process to calculate the number of reported crashes for a specifc car make and year model. The dataset has the following schema:

|    Column     |                      Type                       |
| :-----------: | :---------------------------------------------: |
|  Incident_id  |                       INT                       |
| incident_type | STRING(I: initial sale; A: accident, R: repair) |
|  vin_number   |                     STRING                      |
|     make      |                     STRING                      |
|     model     |                     STRING                      |
|     year      |                     STRING                      |
| incident_date |                      DATE                       |
|  description  |                     STRING                      |

The detailed file is in CSV format, labeled car_accidents.csv. This MapReduce code is sub-divided into two mappers and two reducers, as summarized below.

## Mapper 1

The first mapper will display only the data needed for the subsequent calculations. Specifically, the **vin_number** is the key and the values are the **incident_type**, **make**, and **year**. The expected output is as follows:







## Reducer 1

As shown above, there are entries which do not contain the make and the year model. Further, we are only interested in incident_types of initial sale, i.e., 'I'. Thus, this reducer will populate the group-level information based on **vin_number** and filter out records that are not of **incident_type** 'I'. The expected output is as follows:



## Mapper 2 

Now that only the pertinent records are retained, the next mapper will assign a value of '1' for each entry.  The expected output is as follows:







## Reducer 2

For the final reducer, the make and the year are used as a composite key, which are then tied to the value as the count. The output yields the number of incidents reported for a car with a specific make and year, as shown below:



