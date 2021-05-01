def run():
    language = "Pytjon"
    age = 30
    message = f"{language} ma już {age} lat"
    print(message)

    # starszy sposób - metoda format
    message_old = "{} ma już {} lat".format(language, age)
    print(message_old)


if __name__ == '__main__':
    run()