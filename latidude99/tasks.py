from background_task import background
import datetime as dt
import owid.service as service
import owid.service_covid as service_covid


@background(schedule=10)
def back_task_1():
    service.task_test()
    status = {}
    status['task_date'] = dt.datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")
    service_covid.log_to_file(service_covid.LOG_FILE, status)

@background(schedule=14400)
def task_download_and_update_covid():
    status = service.download_and_update_covid()
    status['task_name'] = 'download_and_update_covid'
    status['task_date'] = dt.datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")
    service_covid.log_to_file(service_covid.LOG_FILE, status)


