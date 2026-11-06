def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
def main():
        inputtaken=input()
        print(convert(inputtaken))
if __name__=="__main__":
    main()
