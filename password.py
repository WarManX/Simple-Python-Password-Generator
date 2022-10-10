import random
import os
import sys
from colors import Colors as colors


def logo():
    os.system('clear')
    print(colors.BOLD + colors.G + '''

    ╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐┌─┐
    ╠═╝├─┤└─┐└─┐││││ │├┬┘ ││└─┐
    ╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘└─┘
    ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
    ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
    ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─

    ''')


def generatePassword():
    logo()

    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    digits = '0123456789'
    symbols = '!@#$%^&*()/?\\|[]{}~±§+=-_'
    upper, lower, nums, syms = False, False, False, False
    all = ''
    length = 8
    amount = 5
    password = ''

    up = input(colors.G + "[" + colors.O + "+" + colors.G + "] " +
               colors.W + "Would you like to add " + colors.G + "uppercase" + colors.W + "? (Y/n): ")
    lo = input(colors.G + "[" + colors.O + "+" + colors.G + "] " +
               colors.W + "Would you like to add " + colors.G + "lowercase" + colors.W + "? (Y/n): ")
    dig = input(colors.G + "[" + colors.O + "+" + colors.G + "] " +
                colors.W + "Would you like to add " + colors.G + "digits" + colors.W + "? (Y/n): ")
    sym = input(colors.G + "[" + colors.O + "+" + colors.G + "] " +
                colors.W + "Would you like to add " + colors.G + "symbols" + colors.W + "? (Y/n): ")
    try:
        len = input(colors.G + "[" + colors.O + "+" + colors.G + "] " +
                    colors.W + "Enter length of the password (Default 8): ")
        amo = input(colors.G + "[" + colors.O + "+" + colors.G + "] " +
                    colors.W + "Enter number of passwords to generate (Default 5): ")

        if len != "":
            length = int(len)
        if amo != "":
            amount = int(amo)

    except:
        sys.exit(0)

    if up.lower() == "y" or up == "":
        upper = True
    if lo.lower() == "y" or lo == "":
        lower = True
    if dig.lower() == "y" or dig == "":
        nums = True
    if sym.lower() == "y" or sym == "":
        syms = True

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

    print(colors.BOLD + "\n=================[" + colors.G +
          "Passwords" + colors.W + "]=================\n")

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(colors.G + "[" + colors.O + "+" + colors.G + "] " +
              colors.W + password)

    repeat = input(colors.G + "\n[" + colors.O + "+" + colors.G + "] " +
                   colors.W + "Would you like to generate again? (Y/n): ")
    if repeat.lower() == "y" or repeat == "":
        generatePassword()
    else:
        sys.exit()


if __name__ == __name__:
    generatePassword()
