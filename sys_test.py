import sys

print(f"Running system is {sys.platform}.")

if sys.argv[1:]:
    print(f"Number of arguments is {len(sys.argv) - 1}.")
    print(f"Actual arguments are:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print(f"No actual arguments.")

