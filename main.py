from data_processor import DataProcessor


def main():
    data_processor = DataProcessor('TV')
    data_processor.collect_sensor_data()
    data_processor.analyze_sensor_data()
    data_processor.print_analysis_result()