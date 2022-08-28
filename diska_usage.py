import shutil
import argparse
import datetime
import time


def get_free_space(path):
    """
    Возврат пустого места на диске по ссылке
    """
    _, _, free_space = shutil.disk_usage(path)
    return free_space


def convert_to_readebl(path):
    """
    Конвертация в в читабельный виод
    """
    free_space = get_free_space(path)
    converted = ''
    for unit, id in zip(['k', 'M', 'G', 'T', 'P'], range(10, 50, 10)):
        usage_human = (free_space % (2 ** (id + 10))) // (2 ** id)
        if usage_human == 0:
            break
        converted = f"{usage_human}{unit} {converted}"
    return converted


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="Path for using the disk usage", type=str)
    parser.add_argument('-n', '--interval',
                        help="Interval in seconds (default: 2)",
                        type=int, default=2)
    args = parser.parse_args()
    while True:
        readeble = convert_to_readebl(args.path)
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{cur_time} {readeble}")
        time.sleep(args.interval)