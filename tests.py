from functions.get_file_content import get_file_content

def main():
    calculator_main = get_file_content("calculator", "main.py")
    calculator_pkgSlashcalculator = get_file_content("calculator", "pkg/calculator.py")
    calculator_SlashbinSlashcat = get_file_content("calculator", "/bin/cat")
    calculator_pkgSlashdoesnotexist = get_file_content("calculator", "pkg/does_not_exist.py")

    print(calculator_main)
    print(calculator_pkgSlashcalculator)
    print(calculator_SlashbinSlashcat)
    print(calculator_pkgSlashdoesnotexist)

if __name__ == "__main__":
    main()