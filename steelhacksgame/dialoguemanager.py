import pygame

class DialogueManager:
    def __init__(self, font, txt_path="assets/dialogue.txt", pos=(50, 500)):
        self.font = font
        self.pos = pos
        self.index = 0
        self.finished = False

        # load dialogue from txt
        self.dialogue_list = []
        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                #This slipts the 
                if not line:
                    continue
                if ":" in line:
                    speaker, text = line.split(":", 1)
                    self.dialogue_list.append({"speaker": speaker.strip(), "text": text.strip()})
    #make sure you are not at the end of the dialogue and moving you to the next dialogue
    def next(self):
        self.index += 1
        if self.index >= len(self.dialogue_list):
            self.finished = True
    #show chosen text on screen
    def draw(self, screen):
        if self.finished:
            return
        line = self.dialogue_list[self.index]["text"]
        text_surf = self.font.render(line, True, (255, 255, 255))
        #formatting
        screen.blit(text_surf, self.pos)
