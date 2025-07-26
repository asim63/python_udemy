from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name","Type"]
table.add_rows(
    [
        ["Pikachu","Electric"],
        ["Squirtle","Water"],
        ["Charmander","Fire"],
    ]
)

# table.add_column("Remarks",["pika pika","squirtle squirt","chaamandaaa"])
print(table)

table.align ="l"
print(table)
# table = PrettyTable()
# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_divider()
# table.add_row(["Brisbane", 5905, 1857594, 1146.4], divider=True)
# table.add_rows(
#     [["Darwin", 112, 120900, 1714.7],
#      ["Hobart", 1357, 205556, 619.5]],
#     divider=True
# )
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])

# #sort by population

# table.sortby = "Population"

# print(table)
# from prettytable import TableStyle

# table.set_style(TableStyle.MARKDOWN)
# print(table)
