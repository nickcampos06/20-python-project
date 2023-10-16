# Write your code here
import time

def set_alarm(alarm_time):
    hour_when_set = time.localtime().tm_hour
    minute_when_set = time.localtime().tm_min
    second_when_set = time.localtime().tm_sec

    seconds_into_day_when_set = (hour_when_set * 3600) + (minute_when_set * 60) + second_when_set

    hour_alarm_time = int(alarm_time[0])
    minute_alarm_time = int(alarm_time[1])
    second_alarm_time = int(alarm_time[2])

    seconds_into_day_when_alarm = (hour_alarm_time * 3600) + (minute_alarm_time * 60) + second_alarm_time

    if seconds_into_day_when_set > seconds_into_day_when_alarm:
        seconds_into_day_when_alarm += 86400
    
    seconds_until_alarm = seconds_into_day_when_alarm - seconds_into_day_when_set

    time.sleep(seconds_until_alarm)

    print('Wake up!')
    
if __name__ == '__main__':
    alarm_time = input('Enter the time for the alarm (HH:MM:SS): ')
    alarm_time = alarm_time.split(':')
    set_alarm(alarm_time)