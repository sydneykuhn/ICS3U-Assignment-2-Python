#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the area of a parallelogram
#    with the dimensions provided by user


def main():

    # this function calculates the area

    # input
    print("Calculate the area of a parallelogram:")
    base = int(input("Enter base of the parallelogram (mm): "))
    height = int(input("Enter height of the parallelogram (mm): "))

    # process
    area = base * height

    # output
    print("")
    print("The area is {0} mm².".format(area))
    print("Done.")


if __name__ == "__main__":
    main()
