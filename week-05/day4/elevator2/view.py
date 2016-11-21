import texts
import os

class View:
    def draw(self, levels, ppl, cl):
        print(texts.the_top)
        print(texts.the_top_2)
        for i in reversed(range(levels)):
            if i == int(cl):
                if ppl == 0 :
                    print(texts.without_ppl)
                else:
                    print(texts.with_ppl)
            else:
                print(texts.empty_floor)
        print(texts.bottom)

    def functions(self):
        print(texts.functions)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def error_messeage(self):
        print(texts.error_messeage)

    def highest_lv(self):
        print(texts.highest_lv)

    def lowest_lv(self):
        print(texts.lowest_lv)
