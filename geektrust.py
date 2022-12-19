from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    items = {"tshirt": 1000, "jacket": 2000,
             "cap": 500, "notebook": 200, "pens": 300, "markers": 500}
    clothing = ["tshirt", "jacket", "cap"]
    stationery = ["notebook", "pens", "markers"]
    discount = {"tshirt": 0.1, "jacket": 0.05,
                "cap": 0.2, "notebook": 0.2, "pens": 0.1, "markers": 0.05}
    output = 0
    l = {}
    for line in lines:
        # Add your code here to process input commands.
        arg = line.strip().split(" ")
        if arg[0] == "ADD_ITEM":
            if arg[1].lower() in clothing:
                if int(arg[2]) > 2:
                    print("ERROR_QUANTITY_EXCEEDED")
                else:
                    output = output + items[arg[1].lower()]*int(arg[2])
                    l[arg[1]] = int(arg[2])
                    print("ITEM_ADDED")
            elif arg[1].lower() in stationery:
                if int(arg[2]) > 3:
                    print("ERROR_QUANTITY_EXCEEDED")
                else:
                    output = output + items[arg[1].lower()]*int(arg[2])
                    l[arg[1]] = int(arg[2])
                    print("ITEM_ADDED")
        if arg[0] == "PRINT_BILL":
            result = output
            dis = 0
            if output >= 1000:
                for i in l.items():
                    dis = dis + items[i[0].lower()]*i[1]*discount[i[0].lower()]
            amount = result-dis
            if amount >= 3000:
                dis = dis + (amount/20)
                amount = amount - (amount/20)
            print("TOTAL_DISCOUNT {:.2f}".format(dis))
            print("TOTAL_AMOUNT_TO_PAY {:.2f}".format((amount)+((amount)/10)))


if __name__ == "__main__":
    main()