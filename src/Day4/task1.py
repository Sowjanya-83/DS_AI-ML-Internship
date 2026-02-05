contacts={"sowjanya":9876543210,
          "sujanya":8765432109,
          "sujaini":7654321098}
contacts["gagan"]=6543210987
contacts["sowjanya"]=9876543210
existing_contact = contacts.get("sujaini", "Contact not found")
missing_contact = contacts.get("ramesh", "Contact not found")
print("Safe Lookups:")
print("sujaini:", existing_contact)
print("ramesh:", missing_contact)
print("\nContact List:")

# Iterate through the dictionary and print all contacts
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
