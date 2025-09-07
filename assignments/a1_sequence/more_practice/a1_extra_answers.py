""" These are my answers to LIN6209 Extra Questions 1 (NOT assessed)"""

from assignments.a1_sequence.a1_answers import *


def add_old_uk_v2(pounds1, shillings1, pennies1, pounds2=0, shillings2=0,
                  pennies2=0):
    """Same as add_old_uk() with two new features:
          default value of the last three parameters is zero
          deals correctly with negative amounts of cash """

    # calculate total pennies same as before.
    total_pennies = psd_to_pennies(pounds1, shillings1,
                                   pennies1) + psd_to_pennies(pounds2,
                                                              shillings2,
                                                              pennies2)
    # convert total pennies to +ve amount by using abs()
    total_pennies_abs = abs(total_pennies)
    # convert to £sd
    p_s_d = pennies_to_psd(total_pennies_abs)
    # convert to original sign by multiplying by original number divided by absolute number
    cr_dr = int(total_pennies / total_pennies_abs)
    return p_s_d[0] * cr_dr, p_s_d[1] * cr_dr, p_s_d[2] * cr_dr


# # now try it out a few times
print(add_old_uk_v2(-1, 19, 11, 0, 0, 0))
print(add_old_uk_v2(0, 0, 0, -1, 19, 11))
print(psd_to_pennies(-1, 19, 11))


def buy_paint(height, width, depth):
    pass
    """Returns the number of litres of paint to buy to paint all six surfaces of a rectangular cuboid with
    sides `height`, `width`, and `depth` meters in length. Paint comes in tins of 10L, 5L and 1L. Cost per litre is
    least for 10L tins and most for 1L tins. One litre of paint covers 10 square meters. Allow for 10% wastage."""
    # total surface area calculate
    area = (height * width + width * depth + depth * height) * 2
    paint = area * 1.1 / 14
    # round paint UP to the next whole digit
    paint = -(-paint // 1)  # a handy little bit of trickery!
    return paint

# If working with integers,
# one way of rounding up is to take advantage of the fact that // rounds down:
# do the division on the negative number,
# then negate the answer.No import, floating point, or conditional needed.
