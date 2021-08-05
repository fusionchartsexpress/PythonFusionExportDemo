# Exporting FusionCharts as Image From Python

## Step 1: Download the FusionExport Server
Download the FusionExport server from the [FusionExport website](https://www.fusioncharts.com/download/fusionexport?framework=python)

You need to follow the steps for your OS

## Step 2: Run the server
Find the location of the installed server and run it by typing at the console:

```

YOUR_PATH/fusionexport
```

If the server runs successfully, you will see the following message:

![FusionExport server screen on console](serverPic.png)

## Step 3: Install the FusionExport sdk for Python

At the console type:

```
$ pip install fusionexport
```

## Step 4: Create the chart configuration file
The chart-config-file.json will contain the configuration for the chart you want to export


## Step 5: Create the main Python file and Run it
Create the export_chart.py file, and run the Python file using:

```
Python export_chart.py
```

## Change the Export Type
The following types are valid for exporting a chart:
'png',  'jpeg',  'pdf',  'svg'

In export_chart.py file change the export type as:
export_config["type"] = 'png'
