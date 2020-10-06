from urllib.request import urlopen
def fetch_words():
    story =  urlopen('http://sixty-north.com/c/t.txt')
  #  story_words = []
    x=2
    while x < 10:
        print(x)
        x += 1
    else:
        print("loop over")

    #line.decode = functional coding
  #  for line in story:
   #     line_words = line.decode('utf-8').split()
    ##       print(word)
            #story_words.append(word)
    story.close()

    #print(story_words)


if __name__ == "__main__":
    fetch_words()