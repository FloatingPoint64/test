import datetime


if __name__ == "__main__":
    now = datetime.datetime.now()
    now_str = now.strftime("%Y/%m/%d %H-%M-%S")
    print(f"{now_str}: Hello world!!")

