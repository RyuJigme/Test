def generate_multiplication_table(number,limit):
    print(f"Multiplication table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        print(f"{number}*{i}={number*i}")

def main():
    num = int(input("Enter the number for the multiplication table:"))
    lim = int(input("Enter the limit up to which you want the table generated:"))
    generate_multiplication_table(num, lim)

if __name__ == "__main__":
    main()