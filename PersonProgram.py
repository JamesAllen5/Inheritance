import PersonClass as pc

per = pc.Person(
    "James",
    "1025 La Salle Ave",
    8172338016,
)

cust = pc.Customer("Andrew", "1025 La Salle", 8171234567, "001", True)

per.print_person()
cust.print_person()
