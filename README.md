# Local Iceberg Demo

## Summary 

Demonstrating how to create, read, and write data to/from Apache Iceberg tables in Python.


## Iceberg Catalog

This demo uses [Boring Catalog](https://github.com/boringdata/boring-catalog) for its 
[Iceberg Catalog](https://medium.com/itversity/iceberg-catalogs-a-guide-for-data-engineers-a6190c7bf381).
Boring Catalog is dead-simple, consisting of a single JSON file for all its state. Full stop.
As we are aiming for _simple_, Boring Catalog is all that's needed. No need to launch other software 
like Hive Metastore backed by MySQL/PostgreSQL or use a cloud provider's managed Iceberg catalog service 
such as 
[AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-pyiceberg.html).


## Usage

_Note_: instructions assume `uv` is already installed in your environment.

```
$ uv run create_local_iceberg_table.py
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Installed 46 packages in 24ms
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
Apache Iceberg table created in ./iceberg_table

$
```

## Query Data From An Iceberg Table

```
$ uv run query_local_iceberg_table.py

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

