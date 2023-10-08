import pandas as pd
from html import escape
import argparse

parser = argparse.ArgumentParser(description='CloudTrail CSV data to generate an HTML report.',
                                epilog="""Example usage:
                                event.py -i user.csv -o user_out.html """)

parser.add_argument('-i','--input_file', help='Path to the CloudTrail CSV input file',type=str)
parser.add_argument('-o','--output_file', help='Path to the HTML output file', type=str)

args = parser.parse_args()

html_data = ""

try:
    df = pd.read_csv(args.input_file)
    for index, row in df.iterrows():
        user_name = escape(str(row['User name']))
        aws_access_key = escape(str(row['AWS access key']))
        event_time = escape(str(row['Event time']))
        event_source = escape(str(row['Event source']))
        event_name = escape(str(row['Event name']))
        aws_region = escape(str(row['AWS region']))
        source_ip = escape(str(row['Source IP address']))
        user_agent = escape(str(row['User agent']))
        error_code = escape(str(row['Error code']))
        resources = escape(str(row['Resources']))
        request_id = escape(str(row['Request ID']))
        event_id = escape(str(row['Event ID']))
        read_only = escape(str(row['Read-only']))
        event_type = escape(str(row['Event type']))
        recipient_account_id = escape(str(row['Recipient Account Id']))
        event_category = escape(str(row['Event category']))

        event_html = f"""
        <div class="event">
            <p><strong>User Name:</strong> {user_name}</p>
            <p><strong>AWS Access Key:</strong> {aws_access_key}</p>
            <p><strong>Event Time:</strong> {event_time}</p>
            <p><strong>Event Source:</strong> {event_source}</p>
            <p><strong>Event Name:</strong> {event_name}</p>
            <p><strong>AWS Region:</strong> {aws_region}</p>
            <p><strong>Source IP Address:</strong> {source_ip}</p>
            <p><strong>User Agent:</strong> {user_agent}</p>
            <p><strong>Error Code:</strong> {error_code}</p>
            <p><strong>Resources:</strong> {resources}</p>
            <p><strong>Request ID:</strong> {request_id}</p>
            <p><strong>Event ID:</strong> {event_id}</p>
            <p><strong>Read-Only:</strong> {read_only}</p>
            <p><strong>Event Type:</strong> {event_type}</p>
            <p><strong>Recipient Account Id:</strong> {recipient_account_id}</p>
            <p><strong>Event Category:</strong> {event_category}</p>
        </div>
        <br> <!-- Add a line break after each event -->
        """
        html_data += event_html

    html_document = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudTrail Events</title>
    </head>
    <body>
        <h1>CloudTrail Events</h1>
        {html_data}
    </body>
    </html>
    """
    with open(args.output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_document)

    print(f"HTML document saved to '{args.output_file}'.")

except IOError:
    print(f"File '{args.input_file}' not found.")
except Exception as e:
    print("An error occurred:", str(e))
