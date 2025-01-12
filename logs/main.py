import sys

def parse_log_line(line: str) -> dict:
    if len(line.strip()) < 3:
        return {}
    try:
        splitting = line.split(' ')
        date, time, loglevel = splitting[:3]
        message = ' '.join(splitting[3:])
        info_dict = {'date': date, 'time': time, 'loglevel': loglevel.upper(), 'message': message, 'message_count': len(message.split())}
        return info_dict
    except FileNotFoundError:
        return 'File does not exist.'
    except TypeError:
        return 'Wrong type.'
    except ValueError:
        return {}

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='UTF_8') as fl:
            return [log for line in fl if (log := parse_log_line(line))]
    except FileNotFoundError:
        return 'File is not found.'

def filter_logs_by_level(logs: list, level: str) -> list:
    try:
        return list(filter(lambda log: log[3:3] == level.upper(), logs))
    except FileNotFoundError:
        return 'File is not found.'

def count_logs_by_level(logs: list) -> dict:
    try:
        count_dict = {}
        for log in logs:
            if 'loglevel' in log:
                count_dict.setdefault(log['loglevel'], 0)
                count_dict[log['loglevel']] += 1
        return count_dict
    except FileNotFoundError:
        return 'File is not found.'
    
def display_log_counts(counts: dict):
    print(f"{'Log level':<9} | {'Quantity':^2}")
    print('--------------------')
    for key, value in counts.items():
        print(f'{key:<9} | {value:^2}')

def display_level_info(logs: list, level: str, ):
    print(f"Log details for level '{level}':")
    for log in logs:
        if log['loglevel'] == level.upper():
            print(f'{log["date"]} {log["time"]} - {log["message"]}')

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    path_to_file = sys.argv[1]
    logs = load_logs(path_to_file)
    countlogs = count_logs_by_level(logs)
    display_log_counts(countlogs)
    
    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()
        levellog = filter_logs_by_level(logs, log_level)
        display_level_info(levellog, log_level)
        
if __name__ == '__main__':
    main()
    
# display_log_counts(count_logs_by_level(load_logs('logfile.log')))
# display_level_info(load_logs('logfile.log'), 'INFO')