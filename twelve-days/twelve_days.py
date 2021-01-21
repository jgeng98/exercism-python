nth = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

gifts = ["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens", "four Calling Birds", "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]

def recite(start_verse, end_verse):
    lines = []
    for day in range(start_verse-1, end_verse):
        lines.append(f"On the {nth[day]} day of Christmas my true love gave to me:") 
        for gift in range(day, -1, -1):
            if gift == 0 and day != 0:
                lines[len(lines)-1] += f" and {gifts[gift]}."
            elif gift == 0 and day == 0:
                lines[len(lines)-1] += f" {gifts[gift]}."
            else:
                lines[len(lines)-1] += f" {gifts[gift]},"
    return lines
