import datetime
import os


def parse_filename(filename):
    base = os.path.splitext(filename)[0]
    parts = base.split('_')
    if len(parts) != 4:
        raise ValueError(f"Incorrect filename format: {filename}")
    return {
        'setup_name': parts[0],
        'topology': parts[1],
        'branch': parts[2],
        'test_name': parts[3]
    }


def parse_test_result(file_path):
    report_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(': ', 1)
                report_data[key.lower().replace(' ', '_')] = value
    return report_data


def generate_report(directory: str):
    report = []
    for filename in os.listdir(directory):
        file_info = parse_filename(filename)
        result = parse_test_result(os.path.join(directory, filename))
        file_info['result'] = result
        report.append(file_info)

    return report


def print_report(report):
    print(f"Daily regression report {datetime.datetime.now().strftime('DD-MM-YY')}\n"
          f"Setup Name: {report[0]['setup_name']}\n"
          f"Topology: {report[0]['topology']}\n"
          f"Branch: {report[0]['branch']}\n"
          f"List of tests:")
    for test_index, test_status in enumerate(report):
        print(f"{report[test_index]['test_name']}: {test_status['result']['result']}")


if __name__ == "__main__":
    # /mswg/projects/sx_plvision_os/sonic_reports/20180612
    report = generate_report(directory="/Users/ystasiv/pythonProject/rep")
    print_report(report)

"""
Daily regression report DD-MM-YY
Setup Name: xxx
   Topology: xxx
   Branch: xxx
   List of tests:
SONIC-DEPLOY-TEST: OK
SONIC-ARP-TEST: OK
       FDB: Not OK
       ...
"""
