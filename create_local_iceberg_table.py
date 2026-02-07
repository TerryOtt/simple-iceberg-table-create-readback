import boringcatalog
import polars
import pyiceberg.table


def _main() -> None:
    
    data: dict[str, list[str | int]] = {
        "Fruit": ["Apple", "Apple", "Pear"],
        "Color": ["Red", "Yellow", "Green"],
        "Count": [2, 1, 1]
    }

    polars_df: polars.DataFrame = polars.DataFrame(data)

    print(polars_df)

    iceberg_catalog: boringcatalog.BoringCatalog = boringcatalog.BoringCatalog(
        name="myicebergcatalog", 
        warehouse="./iceberg_table"
    )

    # Create namespace -- this is a catalog ONLY operation,
    #   nothing is created in warehouse dir
    iceberg_catalog.create_namespace("dataset_xyz_namespace")

    # Create table with required namespace identifier
    #
    #   NOTE: first operation that actually modifies Iceberg table directory structure
    #         creates dataset_xyz_namespace/dataset_xyz_table/metadata/[five digit zero padded version of this table]-[GUID].metadata.json"
    #
    # Only AFTER filesystem changes are all durably persisted to disk, THEN the catalog
    #       is updated. Iceberg operations are atomic, so catalog is only updated when
    #       we know FOR SURE all data is safely on disk
    #
    #       Catalog changes:
    #           - New table in "tables" section" with contents
    #               - Table namespace
    #               - Table's unique name within its namespace
    #               - Pointer to current (latest) metadata file
    #           
    new_iceberg_table: pyiceberg.table.Table = iceberg_catalog.create_table(
        "dataset_xyz_namespace.dataset_xyz_table", 
        schema=polars_df.to_arrow().schema
    )

    # Now write the contents of our Polars dataframe to our Iceberg table, 
    #       using our catalog handle so ACID guarantees are protected
    polars_df.write_iceberg(new_iceberg_table, mode='append')

    # data created (Parquet format)

    # Metadata updated with
    #   current table metadata version
    #   previous table metadata version
    #   
    #   By having metadata with a per-catalog GUID, it allows multiple catalogs to work safely on the same table...
    #       ...if you're crazy enough to allow that
        
    print("Apache Iceberg table created in ./iceberg_table")


if __name__ == "__main__":
    _main()

