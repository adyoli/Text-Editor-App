import tkinter as tk
import yaml

class Highlighter:
    def __init__(self,text_area,syntax_file):
        self.text_area = text_area
        self.syntax_file = syntax_file
        self.categories = None
        self.numbers_color = "blue"
        self.strings_color = "red"
        self.invalid_prefix = ["_", "-", "."]

        self.parse_syntax_file()

        self.text_area.bind('<KeyRelease>', self.on_key_release)
        

    def on_key_release(self, event=None):
        self.highlight()


    def highlight(self, event=None):
        length=tk.IntVar()

        for category in self.categories:
            matches = self.categories[category]["matches"]

            for keyword in matches:
                start = 1.0
                keyword = keyword + "[^A-Za-z_-]"
                idx = self.text_area.search(keyword,start,stopindex=tk.END,count=length,regexp=1)

                while idx:
                    char_match = char_match = int(str(idx).split('.')[1])
                    line_of_char = int(str(idx).split('.')[0])
                    if char_match > 0:
                        previous_char_index = str(line_of_char) + '.' + str(char_match - 1)    
                        previous_char = self.text_area.get(previous_char_index, previous_char_index + "+1c")

                        if previous_char.isalnum() or previous_char in self.invalid_prefix:
                            end = f"{idx}+{length.get() - 1}c"
                            start = end
                            idx = self.text_area.search(keyword, start, stopindex=tk.END,regexp=1)
                        else:
                            end = f"{idx}+{length.get() - 1}c"
                            self.text_area.tag_add(category, idx, end)
                            start = end
                            idx = self.text_area.search(keyword, start, stopindex=tk.END,regexp=1)
                    else:
                        end = f"{idx}+{length.get() - 1}c"
                        self.text_area.tag_add(category, idx, end)
                        start = end
                        idx = self.text_area.search(keyword, start, stopindex=tk.END,regexp=1)

                self.highlight_regex(r"(\d)+[.]?(\d)*", "number")
                self.highlight_regex(r"[\'][^\']*[\']", "string")
                self.highlight_regex(r"[\"][^\']*[\"]", "string")


    def highlight_regex(self, regex, tag):
        length = tk.IntVar()
        start = 1.0
        idx = self.text_area.search(regex, start, stopindex=tk.END, regexp=1,count=length)
        while idx:
            end = f"{idx}+{length.get()}c"
            self.text_area.tag_add(tag, idx, end)
            start = end
            idx = self.text_area.search(regex, start, stopindex=tk.END, regexp=1, count=length)


    def parse_syntax_file(self):
        with open(self.syntax_file, 'r') as stream:
            try:
                config = yaml.load(stream)
            except yaml.YAMLError as error:
                print(error)
                return

        self.categories = config['categories']
        self.numbers_color = config['numbers']['color']
        self.strings_color = config['strings']['color']

        self.configure_tags()


    def configure_tags(self):
        for category in self.categories.keys():
            color = self.categories[category]['color']
            self.text_area.tag_configure(category, foreground=color)

        self.text_area.tag_configure("number", foreground=self.numbers_color)
        self.text_area.tag_configure("string", foreground=self.strings_color)


if __name__ == '__main__':
    w = tk.Tk()
    text = tk.Text(w)
    text.pack()
    h = Highlighter(text, 'languages/python.yaml')
    w.mainloop()
