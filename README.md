CSV vs Paraquet

CSV (Comma-Separated Values) and Parquet are two popular formats for storing structured data.
CSV is a plain-text format where data is stored row by row, making it easy to read and widely
compatible with various applications. However, CSV files tend to be large and inefficient for 
big data processing since they lack built-in compression and schema enforcement.

Parquet, on the other hand, is a columnar storage format designed for efficient data retrieval
and compression. It is optimized for analytical workloads, making it significantly faster than
CSV when working with large datasets. Parquet enforces a structured schema, reducing storage
space and improving query performance in big data frameworks like Apache Spark and Hadoop.
