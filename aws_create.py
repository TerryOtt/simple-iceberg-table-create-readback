import json
import os
import polars
import pyiceberg.catalog
import pyiceberg.table


aws_region: str = "us-east-2"
iceberg_namespace: str = "dataset_xyz_namespace"
catalog_name: str = "aws_catalog"
iceberg_table_name: str = "dataset_xyz_table"
#s3_bucket_path: str = f"s3://{iceberg_table_name}"
table_s3_bucket_name: str = "firsttracks-net-iceberg-demo"

def _main() -> None:
    
    data: dict[str, list[str | int]] = {
        "Fruit": ["Apple", "Apple", "Pear"],
        "Color": ["Red", "Yellow", "Green"],
        "Count": [2, 1, 1]
    }

    polars_df: polars.DataFrame = polars.DataFrame(data)

    print(f"\n{polars_df}")

    iceberg_catalog: pyiceberg.catalog.Catalog = pyiceberg.catalog.load_catalog(
        catalog_name,
        **{
            "type"                  : "rest",
            "uri"                   : f"https://glue.{aws_region}.amazonaws.com/iceberg",
            "rest.sigv4-enabled"    : "true",
            "rest.signing-name"     : "glue",
            "rest.signing-region"   : aws_region,
            "glue.region"           : aws_region,
            # "warehouse"             : f"{os.environ.get('AWS_ACCOUNT_ID')}",
            # "s3.region"             : aws_region,
        }
    )

    # Before we create our namespace, do any exist?
    print("\nCatalog namespaces (aka, \"AWS Glue Data Catalog Databases\"):\n"
          f"{json.dumps(iceberg_catalog.list_namespaces()[0], indent=4, sort_keys=True)}")

    # Create namespace -- this is a catalog ONLY operation,
    iceberg_catalog.create_namespace_if_not_exists(iceberg_namespace)

    print("\nCatalog namespaces (aka, \"AWS Glue Data Catalog Databases\"):\n"
          f"{json.dumps(iceberg_catalog.list_namespaces()[0], indent=4, sort_keys=True)}")

    # Create table with required namespace identifier
    # new_iceberg_table: pyiceberg.table.Table = iceberg_catalog.create_table(
    #     f"{iceberg_namespace}.{iceberg_table_name}",
    #     schema=polars_df.to_arrow().schema
    # )

    #
    # # Now write the contents of our Polars dataframe to our Iceberg table,
    # #       using our catalog handle so ACID guarantees are protected
    # polars_df.write_iceberg(new_iceberg_table, mode='append')
    #
    # # data created (Parquet format)
    #
    # # Metadata updated with
    # #   current table metadata version
    # #   previous table metadata version
    #
    # print( "\n"
    #        "*********************************************************\n"
    #       f"BoringTable catalog  : {catalog_json}\n"
    #       f"Apache Iceberg table : {iceberg_dir}\n"
    #        "*********************************************************\n"
    #        "\n" )


if __name__ == "__main__":
    _main()
