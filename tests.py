from functions.run_python_file import run_python_file

def main():
    calc_instruc = run_python_file("calculator", "main.py")
    calc_program =run_python_file("calculator", "main.py", ["3 + 5"])
    calc_test = run_python_file("calculator", "tests.py")
    calc_error = run_python_file("calculator", "../main.py")
    calc_nofile = run_python_file("calculator", "nonexistent.py")
    
    print(calc_instruc)
    print(calc_program)
    print(calc_test)
    print(calc_error)
    print(calc_nofile)

if __name__ == "__main__":
    main()