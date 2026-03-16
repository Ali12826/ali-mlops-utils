def summarize_data(data_list):
    """A simple MLOps utility to summarize data."""
    if not data_list:
        return "No data provided."

    count = len(data_list)
    return f"MLOps Pipeline received {count} data points successfully!"
