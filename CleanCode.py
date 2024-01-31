def _is_member_eligible_for_lending(member_id):
    max_books_to_lend = 2
    _is_eligible = False

    if _is_library_member(member_id):
        books_lent_todate = _get_books_lent_todate(member_id)
        if len(books_lent_todate) < max_books_to_lend:
            _is_eligible = True
        else:
            print("User not eligible, cannot lend more than 2 books")
    else:
        print("User not eligible, User is not a member")

    return _is_eligible
    
def _get_book_return_date():
    lend_time_period = 14
    current_date = date.today()
    return current_date + datetime.timedelta(days = lend_time_period)

def lend_book(member_id, book_id):
    if _is_member_eligible_for_lending(member_id):
        if _is_book_available(book_id):
            return_date = _get_book_return_date()
            _checkout_book(book_id, member_id, return_date)
            print("A book lent for a member successfully")
        else:
            print("Book not available")


