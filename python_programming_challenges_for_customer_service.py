# question 2 task 1
class TicketTracker:
    def initialize(self):
        self.tickets = {
            "Ticket01": {"Customer": "Brandy", "Issue": "Login Problem", "Status":"open"},
            "Ticket02": {"Customer": "Meredith", "Issue": "Accidental double payment", "Status": "open"},
            "Ticket03": {"Customer": "Miranda", "Issue": "Cannot create account", "Status": "closed"}
        }
        self.next_ticket = 3

    def new_ticket(self, customer, issue):
        ticket_number = f"Ticket{self.next_ticket:03d}"
        self.tickets[ticket_number] = {
            "Customer": customer,
            "Issue": issue,
            "Status": "open" 
        }
        self.next_ticket += 1


    def update_status(self, ticket_number, new_status):
        if ticket_number in self.tickets:
            if new_status in {"open", "closed"}:
                self.tickets[ticket_number]["Status"] = new_status
                print(f"Ticket '{ticket_number}' updated to '{new_status}'")
            else:
                print("Invalid")

    def display(self, filter=None):
        for ticket_number, info in self.tickets.items():
            customer = info["Customer"]
            issue = info["Issue"]
            status = info["Status"]

            if filter is None or status == filter:
                print(f"{ticket_number} | {customer} | {issue} | {status}")

def main():
    system = TicketTracker()

    print("Initial tickets:")
    system.display()

    system.new_ticket("Dexter", "Can't remember username")

    system.update_status("Ticket002", "closed")

    print("\nAll tickets:")
    system.display()

    print("\nOpen tickets:")
    system.display(filter="open")


if __name__ == "main":
    main()