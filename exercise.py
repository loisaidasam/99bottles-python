
class Bottles(object):
    PHRASE = ("%s bottles of beer on the wall, %s bottles of beer.\n"
              "Take one down and pass it around, %s bottle%s of beer on the wall.")
    PHRASE_NONE = ("No more bottles of beer on the wall, no more bottles of beer.\n"
                   "Go to the store and buy some more, 99 bottles of beer on the wall.")
    PHRASE_ONE = ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                  "Take it down and pass it around, no more bottles of beer on the wall.")

    def verse(self, num):
        if not num:
            return Bottles.PHRASE_NONE
        if num == 1:
            return Bottles.PHRASE_ONE
        plural_s = num - 1 != 1 and 's' or ''
        return Bottles.PHRASE % (num, num, num - 1, plural_s)

    def verses(self, start, end):
        step = start < end and 1 or -1
        phrases = []
        while start != end:
            phrases.append(self.verse(start))
            start += step
        phrases.append(self.verse(end))
        return "\n\n".join(phrases)

    def song(self):
        return self.verses(99, 0)
