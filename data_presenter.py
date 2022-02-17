from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("_mpl-gallery")



invoices = open("CupcakeInvoices.csv")

# Open the CupcakeInvoices.csv.

# Loop through all the data and print each row.

# Loop through all the data and print the type of cupcakes purchased.
# for invoice in invoices:
#     print(invoice)
#     print(invoice.split(",")[2])

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

# for invoice in invoices:
#     print(invoice.split(",")[4])

# Loop through all the data, and print out the total for all invoices combined.

# total = 0
# for invoice in invoices:
#     total += float(invoice.split(",")[3])
# print(total)

totals = {
    "Chocolate": 0,
    "Vanilla": 0,
    "Strawberry": 0
}

for invoice in invoices:
    line = invoice.split(",")
    totals[line[2]] += float(line[3]) * float(line[4])
print(totals)

x = [1,2,3]
y = []

for total in totals.values():
    y.append(total)

print(y)

fig, ax = plt.subplots()

# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

x_pos = np.arange(len(totals))
ax.bar(x_pos,y, color=[(.42, .25, .15 ,1), 'beige', 'pink'], edgecolor = "black")
ax.set_xticks(x_pos, labels=totals.keys())
ax.set_ylim(0, 450)
ax.set_yticks(np.arange(0, 450, 50))

font1 = {'family': 'sans-serif', 'color': 'black', 'size': 18}

ax.set_title("Cupcake Sales", fontdict = font1)
ax.set_xlabel('Flavor', fontdict = font1)
ax.set_ylabel('Sales ($)', fontdict = font1)



# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# x_pos = np.arange(0, 4)

# ax.set_xlim()
# ax.set_xticks(x_pos, labels=totals.keys())

# ax.set(xlim=(0, 4),
#        ylim=(0, 150), yticks=np.arange(0, 150, 25))
    
plt.tight_layout()
plt.show()

# Close your open file.
invoices.close()