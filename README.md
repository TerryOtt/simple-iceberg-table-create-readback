# Local Iceberg Demo

## Summary 

Demonstrating how to create, read, and write data to/from Apache Iceberg tables in Python.


## Iceberg Catalog

This demo uses [Boring Catalog](https://github.com/boringdata/boring-catalog) for its 
[Iceberg Catalog](https://medium.com/itversity/iceberg-catalogs-a-guide-for-data-engineers-a6190c7bf381).
Boring Catalog is dead-simple, consisting of a single JSON file for all its state. Full stop.
Since this demo is striving for _simple_, Boring Catalog is all that's needed. No need to launch other software 
like Hive Metastore backed by MySQL/PostgreSQL or use a cloud provider's managed Iceberg catalog service 
such as 
[AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-pyiceberg.html).


## AWS

### Glue Data Catalog

In the console, create a new Database (under Data Catalog) called 

### S3 Bucket

Create an S3 bucket and note the ARN.

### IAM Permissions

Using AWS Glue for the Iceberg Catalog and S3 for the Iceberg Table requires the following permissions:

* AWS Glue Data Catalog
    * `glue:CreateDatabase`
    * `glue:CreateTable`
    * `glue:DeleteDatabase`
    * `glue:DeleteTable`
    * `glue:GetCatalog`
    * `glue:GetDatabase`
    * `glue:GetDatabases`
    * `glue:GetTable`
    * `glue:GetTables`
    * `glue:UpdateDatabase`
    * `glue:UpdateTable`

Create an IAM role with these permissions then set your credentials to assume that role 
(e.g., Access Key and Secret Access Key). 

## Usage

_Note_: instructions assume `uv` is already installed in your environment.

### Iceberg Table Stored In Local File System

```
$ uv run local_create.py

shape: (3, 3)
┌───────┬────────┬───────┐
│ Fruit ┆ Color  ┆ Count │
│ ---   ┆ ---    ┆ ---   │
│ str   ┆ str    ┆ i64   │
╞═══════╪════════╪═══════╡
│ Apple ┆ Red    ┆ 2     │
│ Apple ┆ Yellow ┆ 1     │
│ Pear  ┆ Green  ┆ 1     │
└───────┴────────┴───────┘

*********************************************************
BoringTable catalog  : ./data/catalogs/catalog_local.json
Apache Iceberg table : ./data/iceberg_table
*********************************************************


$ uv run local_query.py

Full table data out of Iceberg:

shape: (3, 3)
┌───────┬────────┬───────┐
│ Fruit ┆ Color  ┆ Count │
│ ---   ┆ ---    ┆ ---   │
│ str   ┆ str    ┆ i64   │
╞═══════╪════════╪═══════╡
│ Apple ┆ Red    ┆ 2     │
│ Apple ┆ Yellow ┆ 1     │
│ Pear  ┆ Green  ┆ 1     │
└───────┴────────┴───────┘

$
```

