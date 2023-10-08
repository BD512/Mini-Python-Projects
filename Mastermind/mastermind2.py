
import time,sys
import random

class MasterMind:
    def __init__(self):
        self.digit1 = str(random.randint(0,6))
        self.digit2 = str(random.randint(0,6))
        self.digit3 = str(random.randint(0,6))
        self.digit4 = str(random.randint(0,6))
        self.number = self.digit1 + self.digit2 + self.digit3 + self.digit4
        self.all_results = []
        # self.number = str(random.randint(1000,9999))
        
    def typingPrint(self, text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        print("")
    
    def checkGuess(self, guess:str): # checks the guess against the answer and returns the results
        right_place = 0
        right_dig_only = 0
        answer_num_using = self.number
        for current_index in range(0, len(self.number)):
            if answer_num_using[current_index] == guess[current_index]:
                right_place += 1
                answer_num_using = answer_num_using[:current_index] + "x" + answer_num_using[current_index+1:]
                guess = guess[:current_index] + "y" + guess[current_index+1:]
        for current_index in range(0, len(self.number)):
            if guess[current_index] in answer_num_using:
                right_dig_only += 1
                correct_num_index = answer_num_using.index(guess[current_index])
                answer_num_using = answer_num_using[:correct_num_index] + "x" + answer_num_using[correct_num_index+1:]
                guess = guess[:current_index] + "y" + guess[current_index+1:]
        return right_place, right_dig_only
    
    def displayResults(self): # displays a table of all the guesses
        print("\033[1;35m A = number of correct digits in the correct place")
        print("\033[1;36m B = Number of correct digits not in the correct place")
        str_of_results = "\033[1;32m No. \033[1;34m \tGuess \033[1;35m \tA \033[1;36m \tB \n \033[1;39m"
        for guess_set in self.all_results:
            str_of_results += str("\033[1;32m"+guess_set[0]+"\033[1;34m"+" \t"+guess_set[1]+"\033[1;35m"+" \t"+guess_set[2]+"\033[1;36m"+" \t"+guess_set[3]+" \n \033[1;39m")
        print(str_of_results)
        
    def doDigitsFit(self, guess):
        possible_digits = "0123456"
        if len(str(guess)) != 4:
            return False
        for digit in str(guess):
            if digit not in possible_digits:
                return False
        return True
                
    def run(self):
        guesses = 1
        guess = ""
        self.typingPrint("Mastermind")
        while not self.doDigitsFit(guess):
            guess = input("\033[1;39m Please guess a 4 digit number(using digits 0, 1, 2, 3, 4, 5, 6):")
        while guess != self.number:
            results = self.checkGuess(guess)
            self.all_results += [[str(guesses), guess, str(results[0]), str(results[1])]]
            self.displayResults()
            guess = ""
            while not self.doDigitsFit(guess):
                guess = input("\033[1;39m Please guess a 4 digit number(using digits 0, 1, 2, 3, 4, 5, 6):")
            guesses += 1
        print("Correct well done! You got it in "+str(guesses)+" tries")

MasterMind().run()
