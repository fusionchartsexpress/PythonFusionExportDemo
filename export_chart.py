# Import sdk
from fusionexport import ExportManager, ExportConfig
# Import json library
import json


# Load the JSON chart configuration file
chart_json_file = open('chart-config-file.json')
config = json.load(chart_json_file)

# Instantiate the ExportConfig class and add the required configurations
export_config = ExportConfig()
export_config["chartConfig"] = config

# Various options are: 'png', 'jpeg' 'pdf' and 'svg'
export_config["type"] = 'png'

# Port and host of FusionExport Service
export_server_host = "127.0.0.1"
export_server_port = 1337

# Instantiate the ExportManager class
export_manager = ExportManager(export_server_host, export_server_port)

# Call the export() method with the export_config as an argument
export_manager.export(export_config, output_dir = ".", unzip = True)