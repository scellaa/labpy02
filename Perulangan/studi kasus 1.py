def counting_ticket_price():
    Reguler_ticket = 50000
    VIP_ticket = 100000
    discount_price = 20000  

    ticket_type = (False, True)[input('What kind of ticket u want to buy?(VIP/Reguler): ') == 'Reguler']
    member_status = (False, True)[input('Do you have member card?(Yes/No): ') == 'Yes']

    # Normal Price
    normal_price = Reguler_ticket if ticket_type else VIP_ticket

    # Discount logic
    if member_status:
        final_price = normal_price - discount_price
        print(f'Normal Price   : Rp{normal_price}')
        print(f'Discount Price : Rp{discount_price}')
        print(f'Final Price    : Rp{final_price}')
    else:
        print(f"Ticket Price: Rp{normal_price} (no discount)") 

counting_ticket_price()