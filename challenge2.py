# -*- coding: utf-8 -*-
"""Challenge2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rRCDILjj4PhbUELk2oiZKF1PP6CSr5aJ
"""

from google.colab import drive
drive.mount("/content/drive", force_remount=True)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

!pip install pyspark



from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def enrich_user_events(spark, user_events_file, bot_lookup_file, output_file):
    # Read user_events and bot_lookup tables from TSV files
    user_events_df = spark.read.option("header", "true").option("delimiter", "\t").csv(user_events_file)
    bot_lookup_df = spark.read.option("header", "true").option("delimiter", "\t").csv(bot_lookup_file)

    # Convert columns to proper data types
    user_events_df = user_events_df.withColumn("date", col("date").cast("date"))
    user_events_df = user_events_df.withColumn("hour", col("hour").cast("int"))
    user_events_df = user_events_df.withColumn("user_session", col("user_session").cast("int"))
    user_events_df = user_events_df.withColumn("event_timestamp", col("event_timestamp").cast("timestamp"))

    bot_lookup_df = bot_lookup_df.withColumn("date", col("date").cast("date"))

    # Enrich user_events with bot_status information
    enriched_user_events = user_events_df.join(
        bot_lookup_df,
        (user_events_df["date"] == bot_lookup_df["date"]) &
        (user_events_df["user_identifier"] == bot_lookup_df["user_identifier"]),
        "left_outer"
    ).select(
        user_events_df["*"],
        bot_lookup_df["bot_status"]
    )

    # Write the enriched user_events to an output TSV file
    enriched_user_events.write.option("header", "true").option("delimiter", "\t").csv(output_file)

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder.appName("Enrich User Events").getOrCreate()

    # Input and output file paths
    user_events_file = "/content/drive/MyDrive/Task/user_events.tsv"
    bot_lookup_file = "/content/drive/MyDrive/Task/bot_lookup.tsv"
    output_file = "/content/drive/MyDrive/Task/enriched_user_events.tsv"

    # Enrich user_events and write to the output file
    enrich_user_events(spark, user_events_file, bot_lookup_file, output_file)

    # Stop SparkSession
    spark.stop()



import unittest


def test_enrich_user_events():
    # Initialize SparkSession
    spark = SparkSession.builder.appName("Test Enrich User Events").getOrCreate()

    # Input and output file paths
    user_events_file = "/content/drive/MyDrive/Task/user_events.tsv"
    bot_lookup_file = "/content/drive/MyDrive/Task/bot_lookup.tsv"
    output_file = "/content/drive/MyDrive/Task/enriched_user_events.tsv"

    # Enrich user_events and write to the output file
      enrich_user_events(spark, user_events_file, bot_lookup_file, output_file)

    # Load the output file and check the result
    enriched_user_events_df = spark.read.option("header", "true").option("delimiter", "\t").csv(output_file)
    assert enriched_user_events_df.count() == 3  # Check the number of rows

    # Stop SparkSession
    spark.stop()

if __name__ == "__main__":
    test_enrich_user_events()

