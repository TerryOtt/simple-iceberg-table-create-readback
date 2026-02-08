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


## Usage

_Note_: instructions assume `uv` is already installed in your environment.

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

```

