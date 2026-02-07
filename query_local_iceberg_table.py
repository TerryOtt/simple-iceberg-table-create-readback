import boringcatalog
import polars
import pyiceberg.table


def _main() -> None:
    
    iceberg_catalog: boringcatalog.BoringCatalog = boringcatalog.BoringCatalog(
        name="myicebergcatalog", 
        warehouse="./iceberg_table"
    )

    # Get iceberg table handle from catalog
    iceberg_table: pyiceberg.table.Table = iceberg_catalog.load_table("dataset_xyz_namespace.dataset_xyz_table")
    
    # Get a polars lazyframe (no data, just a plan to get data!) from PyIceberg table
    polars_lf: polars.LazyFrame = iceberg_table.to_polars()

    # Materialize one row of data  -- collect() finalizes query plan smartly retrieves data from Iceberg Table
    #       DataFrames DO have data in them
    polars_singlerow_df: polars.DataFrame = polars_lf.limit(1).collect()
    print(f"\nSingle row:\n{polars_singlerow_df}")

    # Query to get two rows of data
    polars_tworows_df: polars.DataFrame = polars_lf.filter(polars.col("Fruit") == "Apple").collect()
    print(f"\nTwo rows:\n{polars_tworows_df}")
    
    # Get unique names of fruit in descending (Z-A) string order
    polars_uniquefruits: polars.Series = polars_lf.select("Fruit").unique().sort("Fruit", descending=True).collect().get_column("Fruit").rename("Unique Fruits (Descending Order)")
    print(f"\n{polars_uniquefruits}")



if __name__ == "__main__":
    _main()

