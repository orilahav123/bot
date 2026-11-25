import os
from datetime import datetime

memories = []

def save():
    file = open("memories.txt", "w")
    for memory in memories:
        file.write(memory["time"] + "|" + memory["text"] + "\n")
    file.close()

def load():
    if os.path.exists("memories.txt"):
        file = open("memories.txt", "r")
        for line in file:
            clean = line.strip()
            if "|" in clean:
                pieces = clean.split("|", 1)
                memory = {"time": pieces[0], "text": pieces[1]}
            else:
                memory = {"time": "unknown", "text": clean}
            memories.append(memory)
        file.close()

def found_in(memory,search):
    prefixes = ["ל", "מ", "ב", "ה", "ו"]
    good_memory = memory.split()
    search = search.strip(".")
    for word in good_memory:
        word = word.strip(".")
        if len(word)> 0:
            if word[0] in prefixes and word[1:] == search or word == search:
                return True
    return False

def recall(memories, query):
    words = query.split()
    results = []
    for memory in memories:
        all_words = True
        for word in words:
            if not found_in(memory["text"], word):
                all_words = False
        if all_words == True:
            results.append(memory)
    return results

def forget(memories,number_text):
    if number_text.isdigit():
        num = int(number_text)
        if num >= 1 and num <= len(memories):
            index = num - 1
            del memories[index]
            return "forgotten"
        else:
            return "number doesnt exist"
    else:
        return "please select number from the list"  


def main():
    load()
    sentence = " "
    while sentence.lower() != "exit":
        sentence = input(" ")
        parts = sentence.split(" ", 1)
        parts[0] = parts[0].lower()
        if parts[0] == "remember":
            if len(parts) > 1:
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                new_memory = {"text": parts[1], "time": now}
                memories.append(new_memory)
                save()
                print("saved")
            else:
                print("remember what?")
        elif parts[0] == "list":
            number = 1
            for memory in memories:
                print(number, memory["text"], "(" + memory["time"] + ")")
                number = number + 1
        elif parts[0] == "forget":
            if len(parts) > 1:
                message =forget (memories,parts[1])
                if message == "forgotten":
                    save()
                print(message)
            else:
                print("which number to forget?")
        elif parts[0] == "recall":
            if len(parts) > 1:
                results = recall(memories, parts[1])
                if len(results) == 0:
                    print("memory doesnt exist")
                else:
                    for memory in results:
                        print(memory["text"], "(" + memory["time"] + ")")
            else:
                print("recall what?")

if __name__ == "__main__":
    main()