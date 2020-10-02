### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card): 
    if card.value = 1:  # Should use 2 equal signs (==) so that is is comparing and not assigning
      return True
    else                # There is no colon (:) after else
      return False

  dif highest_card(self, card1 card2):  # Should start "def" and not "dif", also there is a comma missing between card1 and card2
  if card1.value > card2.value:         # Indentation of full if/else statement, should all be indented from the function definition line
    return card                         # Card is not defined, it should read "card1"
  else:
    return card2
  

def cards_total(self, cards):
  total                                     # The "total" variable has not been assigned anything, it should read "total = 0"
  for card in cards:
    total += card.value
    return "You have a total of" + total    # Return statement is indented incorectly, it should line up with the for statement.

    # Indentation of this full last function is out, it needs to line up with the other 2 functions, by being indented by 1 more step.
  
```
