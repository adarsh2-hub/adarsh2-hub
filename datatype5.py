#You are creating a simple movie ticket system. Create variable for: 1.Movie name,2.Number fo tickets,3.Ticket price,4.Is the show available? Then write a program to-1:print all four values.2:print the data type of each value.3:Calculate and print the total ticket cost.
movie_name="Toxic"
no_of_tickets=100
ticket_price=350
show_available=True
print(movie_name,type(movie_name))
print(no_of_tickets,type(no_of_tickets))
print(ticket_price,type(ticket_price))
print(show_available,type(show_available))
total_ticket_cost=no_of_tickets*ticket_price
print("total ticket cost=",total_ticket_cost)