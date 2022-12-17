import PyPDF2


def text_from_file(filename: str) -> list[str]:
    text = []
    f = open(filename, "rb")
    reader = PyPDF2.PdfFileReader(f)
    for num in range(reader.getNumPages()):
        page = reader.getPage(num)
        text.append(page.extractText())
    return text


def main():
    text = text_from_file(r"C:\Users\ashbyp\Dropbox\Fitness\HYROX\training_plan.pdf")
    for t in text:
        t = t.replace("During week 1-7 you can select weekdays as you like as long as you follow the sessions in order.For week 8 you should stick to our recommendation.", "")
        t = t.replace("WARM UP", "\n\n\nWARM UP\n")
        t = t.replace("WORKOUT", "\n\nWORKOUT\n")
        t = t.replace("CORE", "\n\nCORE\n")
        t = t.replace("FOR TIME", "FOR TIME\n")
        t = t.replace("1 Round", "\n1 Round\n")
        t = t.replace("Superman", "Superman\n")
        t = t.replace("**", "\n **")
        for r in range(2, 11):
            t = t.replace(f"{r} Rounds", f"\n{r} Rounds\n")
        print(t)


if __name__ == '__main__':
    main()