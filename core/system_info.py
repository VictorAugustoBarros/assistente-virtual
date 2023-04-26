from datetime import datetime


class SystemInfo:
    def __init__(self):
        pass

    def get_time(self):
        now = datetime.now()
        answer = f"São {now.hour} horas e {now.minute} minutos"
        return answer


if __name__ == '__main__':
    answer = SystemInfo().get_time()
    print(answer)
