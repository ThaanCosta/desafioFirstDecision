# main.py

from monitoramento import check_services, backup_files, monitor_resources, check_updates, generate_report

if __name__ == "__main__":
    check_services()
    backup_files()
    monitor_resources()
    check_updates()
    generate_report()
