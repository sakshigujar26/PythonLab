def convert_capitalcase(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def change_smallcase(text):
    result = ''
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def change_reversecase(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def change_zigzagcase(text):
    result = ''
    for i, char in enumerate(text):
        if i % 2 == 0:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        else:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    return result

def change_case(text, style):
    if style == 'c' or style == 'C':
        return convert_capitalcase(text)
    elif style == 's' or style == 'S':
        return change_smallcase(text)
    elif style == 'r' or style == 'R':
        return change_reversecase(text)
    elif style == 'z' or style == 'Z':
        return change_zigzagcase(text)
    else:
        return "Please enter a valid style."

def main():
    print(change_case("abcd", 'C'))

if __name__ == "__main__":
    main()

