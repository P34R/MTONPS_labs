import math
from datetime import datetime
from decimal import Decimal, getcontext
import mpmath
from math import comb
from fractions import Fraction
from dataclasses import dataclass


@dataclass
class Saved:
    x: float
    e: float
    fxe: float
    N: int


getcontext().prec = 99  # You can adjust this value based on required precision


def bernoulli(n):
    if n == 0:
        return Fraction(1)

    if n == 1:  # convention
        return Fraction(-1 / 2)

    somme = Fraction(0)

    if n % 2:  # B(n) = 0 when n is odd
        return somme

    for k in range(n):
        somme += bernoulli(k) * comb(n, k) / (n + 1 - k)

    return -somme


# Function to compute even Euler numbers using Decimal
def euler_number(n):
    # Euler numbers follow a known recurrence relation for even n
    if n == 0:
        return (1.0)
    elif n == 2:
        return (-1.0)
    elif n % 2 != 0:
        return (0)
    E = float(1)
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue
        temp = comb(n, i - 1)
        temp_2 = math.pow(2, i) - math.pow(4, i)
        temp_2 = temp_2 / i
        final = temp * temp_2 * float(bernoulli(i))
        E += final
    return E


# Function to compute hyperbolic secant using Maclaurin series with given accuracy
def maclaurin_sch(x, e):
    if abs(x) >= math.pi / 2:
        raise ValueError("x must satisfy |x| < pi/2")
    # except ValueError as er:
    #   print(er)
    #  exit(1)
    if e <= 0 or e >= 1:
        raise ValueError("Accuracy e must be in range (0, 1).")
    sum_series = 1.0  # Initial term of the series (1)
    n = 1

    while True:
        # Compute the nth term
        top = euler_number(2 * n) * math.pow(x, 2 * n)
        bottom = math.factorial(2 * n)
        term = float(top) / float(bottom)
        if abs(term) < e:  # If term is smaller than accuracy, stop
            break
        sum_series += term
        n += 1
    return sum_series, n


CONST_MAX_FILES = 5

def save_calcs(filename,calcs):
    filename=filename+".txt"
    date_str = datetime.now().strftime("%d.%m.%Y")
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            for result in calcs:
                x = result.x
                e = result.e
                f_x_e = result.fxe
                N = result.N
                f.write(f"{date_str}, {x}, {e}, {f_x_e:.12f}, {N}\n")
    except Exception as ex:
        print("An error occurred while writing to the file: 1", ex)
        return 0
    # Count total number of entries in the file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            total_entries = sum(1 for line in f)
    except Exception as ex:
        print("An error occurred while reading the file: 2", ex)
        return None
    return total_entries


# Main code
def main():
    calcs = []
    files = []
    last_file = ""

    while True:
        x = input("Enter x (|x| < pi/2): ")
        if x.strip().lower() == "end":
            if len(calcs) == 0:
                print("Nothing to save. Closing the program")
                break
            save_to_file = input("Would you like to save the result to file (yes or anything else means no):").strip()
            if save_to_file.lower()=="yes":
                if last_file!="":
                    print(f"saving results to {last_file}")
                    save_calcs(last_file,calcs)
                else:
                    file_prompt = "Enter a new file name (up to 5 letters or '*' to cancel and exit: "
                    filename = input(file_prompt).strip()
                    if filename == '*':
                        print("Data not saved to file")
                        break
                    else:
                        if 1 <= len(filename) <= 5:
                            total_entries = save_calcs(filename, calcs)
                            if total_entries!=0:
                                print(f"Data saved to file '{filename}'. Total number of entries: {total_entries}")
                                files.append(filename)
                                last_file = filename
                            else:
                                print("Filename must be 1 to 5 characters long.")
                                continue
        else:
            try:
                x = float(x)
                if abs(x) >= math.pi / 2:
                    raise ValueError("x must satisfy |x| < pi/2")
            except ValueError as er:
                print(er)
                exit(1)
            try:
                e = float(input("Enter accuracy e (0 < e < 1):"))
                if e <= 0 or e >= 1:
                    raise ValueError("Accuracy e must be in range (0, 1).")
            except ValueError as er:
                print(er)
                exit(1)

            result, N = maclaurin_sch(x, e)
            calcs.append(Saved(x,e,result, N))
            print(f"Hyperbolic secant of {x} is approximately {result:.20f}.")
            print(f"Straight hyperbolic secant of {x} is {mpmath.sech(x)}.")
            print(f"The last index N used was {N}.")




# Run the program
if __name__ == "__main__":
    main()
'''

    '''