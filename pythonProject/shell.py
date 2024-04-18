import nathan

while True:
    text = input('nathan >')
    result, error = nathan.run('<stdn>', text)

    if error: print(error.as_string())
    print(result)