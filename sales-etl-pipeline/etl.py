from backend.etl.extract import download_csv_files_from_s3
from backend.etl.transform import validate_and_clean_data
from backend.etl.load import load_data_to_postgres, create_sales_data_table

def run_pipeline():
    print("Starting ETL pipeline...")

    dataframes = download_csv_files_from_s3()

    if not dataframes:
        print("No data found")
        return

    cleaned_data = validate_and_clean_data(dataframes)

    if cleaned_data.empty:
        print("No valid data")
        return

    file_path = "processed_sales.csv"
    cleaned_data.to_csv(file_path, index=False)

    create_sales_data_table()
    load_data_to_postgres(file_path)

    print("ETL completed")

if __name__ == "__main__":
    run_pipeline()